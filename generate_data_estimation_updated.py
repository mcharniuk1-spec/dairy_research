#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import copy
import math
import re
import struct
from typing import Union
import xml.etree.ElementTree as ET
import zipfile

import pandas as pd

from generate_rw4_interpretation_report import _find_thesis_root, _load_context


NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_PIC = "http://schemas.openxmlformats.org/drawingml/2006/picture"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_XML = "http://www.w3.org/XML/1998/namespace"

ET.register_namespace("w", NS_W)
ET.register_namespace("wp", NS_WP)
ET.register_namespace("a", NS_A)
ET.register_namespace("pic", NS_PIC)
ET.register_namespace("r", NS_R)

W_VAL = f"{{{NS_W}}}val"
XML_SPACE = f"{{{NS_XML}}}space"

REPO_ROOT = Path(__file__).resolve().parent
OUTPUTS_ROOT = REPO_ROOT / "outputs"
PRIMARY_PATH = OUTPUTS_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"

R_ID_BASE = 5000
DOC_PR_ID_BASE = 7000


def _w(tag: str) -> str:
    return f"{{{NS_W}}}{tag}"


def _wp(tag: str) -> str:
    return f"{{{NS_WP}}}{tag}"


def _a(tag: str) -> str:
    return f"{{{NS_A}}}{tag}"


def _pic(tag: str) -> str:
    return f"{{{NS_PIC}}}{tag}"


@dataclass
class ParagraphBlock:
    text: str
    style: str | None = None
    page_break_before: bool = False


@dataclass
class FigureBlock:
    path: Path
    caption: str
    source: str
    caption_style: str = "Subtitle"
    width_in: float = 5.9


@dataclass
class TableBlock:
    caption: str
    headers: list[str]
    rows: list[list[str]]
    source: str
    caption_style: str = "Subtitle"
    style_id: str = "TableGrid"


Block = Union[ParagraphBlock, FigureBlock, TableBlock]


def _safe_num(value: object) -> float | None:
    if value is None:
        return None
    try:
        num = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(num):
        return None
    return num


def _fmt_number(value: object, digits: int = 3) -> str:
    num = _safe_num(value)
    if num is None:
        return "n/a"
    abs_num = abs(num)
    if abs_num >= 100:
        return f"{num:,.1f}"
    if abs_num >= 10:
        return f"{num:,.2f}"
    return f"{num:,.{digits}f}"


def _fmt_percent(value: object, digits: int = 1) -> str:
    num = _safe_num(value)
    if num is None:
        return "n/a"
    return f"{num * 100:.{digits}f}%"


def _fmt_int(value: object) -> str:
    num = _safe_num(value)
    if num is None:
        return "n/a"
    return f"{int(round(num)):,}"


def _b(text: str) -> str:
    return f"**{text}**"


def _b_num(value: object, digits: int = 3) -> str:
    return _b(_fmt_number(value, digits=digits))


def _b_pct(value: object, digits: int = 1) -> str:
    return _b(_fmt_percent(value, digits=digits))


def _b_int(value: object) -> str:
    return _b(_fmt_int(value))


def _inline_parts(text: str) -> list[tuple[str, bool]]:
    if not text:
        return [("", False)]
    parts = re.split(r"(\*\*.*?\*\*)", text)
    runs: list[tuple[str, bool]] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) >= 4:
            runs.append((part[2:-2], True))
        else:
            runs.append((part, False))
    return runs or [("", False)]


def _make_paragraph(text: str, style: str | None = None, page_break_before: bool = False) -> ET.Element:
    paragraph = ET.Element(_w("p"))
    if style or page_break_before:
        ppr = ET.SubElement(paragraph, _w("pPr"))
        if style:
            pstyle = ET.SubElement(ppr, _w("pStyle"))
            pstyle.set(W_VAL, style)
        if page_break_before:
            ET.SubElement(ppr, _w("pageBreakBefore"))
    for run_text, bold in _inline_parts(text):
        run = ET.SubElement(paragraph, _w("r"))
        if bold:
            rpr = ET.SubElement(run, _w("rPr"))
            ET.SubElement(rpr, _w("b"))
        text_el = ET.SubElement(run, _w("t"))
        if run_text.startswith(" ") or run_text.endswith(" ") or "  " in run_text:
            text_el.set(XML_SPACE, "preserve")
        text_el.text = run_text
    if not list(paragraph):
        run = ET.SubElement(paragraph, _w("r"))
        ET.SubElement(run, _w("t")).text = ""
    return paragraph


def _make_table(headers: list[str], rows: list[list[str]], style_id: str = "TableGrid") -> ET.Element:
    w_type = f"{{{NS_W}}}type"
    w_w = f"{{{NS_W}}}w"
    w_sz = f"{{{NS_W}}}sz"
    w_space = f"{{{NS_W}}}space"
    w_color = f"{{{NS_W}}}color"
    w_fill = f"{{{NS_W}}}fill"

    table = ET.Element(_w("tbl"))
    tbl_pr = ET.SubElement(table, _w("tblPr"))
    tbl_style = ET.SubElement(tbl_pr, _w("tblStyle"))
    tbl_style.set(W_VAL, style_id)
    tbl_w = ET.SubElement(tbl_pr, _w("tblW"))
    tbl_w.set(w_w, "0")
    tbl_w.set(w_type, "auto")
    tbl_layout = ET.SubElement(tbl_pr, _w("tblLayout"))
    tbl_layout.set(w_type, "autofit")
    tbl_borders = ET.SubElement(tbl_pr, _w("tblBorders"))
    for border_name in ["top", "left", "bottom", "right", "insideH", "insideV"]:
        border = ET.SubElement(tbl_borders, _w(border_name))
        border.set(W_VAL, "single")
        border.set(w_sz, "4")
        border.set(w_space, "0")
        border.set(w_color, "auto")

    tbl_grid = ET.SubElement(table, _w("tblGrid"))
    for _ in headers:
        ET.SubElement(tbl_grid, _w("gridCol"))

    def add_row(cells: list[str], header: bool = False) -> None:
        tr = ET.SubElement(table, _w("tr"))
        for cell_text in cells:
            tc = ET.SubElement(tr, _w("tc"))
            tc_pr = ET.SubElement(tc, _w("tcPr"))
            tc_w = ET.SubElement(tc_pr, _w("tcW"))
            tc_w.set(w_w, "0")
            tc_w.set(w_type, "auto")
            v_align = ET.SubElement(tc_pr, _w("vAlign"))
            v_align.set(W_VAL, "top")
            para = _make_paragraph(f"**{cell_text}**" if header else cell_text, style="NoSpacing")
            tc.append(para)

    add_row(headers, header=True)
    for row in rows:
        normalized = ["" if cell is None else str(cell) for cell in row]
        add_row(normalized, header=False)
    return table


def _png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        header = fh.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Unsupported image format for {path}; expected PNG.")
    return struct.unpack(">II", header[16:24])


def _image_extents(path: Path, width_in: float) -> tuple[int, int]:
    width_px, height_px = _png_size(path)
    emu_per_inch = 914400
    cx = int(width_in * emu_per_inch)
    cy = int(cx * height_px / width_px)
    return cx, cy


def _make_image_paragraph(image_path: Path, rel_id: str, docpr_id: int, width_in: float = 5.9) -> ET.Element:
    cx, cy = _image_extents(image_path, width_in)

    paragraph = ET.Element(_w("p"))
    ppr = ET.SubElement(paragraph, _w("pPr"))
    jc = ET.SubElement(ppr, _w("jc"))
    jc.set(W_VAL, "center")

    run = ET.SubElement(paragraph, _w("r"))
    drawing = ET.SubElement(run, _w("drawing"))
    inline = ET.SubElement(drawing, _wp("inline"))
    inline.set("distT", "0")
    inline.set("distB", "0")
    inline.set("distL", "0")
    inline.set("distR", "0")

    extent = ET.SubElement(inline, _wp("extent"))
    extent.set("cx", str(cx))
    extent.set("cy", str(cy))

    effect = ET.SubElement(inline, _wp("effectExtent"))
    effect.set("l", "0")
    effect.set("t", "0")
    effect.set("r", "0")
    effect.set("b", "0")

    doc_pr = ET.SubElement(inline, _wp("docPr"))
    doc_pr.set("id", str(docpr_id))
    doc_pr.set("name", image_path.name)

    c_nv = ET.SubElement(inline, _wp("cNvGraphicFramePr"))
    graphic_frame_locks = ET.SubElement(c_nv, _a("graphicFrameLocks"))
    graphic_frame_locks.set("noChangeAspect", "1")

    graphic = ET.SubElement(inline, _a("graphic"))
    graphic_data = ET.SubElement(graphic, _a("graphicData"))
    graphic_data.set("uri", "http://schemas.openxmlformats.org/drawingml/2006/picture")

    pic = ET.SubElement(graphic_data, _pic("pic"))
    nv_pic_pr = ET.SubElement(pic, _pic("nvPicPr"))
    c_nv_pr = ET.SubElement(nv_pic_pr, _pic("cNvPr"))
    c_nv_pr.set("id", str(docpr_id))
    c_nv_pr.set("name", image_path.name)
    c_nv_pic_pr = ET.SubElement(nv_pic_pr, _pic("cNvPicPr"))
    pic_locks = ET.SubElement(c_nv_pic_pr, _a("picLocks"))
    pic_locks.set("noChangeAspect", "1")

    blip_fill = ET.SubElement(pic, _pic("blipFill"))
    blip = ET.SubElement(blip_fill, _a("blip"))
    blip.set(f"{{{NS_R}}}embed", rel_id)
    stretch = ET.SubElement(blip_fill, _a("stretch"))
    ET.SubElement(stretch, _a("fillRect"))

    sp_pr = ET.SubElement(pic, _pic("spPr"))
    xfrm = ET.SubElement(sp_pr, _a("xfrm"))
    off = ET.SubElement(xfrm, _a("off"))
    off.set("x", "0")
    off.set("y", "0")
    ext = ET.SubElement(xfrm, _a("ext"))
    ext.set("cx", str(cx))
    ext.set("cy", str(cy))
    prst = ET.SubElement(sp_pr, _a("prstGeom"))
    prst.set("prst", "rect")
    ET.SubElement(prst, _a("avLst"))

    return paragraph


def _add_relationship(rels_root: ET.Element, rel_id: str, target: str) -> None:
    rel = ET.SubElement(rels_root, f"{{{NS_PKG_REL}}}Relationship")
    rel.set("Id", rel_id)
    rel.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
    rel.set("Target", target)


def _ensure_png_content_type(content_root: ET.Element) -> None:
    for node in content_root:
        if node.tag.endswith("Default") and node.get("Extension") == "png":
            return
    new_default = ET.Element(content_root[0].tag)
    new_default.set("Extension", "png")
    new_default.set("ContentType", "image/png")
    content_root.append(new_default)


def _select_first(df: pd.DataFrame, mask: pd.Series) -> pd.Series:
    subset = df.loc[mask].copy()
    if subset.empty:
        raise RuntimeError("Expected data row not found while building the thesis chapter update.")
    return subset.iloc[0]


def _coverage_row(coverage: pd.DataFrame, stage_from: str, stage_to: str) -> pd.Series:
    return _select_first(coverage, (coverage["stage_from"] == stage_from) & (coverage["stage_to"] == stage_to))


def _coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.columns:
        try:
            out[col] = pd.to_numeric(out[col])
        except (TypeError, ValueError):
            continue
    return out


def _brand_missing_mask(series: pd.Series) -> pd.Series:
    return series.isna() | series.astype(str).str.strip().eq("")


def _load_product_book(product: str, retailer: str) -> dict[str, pd.DataFrame]:
    path = OUTPUTS_ROOT / product / retailer / "primary_chain_output.xlsx"
    return {
        "path": path,
        "PreTests": _coerce_numeric(pd.read_excel(path, sheet_name="PreTests")),
        "ModelCoefficients": _coerce_numeric(pd.read_excel(path, sheet_name="ModelCoefficients")),
        "ResidualDiagnostics": _coerce_numeric(pd.read_excel(path, sheet_name="ResidualDiagnostics")),
        "LagProfile": _coerce_numeric(pd.read_excel(path, sheet_name="LagProfile")),
        "ModelEligibility": _coerce_numeric(pd.read_excel(path, sheet_name="ModelEligibility")),
    }


def _mc_row(book: dict[str, pd.DataFrame], link: str, model_family: str) -> pd.Series:
    df = book["ModelCoefficients"]
    return _select_first(df, (df["link"] == link) & (df["model_family"] == model_family))


def _diag_row(book: dict[str, pd.DataFrame], link: str, model_family: str) -> pd.Series:
    df = book["ResidualDiagnostics"]
    return _select_first(df, (df["link"] == link) & (df["model_family"] == model_family))


def _lag_top(book: dict[str, pd.DataFrame], pair: str) -> pd.Series:
    df = book["LagProfile"]
    subset = df[df["pair"] == pair].sort_values("corr", ascending=False)
    return subset.iloc[0]


def _pretest_pair(book: dict[str, pd.DataFrame], pair_name: str) -> pd.Series:
    df = book["PreTests"]
    return _select_first(df, df["series"] == pair_name)


def _build_blocks() -> list[Block]:
    ctx = _load_context()
    thesis_root = _find_thesis_root()

    run = ctx["run"]
    total = ctx["total"]
    primary = ctx["primary"]
    discounts = ctx["discounts"]
    corr = ctx["corr"]
    brand_ctx = ctx["brand"]
    forecast = ctx["forecast"]
    decomposition = ctx["decomposition"]
    intersection = ctx["intersection"]

    run_summary = run["Run_All_Summary"].copy()
    sheets_index = run["Sheets_Index"].copy()
    category_summary = total["02_CategorySummary"].copy()

    coef = _coerce_numeric(primary["Consolidated_ModelCoefficients"])
    pretests = _coerce_numeric(primary["Consolidated_PreTests"])
    reverse = _coerce_numeric(primary["ReverseFlow_ModelCoefficients"])
    raw = _coerce_numeric(primary["RawMilk_To_Product_Transmission"])
    brand = _coerce_numeric(primary["Retailer_Brand_Transmission"])
    robustness = _coerce_numeric(primary["Variant_Robustness"])
    farmgate_compare = _coerce_numeric(primary["FarmGate_Source_Comparison"])
    farmgate_direct = _coerce_numeric(primary["FarmGate_Direct_Summary"])
    farmgate_reverse = _coerce_numeric(primary["FarmGate_Reverse_Summary"])
    farmgate_variant = _coerce_numeric(primary["FarmGate_Variant_Stability"])
    unified_retail = _coerce_numeric(primary["Unified_Retail_Comparison"])
    intersection_stability = _coerce_numeric(primary["Intersection_Stability"])
    benchmark = _coerce_numeric(primary["Benchmark_Comparison"])
    coverage = _coerce_numeric(primary["Coverage_Validation"])
    mapping = _coerce_numeric(primary["Mapping_Audit"])
    unit = _coerce_numeric(primary["Unit_Admissibility"])
    retail_combined_diag = _coerce_numeric(primary["Retail_Combined_Diagnostics"])
    panel_index = _coerce_numeric(pd.read_excel(PRIMARY_PATH, sheet_name="Panel_Index"))

    asymmetry = _coerce_numeric(discounts["Asymmetry_Observed_vs_Baseline"])
    discount_synthesis = discounts["Discount_Strategy_Synthesis"].copy()
    lag_best = _coerce_numeric(corr["Lag_Best"])
    brand_io = _coerce_numeric(brand_ctx["Brand_IO_Metrics"])
    region = _coerce_numeric(brand_ctx["Prozorro_ByRegion"])
    forecast_summary = _coerce_numeric(forecast["Forecast_Summary"])
    synthetic_link = _coerce_numeric(forecast["Synthetic_to_Consumer_Link"])
    decomp_summary = _coerce_numeric(decomposition["Decomposition_Summary"])

    butter = _load_product_book("butter", "silpo_novus")
    milk = _load_product_book("milk", "silpo")
    hard_cheese = _load_product_book("hard_cheese", "silpo_novus")
    cream = _load_product_book("cream", "silpo")
    sour_cream = _load_product_book("sour_cream", "silpo_novus")

    steps_ok = int((run_summary["status"].astype(str) == "ok").sum())
    total_steps = len(run_summary)
    total_graphs = len(list(OUTPUTS_ROOT.rglob("*.png")))
    current_sheets = len(sheets_index)
    total_tables = int(pd.to_numeric(category_summary["tables"], errors="coerce").fillna(0).sum())
    total_rows = int(pd.to_numeric(category_summary["rows_total"], errors="coerce").fillna(0).sum())

    mapping_total = len(mapping)
    matched_share = (mapping["mapping_quality_flag"].astype(str) == "matched").mean()
    multi_share = (mapping["mapping_quality_flag"].astype(str) == "multi_match").mean()
    unmatched_share = (mapping["mapping_quality_flag"].astype(str) == "unmatched").mean()
    comparable_share = pd.to_numeric(mapping["economically_comparable_flag"], errors="coerce").fillna(0).mean()

    unit_lookup = {
        (str(row["source"]), str(row["admissibility_reason"])): row for _, row in unit.iterrows()
    }

    coef_core = pd.to_numeric(coef["core_finding_flag"], errors="coerce").fillna(0)
    ok_share = (coef["model_status"].astype(str) == "ok").mean()
    unreliable_share = pd.to_numeric(coef["unreliable_flag"], errors="coerce").fillna(0).mean()
    core_share = coef_core.mean()
    coint_share = (pd.to_numeric(pretests["cointegration_p"], errors="coerce") < 0.10).mean()
    integration_y = pretests["integration_y"].astype(str)
    no_fit = coef[coef["model_family"].astype(str) == "NO_FIT"]
    no_fit_i2 = int((no_fit["unreliable_reason"].astype(str) == "i2_series_blocked").sum())
    no_fit_overlap = int((no_fit["unreliable_reason"].astype(str) == "insufficient_overlap").sum())
    robust_linear = pd.to_numeric(robustness["robust_linear_vs_pchip"], errors="coerce").fillna(0).mean()
    robust_farmgate = pd.to_numeric(farmgate_compare["robust_across_reconstruction"], errors="coerce").fillna(0).mean()
    interpolation_sensitive = pd.to_numeric(robustness["interpolation_sensitive"], errors="coerce").fillna(0).mean()

    panel_counts = panel_index["panel_level"].astype(str).value_counts().to_dict()

    coverage_fp = _coverage_row(coverage, "FarmGateUA", "ProducerUA")
    coverage_pp = _coverage_row(coverage, "ProducerUA", "ProZorro")
    coverage_pr = _coverage_row(coverage, "ProZorro", "Retail")
    coverage_rp = _coverage_row(coverage, "Retail", "ProZorro")
    coverage_brand = _select_first(coverage, coverage["check_type"].astype(str) == "brand_panels")

    raw_best = (
        raw.groupby("stage_to", as_index=False)["core_finding_flag"]
        .agg(["count", "sum", "mean"])
        .reset_index()
        .sort_values("mean", ascending=False)
        .iloc[0]
    )
    raw_stage_summary = (
        raw.groupby("stage_to", as_index=False)["core_finding_flag"]
        .agg(["count", "sum", "mean"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )
    raw_retail_best = _select_first(
        raw.sort_values(["core_finding_flag", "unreliable_flag", "ect_pvalue"], ascending=[False, True, True]),
        raw["stage_to"].astype(str) == "Retail",
    )
    raw_prozorro_best = _select_first(
        raw.sort_values(["core_finding_flag", "unreliable_flag", "ect_pvalue"], ascending=[False, True, True]),
        raw["stage_to"].astype(str) == "ProZorro",
    )

    farmgate_direct_retail = farmgate_direct[
        (farmgate_direct["stage_from"].astype(str) == "FarmGateUA")
        & (farmgate_direct["stage_to"].astype(str) == "Retail")
        & (farmgate_direct["model_family"].astype(str) == "NARDL")
    ].copy()
    fg_retail_anchor_pairwise = _select_first(
        farmgate_direct_retail.sort_values(
            ["core_finding_share", "robust_across_reconstruction_share", "robust_linear_vs_pchip_share", "median_n_obs"],
            ascending=[False, False, False, False],
        ),
        (farmgate_direct_retail["retailer_panel"].astype(str) == "Retail_combined")
        & (farmgate_direct_retail["intersection_rule"].astype(str) == "pairwise_overlap"),
    )
    fg_retail_core_pairwise = _select_first(
        farmgate_direct_retail.sort_values(
            ["core_finding_share", "robust_across_reconstruction_share", "robust_linear_vs_pchip_share", "median_n_obs"],
            ascending=[False, False, False, False],
        ),
        (farmgate_direct_retail["retailer_panel"].astype(str) == "Retail_combined_core")
        & (farmgate_direct_retail["intersection_rule"].astype(str) == "pairwise_overlap"),
    )
    fg_proc_pairwise = _select_first(
        farmgate_direct.sort_values(
            ["core_finding_share", "robust_across_reconstruction_share", "robust_linear_vs_pchip_share", "median_n_obs"],
            ascending=[False, False, False, False],
        ),
        (farmgate_direct["stage_from"].astype(str) == "FarmGateUA")
        & (farmgate_direct["stage_to"].astype(str) == "ProZorro")
        & (farmgate_direct["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_direct["model_family"].astype(str) == "NARDL"),
    )
    fg_reverse_anchor_pairwise = _select_first(
        farmgate_reverse.sort_values(
            ["core_finding_share", "robust_across_reconstruction_share", "robust_linear_vs_pchip_share", "median_n_obs"],
            ascending=[False, False, False, False],
        ),
        (farmgate_reverse["stage_from"].astype(str) == "Retail")
        & (farmgate_reverse["stage_to"].astype(str) == "FarmGateUA")
        & (farmgate_reverse["retailer_panel"].astype(str) == "Retail_combined")
        & (farmgate_reverse["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_reverse["model_family"].astype(str) == "NARDL"),
    )
    fg_reverse_core_pairwise = _select_first(
        farmgate_reverse.sort_values(
            ["core_finding_share", "robust_across_reconstruction_share", "robust_linear_vs_pchip_share", "median_n_obs"],
            ascending=[False, False, False, False],
        ),
        (farmgate_reverse["stage_from"].astype(str) == "Retail")
        & (farmgate_reverse["stage_to"].astype(str) == "FarmGateUA")
        & (farmgate_reverse["retailer_panel"].astype(str) == "Retail_combined_core")
        & (farmgate_reverse["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_reverse["model_family"].astype(str) == "NARDL"),
    )

    retail_combined_diag_anchor = retail_combined_diag[retail_combined_diag["panel_name"].astype(str) == "Retail_combined"].copy()
    retail_combined_diag_core = retail_combined_diag[retail_combined_diag["panel_name"].astype(str) == "Retail_combined_core"].copy()
    consumer_supported_products = int(pd.to_numeric(retail_combined_diag_anchor.get("coverage_consumer"), errors="coerce").fillna(0).gt(0).sum())
    anchor_overlap_median = pd.to_numeric(retail_combined_diag_anchor.get("retailer_overlap_share"), errors="coerce").median()
    core_overlap_median = pd.to_numeric(retail_combined_diag_core.get("retailer_overlap_share"), errors="coerce").median()
    anchor_consumer_weight_median = pd.to_numeric(retail_combined_diag_anchor.get("weight_consumer"), errors="coerce").median()

    brand_missing_share = _brand_missing_mask(brand["brand"]).mean()
    brand_core_share = pd.to_numeric(brand["core_finding_flag"], errors="coerce").fillna(0).mean()
    brand_by_retailer = (
        brand.assign(core_finding_flag=pd.to_numeric(brand["core_finding_flag"], errors="coerce").fillna(0))
        .groupby("retailer_panel", as_index=False)["core_finding_flag"]
        .agg(["count", "sum", "mean"])
        .reset_index()
    )
    silpo_brand = brand_by_retailer.loc[brand_by_retailer["retailer_panel"] == "Silpo"].iloc[0]
    novus_brand = brand_by_retailer.loc[brand_by_retailer["retailer_panel"] == "Novus"].iloc[0]

    reverse_core_share = coverage_rp["core_finding_rows"] / coverage_rp["rows_total"]
    retail_to_producer = _select_first(
        reverse.sort_values(["core_finding_flag", "unreliable_flag", "ect_pvalue"], ascending=[False, True, True]),
        (reverse["stage_from"].astype(str) == "Retail")
        & (reverse["stage_to"].astype(str) == "ProducerUA")
        & (reverse["model_family"].astype(str) == "NARDL"),
    )

    family_counts = coef["model_family"].astype(str).value_counts().to_dict()
    family_core = (
        coef.assign(core_finding_flag=coef_core)
        .groupby("model_family", as_index=False)["core_finding_flag"]
        .sum()
        .set_index("model_family")["core_finding_flag"]
        .to_dict()
    )
    dynamic_core_rows = int(family_core.get("NARDL", 0) + family_core.get("ECM", 0))
    total_core_rows = int(coef_core.sum())

    benchmark["abs_corr"] = pd.to_numeric(benchmark["corr_at_best_lag"], errors="coerce").abs()
    benchmark_best = benchmark.groupby(["benchmark_source", "stage"], as_index=False)["abs_corr"].mean().sort_values("abs_corr", ascending=False).head(3)

    top_hhi = brand_io.sort_values("hhi_brand", ascending=False).head(3)
    top_region = region.sort_values("cv", ascending=False).head(3)
    top_seasonal = decomp_summary.sort_values("seasonal_strength", ascending=False).head(4)

    discount_lookup = {
        str(row["question"]): (str(row["answer"]), str(row["evidence"])) for _, row in discount_synthesis.iterrows()
    }
    delta_sr_mean = pd.to_numeric(asymmetry["delta_sr_coef"], errors="coerce").abs().mean()
    delta_lr_mean = pd.to_numeric(asymmetry["delta_lr_coef"], errors="coerce").abs().mean()
    delta_ect_mean = pd.to_numeric(asymmetry["delta_ect_coef"], errors="coerce").abs().mean()
    pseudo_asymmetry_share = pd.to_numeric(asymmetry["pseudo_asymmetry_likely"], errors="coerce").fillna(0).mean()

    producer_rmse = forecast_summary.loc[forecast_summary["target"].astype(str) == "ProducerUA", "rmse_dlog"]
    consumer_rmse = forecast_summary.loc[forecast_summary["target"].astype(str) == "ConsumerUA", "rmse_dlog"]
    forecast_r2 = forecast_summary["r2_train"]
    synth_best = synthetic_link.sort_values("p_synth_to_consumer", ascending=True).iloc[0]

    butter_prod = _mc_row(butter, "producer_to_prozorro", "NARDL")
    butter_prod_diag = _diag_row(butter, "producer_to_prozorro", "NARDL")
    butter_lag_prod = _lag_top(butter, "producer_to_prozorro")
    butter_lag_proc = _lag_top(butter, "prozorro_to_retail")
    butter_ardl = _mc_row(butter, "prozorro_to_retail", "ARDL")
    butter_ecm = _mc_row(butter, "prozorro_to_retail", "ECM")
    butter_nardl = _mc_row(butter, "prozorro_to_retail", "NARDL")
    butter_ecm_diag = _diag_row(butter, "prozorro_to_retail", "ECM")

    milk_ardl_up = _mc_row(milk, "producer_to_prozorro", "ARDL")
    milk_ecm_up = _mc_row(milk, "producer_to_prozorro", "ECM")
    milk_nardl_up = _mc_row(milk, "producer_to_prozorro", "NARDL")
    milk_ecm = _mc_row(milk, "prozorro_to_retail", "ECM")
    milk_nardl = _mc_row(milk, "prozorro_to_retail", "NARDL")
    milk_ecm_diag = _diag_row(milk, "prozorro_to_retail", "ECM")
    milk_lag_proc = _lag_top(milk, "prozorro_to_retail")
    milk_lag_prod = _lag_top(milk, "producer_to_prozorro")

    hard_prod = _mc_row(hard_cheese, "producer_to_prozorro", "NARDL")
    hard_prod_diag = _diag_row(hard_cheese, "producer_to_prozorro", "NARDL")
    hard_ardl = _mc_row(hard_cheese, "prozorro_to_retail", "ARDL")
    hard_nardl = _mc_row(hard_cheese, "prozorro_to_retail", "NARDL")
    hard_lag_prod = _lag_top(hard_cheese, "producer_to_prozorro")
    hard_lag_proc = _lag_top(hard_cheese, "prozorro_to_retail")

    cream_prod = _mc_row(cream, "producer_to_prozorro", "NARDL")
    sour_prod_ardl = _mc_row(sour_cream, "producer_to_prozorro", "ARDL")
    sour_prod_nardl = _mc_row(sour_cream, "producer_to_prozorro", "NARDL")
    sour_retail_ardl = _mc_row(sour_cream, "prozorro_to_retail", "ARDL")
    sour_retail_nardl = _mc_row(sour_cream, "prozorro_to_retail", "NARDL")
    sour_lag_proc = _lag_top(sour_cream, "prozorro_to_retail")

    lag_best_sorted = lag_best.sort_values("corr", ascending=False)
    lag_top_1 = lag_best_sorted.iloc[0]
    lag_top_2 = lag_best_sorted.iloc[1]
    lag_top_3 = lag_best_sorted.iloc[2]

    blocks: list[Block] = []
    current_chapter: int | None = None
    figure_counters: dict[int, int] = {5: 0, 6: 0}

    def para(text: str, style: str | None = None, page_break_before: bool = False) -> None:
        nonlocal current_chapter
        chapter_match = re.match(r"Chapter\s+([56])\.", str(text).strip())
        if style == "Heading1" and chapter_match:
            current_chapter = int(chapter_match.group(1))
        blocks.append(ParagraphBlock(text=text, style=style, page_break_before=page_break_before))

    def fig(path: str, caption: str, source: str, caption_style: str = "Subtitle", width_in: float = 5.9) -> None:
        numbered_caption = caption
        if current_chapter in figure_counters and not re.match(r"^\s*Figure\s+\d+\.\d+", caption):
            figure_counters[current_chapter] += 1
            numbered_caption = f"Figure {current_chapter}.{figure_counters[current_chapter]}. {caption}"
        blocks.append(
            FigureBlock(
                path=Path(path),
                caption=numbered_caption,
                source=source,
                caption_style=caption_style,
                width_in=width_in,
            )
        )

    para("Chapter 5. Data", "Heading1")
    para(
        "This chapter documents the empirical data architecture of the thesis and explains how heterogeneous raw sources are converted into a coherent system of analytical layers. "
        "The objective is not merely to inventory datasets, but to justify why each source can be treated as a distinct institutional node of price formation: farm-gate supply conditions, processor pricing, public procurement, and managed retail prices do not represent the same market mechanism and should not be interpreted as if they did. "
        f"The current RW4 rerun is complete, with {_b_int(steps_ok)} of {_b_int(total_steps)} module steps finished successfully, {_b_int(current_sheets)} indexed current sheets, {_b_int(total_tables)} bundled tables, and {_b_int(total_graphs)} saved graphs across the output tree. "
        "This updated chapter therefore preserves the structure of the draft, but rewrites the empirical story directly from the present rerun and places more weight on identification, admissibility, and economic meaning."
    )

    para("5.1 Data sources and datasets", "Heading2")
    para(
        "All source data are first collected in a common UAH-aligned environment and then transferred into clean analytical tables and modelling panels. "
        "Each panel represents a distinct price-formation regime rather than a mere storage layer: raw-milk farm-gate pricing, processor-level domestic prices, institutional procurement, retail pricing, and external benchmarks all enter the analysis because they capture different points in the dairy chain."
    )
    para(
        "That layered design is central to the research question. If vertical coordination exists in the Ukrainian dairy market, it should emerge as a sequence of adjustments across institutional regimes, not as one universal pass-through coefficient. "
        "The data chapter is therefore also part of the identification strategy: it clarifies which layers can plausibly transmit shocks, which layers mainly buffer them, and where retail governance is likely to modify the observed response."
    )

    para("5.1.1 FarmGateUA (raw-milk farm-gate benchmark and reconstructed daily layer).", "Heading3")
    para(
        "The raw-milk farm-gate layer now has a clearer analytical status than in the earlier draft. It is the only layer that originates as an official farm-level benchmark rather than as a processed-dairy price environment. "
        "The monthly benchmark is transformed into daily paths in two versions, the initial reconstruction and the filled reconstruction, and each is carried with both linear and pchip variants so that later inference can be checked against reconstruction risk instead of being hidden inside one synthetic series."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_farmgateua_initial" / "sheet_farmgateua_initial_timeseries_by_standardized_type.png"),
        "Ukrainian raw-milk farm-gate prices by standardized type (initial reconstructed daily benchmark)",
        "Source: author's calculations based on the farm_gate_daily.xlsx benchmark and the RW4 farm-gate reconstruction.",
        caption_style="Subtitle",
    )
    para(
        f"The admissibility statistics confirm that this layer is technically clean even if it is economically difficult. The initial farm-gate table keeps {_b_pct(unit_lookup[('FarmGateUA_initial', 'uah_per_kg')]['admissible_share'])} admissible rows across {_b_int(unit_lookup[('FarmGateUA_initial', 'uah_per_kg')]['rows'])} observations, and the gap-filled version keeps {_b_pct(unit_lookup[('FarmGateUA_filled', 'uah_per_kg')]['admissible_share'])} across {_b_int(unit_lookup[('FarmGateUA_filled', 'uah_per_kg')]['rows'])}. "
        "What remains difficult is not unit comparability but the economic fact that one national raw-milk benchmark is a coarse proxy for a highly heterogeneous procurement environment."
    )

    para("5.1.2 ProducerUA (processor-level domestic producer prices).", "Heading3")
    para(
        "A series of daily synthetic domestic producer prices is developed for standardized dairy product types. In the updated interpretation, this layer does not represent farm-gate prices; it is the processor-level domestic producer-price layer for processed dairy categories. "
        "It therefore stands at the first clearly product-differentiated stage after raw milk has already entered processing."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_producerua" / "sheet_producerua_timeseries_by_product.png"),
        "Ukrainian producer prices by products",
        "Source: author's calculations based on the current RW4 ProducerUA layer.",
        caption_style="Subtitle",
    )
    para(
        f"These series display persistent common trends and are mostly I(1)-like, which is why they are better suited to cointegration and error-correction logic than to naive level regressions. "
        f"The strongest external coherence in the benchmark comparison also appears at the producer layer, with mean absolute best-lag correlation of {_b_num(benchmark_best.iloc[0]['abs_corr'])} in the leading benchmark pairing. "
        "Economically, that makes ProducerUA the cleanest domestic anchor for the upstream part of the chain."
    )

    para("5.1.3 Prozorro", "Heading3")
    para(
        "Tender contract prices form the procurement price layer. They adjust in discrete steps rather than continuously because of fixed contracts, budgeting periods, and detailed specifications written into tenders. "
        "Product heterogeneity enters through packaging, fat content, lot size, and delivery terms, so mapping and unit standardization are necessary before procurement-price differences can be interpreted economically."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_prozorro" / "sheet_prozorro_timeseries_by_product.png"),
        "Ukrainian bulk company-level prices (procurement prices, can be interpreted as processors) by products",
        "Source: author's calculations based on the current RW4 ProZorro layer.",
        caption_style="Subtitle",
    )
    para(
        f"After unit normalization, the procurement layer remains broad but not homogeneous. Rows with normalized unit price stay admissible, while {_b_int(unit_lookup[('ProZorro', 'missing_unit_normalized_price')]['rows'])} observations without usable unit normalization are excluded from the comparable sample. "
        "This is exactly the kind of filtering the thesis needs because procurement prices are institutional rather than spot-market observations: contract timing and specification mix matter as much as the underlying market shock."
    )

    para("5.1.4 Retail (Silpo and Novus).", "Heading3")
    para(
        "Online retail prices are observed daily at the product level. The retail layer is split by chain, Silpo and Novus, because the two retailers differ in assortment, promotion intensity, and pricing routines. "
        "Keeping them separate allows the analysis to distinguish common chain-wide responses from retailer-specific pricing behavior."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_novus" / "sheet_novus_timeseries_by_product.png"),
        "Ukrainian Novus retail-level prices by products",
        "Source: author's calculations based on the current RW4 Novus retail layer.",
        caption_style="Subtitle",
    )
    para(
        "Within the same product category, Novus prices display visible dispersion and episodic jumps, which is more consistent with managed retail pricing than with frictionless cost-plus repricing. "
        "For that reason, the Novus layer is informative for heterogeneity, but much thinner for brand-specific transmission than Silpo in the current run."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_silpo" / "sheet_silpo_timeseries_by_product.png"),
        "Ukrainian Silpo retail-level prices by products",
        "Source: author's calculations based on the current RW4 Silpo retail layer.",
        caption_style="Subtitle",
    )
    para(
        "For Silpo, the presence of both an old price and a current price makes it possible to construct a baseline series and to measure discount depth when promotions occur. "
        "This is analytically important because the thesis is trying to distinguish baseline repricing from markdown-based adjustment. "
        "At the category level, the current run suggests that baseline and observed paths often stay quite close, which is consistent with a managed shelf-pricing regime in which promotions absorb part of the short-run pressure without always changing the broader category trend."
    )

    para("5.1.5 External benchmarks (EU and CME).", "Heading3")
    para(
        "EU dairy prices, converted into hryvnia per kilogram, together with CME Class III milk futures converted into hryvnia, are used as external cycle anchors. "
        "These series help identify whether domestic movements reflect broader regional or global dairy conditions rather than purely domestic bargaining or retail frictions."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_cme" / "sheet_cme_distribution.png"),
        "U.S. CME Class III milk prices distribution",
        "Source: author's calculations based on the current RW4 CME benchmark layer.",
        caption_style="Subtitle",
    )
    para(
        "The CME layer is not treated as a structural domestic stage. It is used instead as an external cycle indicator and as a diagnostic reference when interpreting whether domestic price episodes are local or part of a wider dairy shock."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_eu" / "sheet_eu_timeseries_by_product.png"),
        "EU dairy products prices by products",
        "Source: author's calculations based on the current RW4 EU benchmark layer.",
        caption_style="Subtitle",
    )
    para(
        "The EU monitoring series show strong co-movement together with product-specific volatility. This makes the EU layer useful not only as a broad benchmark but also as the structural bridge used to reconstruct higher-frequency movement in the raw-milk farm-gate benchmark."
    )

    para("5.1.6 ConsumerUA (domestic consumer layer).", "Heading3")
    para(
        "Daily synthetic consumer-price series by product type are used for diagnostic context and forecasting checks. They are not part of the core domestic transmission chain, but they help assess whether broader consumer-price dynamics move consistently with the producer and retail layers."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_consumerua" / "sheet_consumerua_timeseries_by_product.png"),
        "Ukrainian consumer prices by products",
        "Source: author's calculations based on the current RW4 ConsumerUA layer.",
        caption_style="Subtitle",
    )
    para(
        "Relative to ProducerUA, the ConsumerUA layer has a stronger consumer-inflation trend and is therefore used primarily as a supporting diagnostic environment. "
        f"In the benchmark comparison, ConsumerUA aligns best with the producer layer, with mean absolute best-lag correlation of {_b_num(benchmark_best.iloc[1]['abs_corr']) if len(benchmark_best) > 1 else _b_num(benchmark_best.iloc[0]['abs_corr'])}. "
        "That makes it useful for judging the plausibility of broader market timing even when it is not used as a structural stage in the main domestic chain."
    )

    para("5.2 Data construction and transformation", "Heading2")
    para(
        "The data-construction pipeline is designed to make vertical price transmission estimable by passing each source through three admissibility gates: product harmonization, unit harmonization, and frequency alignment. "
        "The purpose of these gates is to ensure that the price layers enter the econometric analysis as comparable economic objects rather than as heterogeneous raw observations."
    )
    para(
        "This choice is deliberately conservative. The pipeline does not maximize the number of retained observations at any cost; instead, it prioritizes comparability strong enough to support dynamic interpretation. "
        "In other words, a shorter but economically coherent overlap window is preferred to a longer panel that mixes incompatible package sizes, product definitions, or institutional timings."
    )
    para(
        f"The mapping audit covers {_b_int(mapping_total)} mapped label groups. Exact matches account for {_b_pct(matched_share)}, multi-match cases account for {_b_pct(multi_share)}, and unmatched rows account for {_b_pct(unmatched_share)}. "
        f"Economic comparability remains high at {_b_pct(comparable_share)}. This means the current preparation problem is not broad labeling chaos; it is concentrated in the economically awkward cases where one source carries units or product definitions that do not line up cleanly with the rest of the chain."
    )
    para(
        "Across sources, prices are expressed in UAH per kilogram or in admissible litre-equivalent units where that conversion is economically meaningful. "
        "Retail pricing is handled separately for observed and baseline prices. In Silpo, the old price under discount is treated as the baseline price and the current price as the effective transacted price; when no discount is present, the current price is also the baseline price. "
        "This allows the thesis to carry both the regular-price mechanism and the markdown mechanism without conflating them."
    )
    para(
        f"Frequency alignment follows the same logic. Retail prices are daily, ProducerUA and ConsumerUA are reconstructed to daily frequency, the farm-gate layer is reconstructed in both initial and filled variants, and each reconstructed layer is retained in linear and pchip form. "
        f"That choice matters because interpolation robustness averages only {_b_pct(robust_linear)} and farm-gate-source robustness averages only {_b_pct(robust_farmgate)}. "
        "The modelling datasets are therefore built on strict overlap windows, and the final thesis should keep emphasizing robustness rather than treating interpolation as a neutral preprocessing detail."
    )
    para(
        f"The updated RW4 rerun adds a unified downstream layer in two forms. `Retail_combined` is the anchored consumer-facing retail index that blends Silpo effective prices, Novus observed prices, and a level-aligned ConsumerUA anchor; `Retail_combined_core` keeps only retailer-supported observations. "
        f"That distinction is econometrically important. Consumer support is materially present only for {_b_int(consumer_supported_products)} product groups, the anchored index has a median retailer-overlap share of {_b_pct(anchor_overlap_median)}, and the strict retailer-core version raises that median overlap to {_b_pct(core_overlap_median)}. "
        f"In other words, the anchored layer improves horizon length and macro coherence, while the core layer protects the interpretation against over-reliance on the national consumer anchor. The median ConsumerUA weight in the anchored construction is {_b_num(anchor_consumer_weight_median)}, which is large enough to matter but not large enough to erase retailer-level information completely."
    )

    para("5.3 Diagnostic tests and interpretation", "Heading2")
    para(
        "Before estimating each link, the thesis applies a common set of pre-tests: ADF and KPSS for integration behavior, Ljung-Box for serial dependence, ARCH-type checks for conditional heteroskedasticity, Jarque-Bera for non-normality, and explicit overlap and admissibility screens. "
        "The choice between levels, differencing, and cointegration-based models is therefore made in light of diagnostics rather than imposed mechanically."
    )
    para(
        "This diagnostic layer matters for the credibility of the thesis. The purpose of the tests is not to decorate the output with standard econometric statistics, but to determine whether a coefficient can be read as an economically meaningful adjustment parameter. "
        "Whenever the integration order, overlap, or residual behavior does not support that reading, the specification is downgraded or removed from the core-finding set."
    )
    para(
        f"The consolidated test layer confirms that the environment is heterogeneous rather than uniformly I(1). Among the saved pretests, the dependent series is classified as I(0) in {_b_int((integration_y == 'I(0)').sum())} cases, I(1) in {_b_int((integration_y == 'I(1)').sum())} cases, I(2) in {_b_int((integration_y == 'I(2)').sum())} cases, and ambiguous in {_b_int((integration_y == 'ambiguous').sum())} cases. "
        f"Cointegration support appears in {_b_pct(coint_share)}, which is substantial enough to motivate error-correction models, but not enough to justify forcing every link into the same dynamic form."
    )
    para(
        f"The same diagnostics also explain why the empirical narrative must remain selective. The consolidated coefficient table contains {_b_int(len(coef))} rows, of which {_b_pct(ok_share)} finish with status 'ok', {_b_pct(unreliable_share)} remain unreliable, and only {_b_pct(core_share)} survive into the core-finding layer. "
        f"There are {_b_int(len(no_fit))} explicit NO_FIT rows, dominated by {_b_int(no_fit_i2)} I(2)-blocked cases and {_b_int(no_fit_overlap)} insufficient-overlap cases. "
        "This means the code is actively ruling out mathematically weak estimates rather than hiding them."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_overlay_ln" / "before_after_ln_01.png"),
        "Before/after log transformation (illustrative). Logs stabilize variance and enable elasticity interpretation.",
        "Source: author's calculations based on the current RW4 overlay and transformation outputs.",
        caption_style="Subtitle",
    )
    para(
        "The log transformation reduces variance and makes prices comparable across products with very different absolute price levels. "
        "Because the pre-log series often show variance increasing with the level, the logged version is better suited to linear dynamic modeling and to the elasticity-style interpretation used later in the estimation stage."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_correlations_lags" / "corr_matrix_sources.png"),
        "Cross-source correlation matrix (descriptive). Instantaneous correlations can be weak or misleading in VPT settings.",
        "Source: author's calculations based on the current RW4 correlation and lag outputs.",
        caption_style="Subtitle",
    )
    para(
        "Even when the chain is linked structurally, same-day correlations across layers can remain modest. "
        "In the present dataset, adjustment is delayed, retail prices are influenced by promotions and category management, and procurement prices do not move continuously from day to day. "
        "For that reason, contemporaneous correlation is a descriptive statistic rather than a test of transmission."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_correlations_lags" / "lag_best_bar.png"),
        "Best-lag correlation scan (descriptive). Lag profiles motivate plausible repricing horizons by product and link.",
        "Source: author's calculations based on the current RW4 correlation and lag outputs.",
        caption_style="Subtitle",
    )
    para(
        f"The lag scan is informative precisely because the strongest relationships arise at non-zero lags. In the saved cross-source scan, the strongest positive best-lag examples include {lag_top_1['pair_left']} -> {lag_top_1['pair_right']} for {lag_top_1['product']} at lag {_b_int(lag_top_1['lag_days'])} with correlation {_b_num(lag_top_1['corr'])}, {lag_top_2['pair_left']} -> {lag_top_2['pair_right']} for {lag_top_2['product']} at lag {_b_int(lag_top_2['lag_days'])} with correlation {_b_num(lag_top_2['corr'])}, and {lag_top_3['pair_left']} -> {lag_top_3['pair_right']} for {lag_top_3['product']} at lag {_b_int(lag_top_3['lag_days'])} with correlation {_b_num(lag_top_3['corr'])}. "
        "This pattern is consistent with delayed repricing, contract cycles, and retail smoothing."
    )

    para("5.4 Market-structure and regional heterogeneity diagnostics", "Heading2")
    para(
        "The empirical design does not rely on time-series mechanics alone. It also incorporates market-structure diagnostics because bargaining power, menu costs, contract frictions, and discount-based adjustment are all more plausible when the underlying market environment is concentrated or heterogeneous."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_brand_region" / "brand_hhi.png"),
        "Retail brand concentration (HHI and top-3 share) over time.",
        "Source: author's calculations based on the current RW4 brand-region outputs.",
        caption_style="Subtitle",
    )
    para(
        f"Higher HHI and top-3 shares imply that a product category is more concentrated and therefore that retailers may have more room to manage margins through private labels, assortment, and promotions. "
        f"In the current sample, the sharpest HHI spikes appear in {top_hhi.iloc[0]['source']} {top_hhi.iloc[0]['standardized_type']} at {_b_num(top_hhi.iloc[0]['hhi_brand'])}, {top_hhi.iloc[1]['source']} {top_hhi.iloc[1]['standardized_type']} at {_b_num(top_hhi.iloc[1]['hhi_brand'])}, and {top_hhi.iloc[2]['source']} {top_hhi.iloc[2]['standardized_type']} at {_b_num(top_hhi.iloc[2]['hhi_brand'])}. "
        "These cases must still be interpreted together with SKU counts, but they confirm that concentration is a realistic feature of parts of the retail environment."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_brand_region" / "prozorro_region_median.png"),
        "ProZorro regional median prices by product type (dispersion diagnostic).",
        "Source: author's calculations based on the current RW4 brand-region outputs.",
        caption_style="Subtitle",
    )
    para(
        f"Regional medians also show substantial dispersion. The highest coefficients of variation appear in {top_region.iloc[0]['region']} {top_region.iloc[0]['product']} at {_b_num(top_region.iloc[0]['cv'])}, {top_region.iloc[1]['region']} {top_region.iloc[1]['product']} at {_b_num(top_region.iloc[1]['cv'])}, and {top_region.iloc[2]['region']} {top_region.iloc[2]['product']} at {_b_num(top_region.iloc[2]['cv'])}. "
        "This matters for inference because procurement aggregation cannot assume one homogeneous national institutional market."
    )
    fig(
        str(OUTPUTS_ROOT / "model_short_chain_regional" / "chain_retail_from_producer.png"),
        "Short-chain diagnostic: retail response patterns conditional on upstream movements",
        "Source: author's calculations based on the current RW4 short-chain regional output.",
        caption_style="Subtitle",
    )
    para(
        f"The decomposition layer reinforces the same message. The strongest seasonal signatures are {top_seasonal.iloc[0]['source']} {top_seasonal.iloc[0]['product']} at seasonal strength {_b_num(top_seasonal.iloc[0]['seasonal_strength'])}, {top_seasonal.iloc[1]['source']} {top_seasonal.iloc[1]['product']} at {_b_num(top_seasonal.iloc[1]['seasonal_strength'])}, and {top_seasonal.iloc[2]['source']} {top_seasonal.iloc[2]['product']} at {_b_num(top_seasonal.iloc[2]['seasonal_strength'])}. "
        "This is one reason why the downstream layer cannot be read as a simple passive markup over procurement."
    )

    para("5.5 What data remain after preparation - datasets in models.", "Heading2")
    para(
        "After admissibility filtering and standardization, the relevant modeling universe is defined by actual overlap rather than by the raw length of each dataset. "
        "This matters because the upstream producer-to-procurement link and the downstream procurement-to-retail link differ substantially in the amount of usable joint support."
    )
    para(
        f"The active RW4 chain now uses {_b_int(len(panel_index))} panel definitions: {_b_int(panel_counts.get('product', 0))} product panels, {_b_int(panel_counts.get('average', 0))} average panels, {_b_int(panel_counts.get('comparison', 0))} comparison panels, and {_b_int(panel_counts.get('brand', 0))} brand panels. "
        f"Coverage remains broad, but economically uneven: FarmGateUA -> ProducerUA has {_b_int(coverage_fp['rows_total'])} covered rows and {_b_int(coverage_fp['core_finding_rows'])} core findings; ProducerUA -> ProZorro has {_b_int(coverage_pp['rows_total'])} covered rows and {_b_int(coverage_pp['core_finding_rows'])} core findings; ProZorro -> Retail has {_b_int(coverage_pr['rows_total'])} covered rows and {_b_int(coverage_pr['core_finding_rows'])} core findings; and the brand block adds {_b_int(coverage_brand['rows_total'])} panel definitions with {_b_int(coverage_brand['core_finding_rows'])} core findings."
    )
    para(
        f"The direct raw-milk bypass remains weak: its best-performing target is {raw_best['stage_to']}, but even there the core-finding share is only {_b_pct(raw_best['mean'])}. "
        "So the new farm-gate layer widens the story analytically, but it does not create an artificial claim that raw-milk signals jump directly through the chain."
    )
    fig(
        str(OUTPUTS_ROOT / "hard_cheese" / "novus" / "time_series_observed.png"),
        "Observed retail series (Novus, hard cheese) after unit standardization.",
        "Source: author's calculations based on the current RW4 product-level output for hard cheese in Novus.",
        caption_style="Subtitle",
    )
    para(
        "After unit standardization, the retail series reveals clear repricing events rather than continuous drift. "
        "That is precisely why standardization is not a cosmetic preprocessing step but a condition for economic interpretation."
    )
    fig(
        str(OUTPUTS_ROOT / "milk" / "silpo" / "lag_profile_promo_controlled.png"),
        "Lag profile (Silpo, milk; promo-controlled series) used to guide dynamic specifications",
        "Source: author's calculations based on the current RW4 product-level output for milk in Silpo.",
        caption_style="Subtitle",
    )
    para(
        "The promo-controlled lag profile shows that the strongest relationship between the retail baseline price and upstream movement does not arise contemporaneously but at non-zero lags. "
        "This supports the use of ECM and ARDL specifications in which delayed correction, rather than same-period pass-through, is the relevant benchmark."
    )

    para("Chapter 6. Estimation results", "Heading1", page_break_before=True)
    para(
        "The estimation chapter asks where along the dairy chain price adjustment is fast, where it is buffered, and where the transmission mechanism is reshaped by downstream commercial conduct. "
        "The empirical core remains the domestic chain ProducerUA -> ProZorro -> Retail because it is the clearest sequence through which an upstream cost signal can be traced into procurement and then to the shelf. "
        "Retailer-specific versions, Silpo, Novus, and pooled Silpo+Novus, remain essential because downstream pricing routines are heterogeneous and should not be averaged away before interpretation."
    )
    para(
        f"The model families therefore play different roles. ARDL provides a benchmark distributed-lag relation when a stable long-run link remains plausible; ECM converts that link into an explicit speed-of-adjustment object; NARDL tests whether positive and negative shocks are processed differently; VECM acts as a multivariate robustness check; and the OLS-HAC families operate as reduced-form stress tests rather than as the main identification device. "
        f"Among {_b_int(len(coef))} consolidated coefficient rows, {_b_int(family_counts.get('NARDL', 0))} belong to NARDL, {_b_int(family_counts.get('ARDL', 0))} to ARDL, {_b_int(family_counts.get('VECM', 0))} to VECM, and {_b_int(family_counts.get('ECM', 0))} to ECM. "
        f"Crucially, {_b_int(dynamic_core_rows)} out of {_b_int(total_core_rows)} core findings sit inside the ECM or NARDL families, which is why the thesis treats equilibrium correction, rather than reduced-form contemporaneous response, as its main evidential base."
    )
    para(
        "That hierarchy is substantive, not stylistic. In a vertically coordinated food chain with contracts, inventories, and promotions, the one-period coefficient is often too unstable to stand on its own. "
        "The economically informative object is whether disequilibrium is corrected, how quickly it is corrected, and whether the direction of the underlying shock changes that correction path."
    )
    fig(
        str(OUTPUTS_ROOT / "model_ardl" / "ardl_short_run.png"),
        "Short-run ARDL coefficient dispersion across active links",
        "Source: author's calculations based on the current RW4 ARDL summary output.",
        caption_style="Quote",
    )
    para(
        "The short-run ARDL summary makes the point visually. Coefficients are widely dispersed in sign and magnitude, which is exactly what one would expect when the chain contains contracting frictions, assortment turnover, and retailer smoothing. "
        "For that reason, the thesis does not treat the short-run coefficient as a literal one-step pass-through elasticity unless the broader dynamic specification and the diagnostics support that interpretation."
    )
    para(
        f"In the current consolidated RW4 chain, {_b_pct(ok_share)} of rows finish with status 'ok', {_b_pct(unreliable_share)} remain unreliable, and {_b_int(len(no_fit))} rows are explicitly ruled out by admissibility or overlap constraints. "
        "This chapter therefore follows the same logic as the draft, but it puts far more weight on selective interpretation."
    )
    para(
        "Results are treated as unreliable when residual diagnostics, stability, overlap, or integration admissibility do not support economic interpretation. "
        "That is especially important in the dairy setting because procurement prices, retail prices, and promotional prices are not generated by the same institutional mechanism even when they belong to the same product family."
    )
    fig(
        str(OUTPUTS_ROOT / "model_ecm" / "ecm_ect.png"),
        "Long-run structure and adjustment signals across links",
        "Source: author's calculations based on the current RW4 ECM summary output.",
        caption_style="Quote",
    )
    para(
        f"The core message of the updated run is still the same as in the draft, but now it is better disciplined. In the product-specific producer -> ProZorro block, butter corrects with ECT {_b_num(butter_prod['ect_coef'])} at p-value {_b_num(butter_prod['ect_pvalue'])}, cream with ECT {_b_num(cream_prod['ect_coef'])} at p-value {_b_num(cream_prod['ect_pvalue'])}, and hard cheese with ECT {_b_num(hard_prod['ect_coef'])} at p-value {_b_num(hard_prod['ect_pvalue'])}. "
        "That repeated return toward equilibrium is more informative than any single long-run coefficient taken in isolation."
    )
    para(
        f"In the downstream link, the same logic reappears product by product. Butter in pooled Silpo+Novus corrects with ECM ECT {_b_num(butter_ecm['ect_coef'])}; milk in Silpo corrects with ECM ECT {_b_num(milk_ecm['ect_coef'])} and NARDL ECT {_b_num(milk_nardl['ect_coef'])}; hard cheese in pooled Silpo+Novus corrects with NARDL ECT {_b_num(hard_nardl['ect_coef'])}. "
        "So the present rerun again suggests that vertical coordination is visible most clearly through adjustment speed rather than through one universal pass-through elasticity."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_correlations_lags" / "lag_best_bar.png"),
        "Lag heatmap used to discipline lag selection",
        "Source: author's calculations based on the current RW4 lag-scan output.",
        caption_style="Quote",
    )
    para(
        f"The lag structure is again clearly non-zero. In the product-specific outputs, the best producer -> ProZorro lag is {_b_int(butter_lag_prod['lag'])} for butter, {_b_int(milk_lag_prod['lag'])} for milk, and {_b_int(hard_lag_prod['lag'])} for hard cheese. "
        f"For ProZorro -> Retail, the strongest lags are {_b_int(butter_lag_proc['lag'])} for pooled butter, {_b_int(milk_lag_proc['lag'])} for milk in Silpo, {_b_int(hard_lag_proc['lag'])} for pooled hard cheese, and {_b_int(sour_lag_proc['lag'])} for pooled sour cream. "
        "That timing pattern is exactly what one would expect if repricing is filtered through contracts, inventory, promotions, and retailer routines."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_brand_region" / "brand_hhi.png"),
        "Retail brand structure and concentration",
        "Source: author's calculations based on the current RW4 brand-region output.",
        caption_style="Quote",
    )
    para(
        f"Retail market structure also affects how shocks are absorbed. The brand-transmission table contains {_b_int(len(brand))} rows, but brand labels are missing in {_b_pct(brand_missing_share)} of them and the overall brand core-finding share is only {_b_pct(brand_core_share)}. "
        f"Silpo nevertheless contributes {_b_int(silpo_brand['sum'])} core brand findings out of {_b_int(silpo_brand['count'])} rows, while Novus contributes {_b_int(novus_brand['sum'])} out of {_b_int(novus_brand['count'])}. "
        "That asymmetry matters because concentration and category management are likely sources of downstream market power."
    )
    fig(
        str(OUTPUTS_ROOT / "model_discounts" / "discount_delta_short_run.png"),
        "Discount and promo-control effects in retail aggregation",
        "Source: author's calculations based on the current RW4 discount module.",
        caption_style="Quote",
    )
    para(
        f"The discount module now gives a more nuanced result than the earlier draft. Observed-versus-baseline differences average {_b_num(delta_sr_mean)} in short-run coefficients, {_b_num(delta_lr_mean)} in long-run coefficients, and {_b_num(delta_ect_mean)} in error-correction terms, while pseudo-asymmetry is flagged in {_b_pct(pseudo_asymmetry_share)} of rows. "
        f"The synthesis table answers '{discount_lookup['Do promotions behave like equilibrium correction?'][0]}' to the question of whether promotions behave like equilibrium correction, and '{discount_lookup['Does pseudo-asymmetry weaken after promo control?'][0]}' to whether pseudo-asymmetry weakens after promo control. "
        "The most careful reading is that retail discounting often acts as a shock-absorption mechanism, which is consistent with an everyday-low-price-style smoothing logic at the category level even when item-level promotions remain visible."
    )
    fig(
        str(OUTPUTS_ROOT / "model_nardl" / "nardl_long_run.png"),
        "Asymmetric transmission evidence summary",
        "Source: author's calculations based on the current RW4 NARDL summary output.",
        caption_style="Quote",
    )
    para(
        f"Asymmetry is still not universal. Butter downstream does not reject asymmetry in the pooled retail model, with long-run asymmetry p-value {_b_num(butter_nardl['asymmetry_long_p'])}. Milk in Silpo is also symmetric enough for practical purposes, with long-run asymmetry p-value {_b_num(milk_nardl['asymmetry_long_p'])}. "
        f"Hard cheese is the clearest exception, because the pooled retail NARDL rejects long-run symmetry at p-value {_b_num(hard_nardl['asymmetry_long_p'])}. "
        "This makes a product-specific, rather than system-wide, asymmetry narrative the more reliable conclusion."
    )

    para("6.1 Producers to procurement (processors) transmission", "Heading2")
    para(
        "The first link in the chain remains the cleanest economic object. The econometric question is whether changes in upstream domestic producer prices translate into procurement prices as a stable relation and, more importantly, as a process of equilibrium re-anchoring rather than as a same-period mechanical transfer."
    )
    para(
        "This upstream block should also be read against the new farm-gate evidence. The added FarmGateUA layer broadens the narrative of the thesis by restoring the raw-milk benchmark, but the direct FarmGateUA -> ProducerUA connection stays weak in the current data. "
        "That result increases, rather than reduces, the relevance of the ProducerUA -> ProZorro link: it indicates that processing and procurement are the first stages where the product-specific price signal becomes empirically identifiable."
    )
    para(
        f"Butter gives the clearest example of a procurement layer that is anchored to upstream prices, but not instantaneously. In the current NARDL specification, the short-run coefficient is {_b_num(butter_prod['sr_coef'])}, the long-run coefficient is {_b_num(butter_prod['lr_coef'])}, and the error-correction term is {_b_num(butter_prod['ect_coef'])} with p-value {_b_num(butter_prod['ect_pvalue'])}. "
        f"The best lag for this link sits at {_b_int(butter_lag_prod['lag'])}, and the residual diagnostics remain usable with Ljung-Box {_b_num(butter_prod_diag['ljungbox_p'])} and ARCH {_b_num(butter_prod_diag['arch_p'])}. "
        "The short-run sign should not be over-read as a literal inverse elasticity. In procurement, contract timing and composition can temporarily move against the producer index even when the longer relation remains positive and the corrective force is strong."
    )
    para(
        f"Cream behaves in the same broad direction, but with even faster correction. The current NARDL gives a short-run coefficient of {_b_num(cream_prod['sr_coef'])}, a long-run coefficient of {_b_num(cream_prod['lr_coef'])}, and an error-correction term of {_b_num(cream_prod['ect_coef'])} with p-value {_b_num(cream_prod['ect_pvalue'])}. "
        "Again, the main structural result is the speed of correction. The short-run coefficient is too large to treat as a literal elasticity because procurement composition, fat content, and contract wording vary inside this category."
    )
    para(
        f"Hard cheese remains within the same general pattern, but with slower and more strategic adjustment. The NARDL specification gives a short-run coefficient of {_b_num(hard_prod['sr_coef'])}, a long-run coefficient of {_b_num(hard_prod['lr_coef'])}, and an error-correction term of {_b_num(hard_prod['ect_coef'])} with p-value {_b_num(hard_prod['ect_pvalue'])}. "
        f"The best lag is {_b_int(hard_lag_prod['lag'])}, and the diagnostics are comparatively clean, with Jarque-Bera {_b_num(hard_prod_diag['jb_p'])} closer to conventional tolerable ranges than in butter. "
        "This fits the economics of hard cheese, where inventory and specification heterogeneity can delay the visible procurement response."
    )
    para(
        f"Milk is less clean statistically, but it remains informative. The admissible ARDL gives a short-run coefficient of {_b_num(milk_ardl_up['sr_coef'])} and a long-run coefficient of {_b_num(milk_ardl_up['lr_coef'])}. "
        f"By contrast, the ECM and NARDL versions, though they show fast correction with ECTs {_b_num(milk_ecm_up['ect_coef'])} and {_b_num(milk_nardl_up['ect_coef'])}, are flagged unreliable in the current run. "
        "The safest interpretation is therefore that milk shows short-run linkage under heterogeneous procurement conditions, while its long-run form remains too unstable to summarize with one clean elasticity."
    )
    para(
        f"Sour cream is the most internally coherent ARDL case in this upstream block. The current ARDL gives a short-run coefficient of {_b_num(sour_prod_ardl['sr_coef'])} and a long-run coefficient of {_b_num(sour_prod_ardl['lr_coef'])}. "
        f"The alternative NARDL also produces a strong error-correction term of {_b_num(sour_prod_nardl['ect_coef'])}, but that specification is flagged unreliable. "
        "For this category, the empirically responsible reading is that procurement gradually incorporates upstream pressure rather than resisting it, but the ARDL story is cleaner than the nonlinear one."
    )
    para(
        f"Taken together, the upstream results are still conclusive even though some coefficients remain awkward. Butter, cream, and hard cheese all display economically meaningful equilibrium correction, with ECT values between {_b_num(hard_prod['ect_coef'])} and {_b_num(cream_prod['ect_coef'])}. "
        "That is exactly what one would expect if procurement is an institutional pricing layer that buffers short-run noise but cannot remain detached from upstream market conditions for long."
    )

    para("6.2 Procurement (processors) to retail transmission and retailer heterogeneity", "Heading2")
    para(
        "The second link is harder to interpret because retail price is not a simple cost-plus outcome. It also reflects promotions, assortment changes, pricing strategy, and the retailer's ability to manage the shelf path of a category. "
        "That is why retailer heterogeneity is much more important downstream than upstream."
    )
    para(
        f"Butter in pooled Silpo+Novus is still the clearest example of managed but real downstream linkage. The ARDL estimate gives a short-run coefficient of {_b_num(butter_ardl['sr_coef'])} and a long-run coefficient of {_b_num(butter_ardl['lr_coef'])}. "
        f"The ECM then sharpens the interpretation with short-run coefficient {_b_num(butter_ecm['sr_coef'])}, long-run coefficient {_b_num(butter_ecm['lr_coef'])}, and ECT {_b_num(butter_ecm['ect_coef'])} at p-value {_b_num(butter_ecm['ect_pvalue'])}. "
        f"The NARDL reinforces the correction story with ECT {_b_num(butter_nardl['ect_coef'])}, while asymmetry remains unsupported, with long-run asymmetry p-value {_b_num(butter_nardl['asymmetry_long_p'])}. "
        "The stable conclusion is therefore correction, not a literal long-run markup coefficient."
    )
    para(
        f"Milk in Silpo is the strongest fast-adjustment case in the retail part of the chain. The ECM yields a short-run coefficient of {_b_num(milk_ecm['sr_coef'])}, a long-run coefficient of {_b_num(milk_ecm['lr_coef'])}, and an ECT of {_b_num(milk_ecm['ect_coef'])} with p-value {_b_num(milk_ecm['ect_pvalue'])}. "
        f"The NARDL gives a similar picture: short-run {_b_num(milk_nardl['sr_coef'])}, long-run {_b_num(milk_nardl['lr_coef'])}, and ECT {_b_num(milk_nardl['ect_coef'])} with p-value {_b_num(milk_nardl['ect_pvalue'])}. "
        f"Residual diagnostics are also strong, with Ljung-Box {_b_num(milk_ecm_diag['ljungbox_p'])} and ARCH {_b_num(milk_ecm_diag['arch_p'])}. "
        "Economically, that fits milk very well: it is a high-turnover, frequently observed category with limited room to hide persistent disequilibrium."
    )
    para(
        f"Hard cheese is the opposite and remains the clearest case where category management dominates the long-run coefficient. In pooled Silpo+Novus, ARDL gives short-run {_b_num(hard_ardl['sr_coef'])} and long-run {_b_num(hard_ardl['lr_coef'])}, but the bounds evidence in that specification is weak. "
        f"The NARDL gives short-run {_b_num(hard_nardl['sr_coef'])}, long-run {_b_num(hard_nardl['lr_coef'])}, and ECT {_b_num(hard_nardl['ect_coef'])} with p-value {_b_num(hard_nardl['ect_pvalue'])}. "
        f"This is also the clearest downstream asymmetry case, with long-run asymmetry p-value {_b_num(hard_nardl['asymmetry_long_p'])}. "
        "The interpretation is not that procurement shocks invert mechanically into shelf prices. It is that positive and negative procurement shocks are not treated symmetrically once hard cheese is aggregated into a broad retail category with strategic substitution and brand management."
    )
    para(
        f"Sour cream widens the downstream story further. In pooled Silpo+Novus, the ARDL gives short-run {_b_num(sour_retail_ardl['sr_coef'])} and long-run {_b_num(sour_retail_ardl['lr_coef'])}, while the NARDL gives short-run {_b_num(sour_retail_nardl['sr_coef'])}, long-run {_b_num(sour_retail_nardl['lr_coef'])}, and ECT {_b_num(sour_retail_nardl['ect_coef'])} with p-value {_b_num(sour_retail_nardl['ect_pvalue'])}. "
        "This category therefore sits between the milk and hard-cheese extremes: the corrective mechanism is clear, but the category is still more strategically managed than milk."
    )
    para(
        f"The current RW4 rerun also widens the old downstream story by showing non-trivial reverse-flow evidence. Retail -> ProZorro now retains {_b_int(coverage_rp['core_finding_rows'])} core findings out of {_b_int(coverage_rp['rows_total'])} rows, or roughly {_b_pct(reverse_core_share)}. "
        f"At the higher comparison-panel level, Retail -> ProducerUA in the pooled Silpo-Novus specification gives short-run {_b_num(retail_to_producer['sr_coef'])}, long-run {_b_num(retail_to_producer['lr_coef'])}, and ECT {_b_num(retail_to_producer['ect_coef'])} with p-value {_b_num(retail_to_producer['ect_pvalue'])}. "
        "This does not prove literal reverse causality in every period, but it does show that downstream pricing contains information that travels back through the chain. That is a strong sign of vertical coordination and retailer-mediated market power."
    )
    fig(
        str(OUTPUTS_ROOT / "model_intersection_bidirectional" / "bidirectional_coef.png"),
        "Bidirectional coefficient evidence across upstream and downstream intersection panels",
        "Source: author's calculations based on the current RW4 bidirectional-intersection output.",
        caption_style="Quote",
    )
    para(
        "The bidirectional summary is especially valuable because it makes the coordination result harder to dismiss as a product-specific anomaly. "
        "Forward transmission remains the dominant interpretation, yet the non-zero reverse coefficients show that downstream price setting is informative about the eventual path of the chain. "
        "In market terms, retailers appear not only as receivers of procurement shocks, but as strategic coordinators whose timing and category governance feed back into the broader pricing environment."
    )
    para(
        f"Brand-level evidence pushes in the same direction, but asymmetrically across retailers. The Silpo brand block carries {_b_int(silpo_brand['sum'])} core findings, while Novus carries {_b_int(novus_brand['sum'])}. "
        "So downstream power is not just a retail-stage average phenomenon; in parts of the chain it is also a brand-and-category phenomenon."
    )

    para("6.3 Model visualisations", "Heading2")
    para(
        "The time series, lag profiles, adjustment paths, and dynamic multipliers remain essential because they show whether the numerical estimates correspond to a plausible market process. "
        "In the updated rerun, the same visual logic as in the draft still holds, but it is now backed by the current RW4 outputs."
    )

    fig(
        str(OUTPUTS_ROOT / "butter" / "silpo_novus" / "time_series_observed.png"),
        "Butter, Silpo+Novus, observed category series",
        "Source: author's calculations based on the current butter Silpo+Novus and ProZorro outputs.",
        caption_style="Quote",
    )
    para(
        "The observed butter series clarifies that procurement and retail do not move one-for-one within the same day. The co-movement is visible, but it is filtered through stepwise repricing and periods of shelf-price smoothing. "
        "That is why the correction coefficients are more informative than the raw long-run ARDL magnitude."
    )
    fig(
        str(OUTPUTS_ROOT / "butter" / "silpo_novus" / "lag_profile_observed.png"),
        "Butter, Silpo+Novus, lag profile",
        "Source: author's calculations based on the current butter Silpo+Novus lag-profile output.",
        caption_style="Quote",
    )
    para(
        f"The lag profile turns delay into an observable market object. For butter, the procurement-to-retail peak sits at lag {_b_int(butter_lag_proc['lag'])}, and the producer-to-procurement peak sits at lag {_b_int(butter_lag_prod['lag'])}. "
        "That pattern is consistent with scheduled rather than instantaneous repricing."
    )
    fig(
        str(OUTPUTS_ROOT / "butter" / "silpo_novus" / "ecm_adjustment_observed.png"),
        "Silpo+Novus butter prices ECM adjustment",
        "Source: author's calculations based on the current butter Silpo+Novus ECM output.",
        caption_style="Quote",
    )
    para(
        f"The estimated ECT for pooled butter equals {_b_num(butter_ecm['ect_coef'])}. A steeper negative adjustment path means faster removal of disequilibrium between procurement and retail. "
        "Economically, that corresponds to managed correction rather than to a constant markup."
    )
    fig(
        str(OUTPUTS_ROOT / "butter" / "silpo_novus" / "nardl_multipliers_observed.png"),
        "Silpo+Novus price of butter, NARDL multipliers",
        "Source: author's calculations based on the current butter Silpo+Novus NARDL output.",
        caption_style="Quote",
    )
    para(
        "The multiplier paths show how the system absorbs positive and negative shocks over time. In butter, the current paths do not remain persistently separated in the way a strong rockets-and-feathers story would require. "
        "That is why the updated narrative treats butter as dynamically linked but not asymmetrically governed."
    )

    fig(
        str(OUTPUTS_ROOT / "milk" / "silpo" / "time_series_observed.png"),
        "Milk, Silpo, observed category series",
        "Source: author's calculations based on the current milk Silpo and ProZorro outputs.",
        caption_style="Quote",
    )
    para(
        "Milk in Silpo remains the cleanest high-turnover downstream case. The time series shows a category that reprices frequently enough for procurement pressure to become visible relatively quickly."
    )
    fig(
        str(OUTPUTS_ROOT / "milk" / "silpo" / "lag_profile_observed.png"),
        "Milk, Silpo, lag profile",
        "Source: author's calculations based on the current milk Silpo lag-profile output.",
        caption_style="Quote",
    )
    para(
        f"The lag profile places the strongest procurement-to-retail link at lag {_b_int(milk_lag_proc['lag'])}, with correlation {_b_num(milk_lag_proc['corr'])}. "
        "This is exactly the kind of visual evidence that makes the fast ECM and NARDL correction terms economically believable."
    )
    fig(
        str(OUTPUTS_ROOT / "milk" / "silpo" / "ecm_adjustment_observed.png"),
        "Milk, Silpo, ECM adjustment",
        "Source: author's calculations based on the current milk Silpo ECM output.",
        caption_style="Quote",
    )
    para(
        f"The estimated ECT in the ECM equals {_b_num(milk_ecm['ect_coef'])}, which makes milk the clearest case of rapid downstream correction in the current rerun. "
        "From the standpoint of market behavior, this looks like a category in which disequilibria are removed quickly rather than stored inside assortment shifts."
    )

    fig(
        str(OUTPUTS_ROOT / "hard_cheese" / "silpo_novus" / "time_series_observed.png"),
        "Hard cheese, Silpo+Novus, observed category series",
        "Source: author's calculations based on the current hard-cheese Silpo+Novus and ProZorro outputs.",
        caption_style="Quote",
    )
    para(
        "Hard cheese still moves through stepwise episodes with visibly greater category-management influence than milk. "
        "That visual pattern is consistent with the extreme and asymmetric long-run coefficients in the pooled downstream models."
    )
    fig(
        str(OUTPUTS_ROOT / "hard_cheese" / "silpo_novus" / "lag_profile_observed.png"),
        "Hard cheese, Silpo+Novus, lag profile",
        "Source: author's calculations based on the current hard-cheese Silpo+Novus lag-profile output.",
        caption_style="Quote",
    )
    para(
        f"The lag profile shows the strongest procurement-to-retail relationship at lag {_b_int(hard_lag_proc['lag'])}, while the producer-to-procurement peak sits at lag {_b_int(hard_lag_prod['lag'])}. "
        "This delayed timing is compatible with contract resets, retailer repricing, and substitution across types and brands."
    )
    fig(
        str(OUTPUTS_ROOT / "hard_cheese" / "silpo_novus" / "nardl_multipliers_observed.png"),
        "Hard cheese, Silpo+Novus, NARDL multipliers",
        "Source: author's calculations based on the current hard-cheese Silpo+Novus NARDL output.",
        caption_style="Quote",
    )
    para(
        "The hard-cheese multipliers remain the visual counterpart of the asymmetry finding. The positive and negative paths do not settle into the same plateau, which is exactly what one would expect when category management treats cost increases and decreases differently."
    )

    para("6.3.1 Added RW4 extension figures", "Heading3")
    para(
        "The current rerun adds a set of figures that were not central in the earlier draft but now widen the story materially. These additions concern the farm-gate data layer, forecast-supported coherence, synthetic consumer linkage, and retail promo intensity."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_farmgateua_filled" / "sheet_farmgateua_filled_region_trends.png"),
        "Farm-gate raw-milk benchmark and reconstructed regional trends",
        "Source: author's calculations based on the current RW4 filled farm-gate reconstruction.",
        caption_style="Quote",
    )
    para(
        "This figure is important not because it proves strong farm-gate transmission by itself, but because it shows that the added farm-gate layer is smooth, positive, and regionally structured enough to function as a benchmark-consistent upstream anchor. "
        "The later weak FarmGateUA -> ProducerUA findings should therefore be interpreted as an economic limitation of the proxy, not as a graph-construction mistake."
    )
    fig(
        str(OUTPUTS_ROOT / "model_forecast_knn" / "forecast_producer_consumer.png"),
        "Forecasted producer and consumer trajectories",
        "Source: author's calculations based on the current RW4 forecast module.",
        caption_style="Quote",
    )
    para(
        f"The forecast block is one of the cleanest supportive layers in the entire rerun. Producer holdout RMSE ranges from {_b_num(producer_rmse.min())} to {_b_num(producer_rmse.max())}, consumer holdout RMSE ranges from {_b_num(consumer_rmse.min())} to {_b_num(consumer_rmse.max())}, and training R-squared remains between {_b_pct(forecast_r2.min())} and {_b_pct(forecast_r2.max())}. "
        "This does not make the forecasts causal evidence, but it does confirm that the smoothed trajectories used for interpretation are not arbitrary."
    )
    fig(
        str(OUTPUTS_ROOT / "model_forecast_knn" / "consumer_link_coef.png"),
        "Synthetic retail link to consumer prices",
        "Source: author's calculations based on the current RW4 synthetic-consumer link output.",
        caption_style="Quote",
    )
    para(
        f"The synthetic-retail extension is selective rather than universal. The clearest significant case is {synth_best['product']}, where the synthetic-to-consumer coefficient equals {_b_num(synth_best['coef_synth_to_consumer'])} with p-value {_b_num(synth_best['p_synth_to_consumer'])}. "
        "That makes the extension useful for widening the market picture, but it should not displace the main chain analysis."
    )
    fig(
        str(OUTPUTS_ROOT / "graphs_brand_region" / "brand_promo_intensity.png"),
        "Retail promo intensity and price-smoothing environment",
        "Source: author's calculations based on the current RW4 brand-region output.",
        caption_style="Quote",
    )
    para(
        "Promo intensity is the visual counterpart of the discount story. It suggests that markdowns are part of the downstream adjustment environment even when category-level transmission remains dominated by baseline shelf management. "
        "That is why the discount story in this thesis is best framed as price smoothing and margin management, not as a purely high-low pricing regime."
    )

    para("6.4 Farm-gate transmission and the extreme-points chain", "Heading2")
    para(
        "The direct farm-gate question deserves a separate discussion because it is conceptually the longest transmission route in the thesis: it asks whether the raw-milk benchmark at the upstream extreme can be traced all the way to procurement and retail at the downstream extreme. "
        "That route is economically important, but it is also the most difficult to estimate because it compresses several institutional transformations into one relationship."
    )
    para(
        f"The current RW4 outputs confirm that the farm-gate effect is estimated rather than omitted. In the required-link validation, FarmGateUA -> ProducerUA contributes {_b_int(coverage_fp['rows_total'])} rows with {_b_int(coverage_fp['core_finding_rows'])} core findings, FarmGateUA -> ProZorro contributes {_b_int(_coverage_row(coverage, 'FarmGateUA', 'ProZorro')['rows_total'])} rows with {_b_int(_coverage_row(coverage, 'FarmGateUA', 'ProZorro')['core_finding_rows'])} core findings, and FarmGateUA -> Retail contributes {_b_int(_coverage_row(coverage, 'FarmGateUA', 'Retail')['rows_total'])} rows with {_b_int(_coverage_row(coverage, 'FarmGateUA', 'Retail')['core_finding_rows'])} core findings. "
        f"In share terms, the raw-milk block performs best for {raw_stage_summary.iloc[0]['stage_to']} at {_b_pct(raw_stage_summary.iloc[0]['mean'])}, then {raw_stage_summary.iloc[1]['stage_to']} at {_b_pct(raw_stage_summary.iloc[1]['mean'])}, while the FarmGateUA -> ProducerUA link remains weakest."
    )
    para(
        "This ranking is economically plausible. The national farm-gate benchmark is broad, smoothed, and only indirectly connected to processed categories. "
        "It therefore struggles most when asked to explain the producer layer product by product, yet becomes more informative when aggregated procurement or retail environments are allowed to absorb some of that missing micro-heterogeneity."
    )
    fig(
        str(OUTPUTS_ROOT / "primary_chain_summary" / "farmgate_direct_heatmap.png"),
        "Direct farm-gate core-finding share by downstream stage and retail panel",
        "Source: author's calculations based on the current RW4 primary-chain consolidated output.",
        caption_style="Quote",
    )
    para(
        f"The new direct-summary heatmap makes one empirical point very clear: the strongest farm-gate block is no longer the direct retail endpoint, but the farm-gate-to-procurement route recovered under pairwise overlap. In the pairwise NARDL summaries, FarmGateUA -> ProZorro reaches a core-finding share of {_b_pct(fg_proc_pairwise['core_finding_share'])} with reconstruction robustness of {_b_pct(fg_proc_pairwise['robust_across_reconstruction_share'])} and interpolation robustness of {_b_pct(fg_proc_pairwise['robust_linear_vs_pchip_share'])}. "
        "That is economically sensible because procurement is the first institutional layer at which upstream raw-milk pressure can be translated into standardized transaction prices without yet being reshaped by full retail category management."
    )
    fig(
        str(OUTPUTS_ROOT / "sheet_farmgateua_filled" / "sheet_farmgateua_filled_region_trends.png"),
        "Farm-gate benchmark and reconstructed regional trends used in the extreme-points analysis",
        "Source: author's calculations based on the current RW4 filled FarmGateUA reconstruction.",
        caption_style="Quote",
    )
    para(
        "The farm-gate benchmark figure clarifies why the direct transmission exercise is analytically difficult. The series is smooth and internally coherent, yet it is far more aggregated than the downstream product categories. "
        "The estimation problem is therefore not data corruption but data mismatch in economic granularity: one upstream raw-milk benchmark must speak to product-specific processed-dairy and retail baskets."
    )
    para(
        f"The retail endpoint becomes more informative once the unified downstream layer is split into an anchored and a strict retailer-core version. For the anchored chain, the pairwise FarmGateUA -> Retail NARDL block reaches a core-finding share of {_b_pct(fg_retail_anchor_pairwise['core_finding_share'])} with median overlap of {_b_int(fg_retail_anchor_pairwise['median_n_obs'])} observations. "
        f"For the strict retailer-core chain, the corresponding pairwise share rises to {_b_pct(fg_retail_core_pairwise['core_finding_share'])}, but the median overlap contracts sharply to {_b_int(fg_retail_core_pairwise['median_n_obs'])} observations. "
        "This is the central identification tradeoff of the new design: the anchored index lengthens the downstream horizon, while the core index is shorter but more retailer-grounded."
    )
    para(
        f"The diagnostics of the unified retail layer explain why neither version should be over-interpreted mechanically. Consumer support is non-zero only for {_b_int(consumer_supported_products)} product groups, the anchored version has a median retailer-overlap share of {_b_pct(anchor_overlap_median)}, and the retailer-core version lifts that median to {_b_pct(core_overlap_median)}. "
        f"At the same time, the median ConsumerUA weight in the anchored construction is {_b_num(anchor_consumer_weight_median)}. "
        "So the anchored index is not a disguised consumer-price series, but it is also not a pure retailer-only panel. It should be read as a consumer-facing downstream environment rather than as a literal shelf-only index."
    )
    para(
        f"The strongest direct farm-gate-to-retail single case still appears in a selected product panel rather than in a universal average specification: {raw_retail_best['product']} for {raw_retail_best['retailer_panel']} under the {raw_retail_best['price_variant']} price variant, {raw_retail_best['reconstruction_variant']} reconstruction, and {raw_retail_best['farm_gate_source']} farm-gate source. "
        f"In that case, the NARDL estimates short-run {_b_num(raw_retail_best['sr_coef'])}, long-run {_b_num(raw_retail_best['lr_coef'])}, and ECT {_b_num(raw_retail_best['ect_coef'])} with p-value {_b_num(raw_retail_best['ect_pvalue'])}. "
        "That profile remains useful as evidence that direct extreme-points transmission can be recovered, but the consolidated summaries show that it is the exception rather than the default."
    )
    fig(
        str(OUTPUTS_ROOT / "primary_chain_summary" / "unified_retail_comparison.png"),
        "Comparison of retail-panel core-finding shares after adding unified retail chains",
        "Source: author's calculations based on the current RW4 unified-retail comparison output.",
        caption_style="Quote",
    )
    para(
        f"The reverse-flow evidence is more persuasive than the direct retail endpoint, and it becomes stronger when the strict retailer-core chain is used. In the pairwise NARDL summaries, Retail_combined -> FarmGateUA reaches {_b_pct(fg_reverse_anchor_pairwise['core_finding_share'])} core support, whereas Retail_combined_core -> FarmGateUA reaches {_b_pct(fg_reverse_core_pairwise['core_finding_share'])}. "
        "That ranking is analytically valuable. It suggests that the national consumer anchor helps lengthen the direct downstream series, but the retailer-only core carries cleaner information when the question is whether downstream pricing behavior feeds back toward upstream conditions."
    )
    fig(
        str(OUTPUTS_ROOT / "primary_chain_summary" / "intersection_stability.png"),
        "Intersection-rule stability after adding pairwise-overlap farm-gate panels",
        "Source: author's calculations based on the current RW4 intersection-stability summary.",
        caption_style="Quote",
    )
    para(
        "The intersection-stability graph reinforces the same message. Once the chain is re-specified through pairwise overlaps rather than only the strict common chain support, direct farm-gate evidence becomes broader and the procurement route strengthens materially. "
        "At the same time, the direct farm-gate-to-retail block remains selective even after the redesign. What the new RW4 results therefore justify is a more precise statement, not a stronger generic claim: the extreme-points effect is real, most visible at the farm-gate-to-procurement margin, and only partially recoverable at the direct retail endpoint."
    )
    para(
        f"What keeps the farm-gate extreme-points story from being a headline result is reliability across variants. Interpolation robustness still averages only {_b_pct(robust_linear)}, reconstruction robustness remains weaker at {_b_pct(robust_farmgate)}, and the direct FarmGateUA -> ProducerUA block continues to contribute only {_b_int(coverage_fp['core_finding_rows'])} core findings. "
        "In other words, the effect is not absent; it is variant-sensitive. The present redesign improves the diagnostics and sharpens the market picture, but it also confirms that a credible farm-gate thesis chapter must distinguish carefully between upstream-to-procurement evidence, anchored downstream evidence, and strict retailer-core evidence."
    )

    para("6.5 Conclusion and economic implications", "Heading2")
    para(
        "The central empirical conclusion is that the Ukrainian dairy chain is vertically coordinated, but that coordination is neither frictionless nor uniform. "
        "The estimates do not support a single pass-through coefficient that could summarize the whole market. Instead, they reveal a layered structure in which procurement repeatedly re-anchors to upstream producer conditions, while retail categories translate those upstream pressures through chain-specific routines, promotion strategies, and assortment management."
    )
    para(
        "From an econometric standpoint, the most persuasive evidence is the repeated presence of negative and statistically meaningful error-correction terms, not the raw size of the long-run coefficients taken in isolation. "
        "Butter, cream, and hard cheese show especially clear upstream correction in the ProducerUA -> ProZorro block, while milk and selected pooled retail panels show fast downstream re-anchoring in the ProZorro -> Retail block. "
        "That pattern is economically coherent: procurement behaves as an institutional buffer, whereas retail behaves as a managed adjustment layer."
    )
    para(
        "The product comparison sharpens the market picture. Milk is the closest case to rapid, high-frequency downstream correction, which fits its turnover, observability, and limited room for prolonged shelf disequilibrium. "
        "Butter also transmits upstream pressure, yet its economically meaningful signal lies in the pace of correction rather than in a stable long-run markup. Hard cheese is different again: the asymmetric pooled-retail result points to strategic category management, product substitution, and selective treatment of cost increases and decreases. "
        "Taken together, these contrasts indicate that vertical coordination in dairy is product-specific and mediated by retail governance rather than mechanically imposed by costs alone."
    )
    para(
        f"The new RW4 extensions add an important second layer to that conclusion. The FarmGateUA benchmark broadens the upstream narrative, but the weak direct FarmGateUA -> ProducerUA core-finding share of {_b_pct(raw_best['mean'])} confirms that a national raw-milk proxy is too coarse to serve as a literal product-level pass-through driver in the current data environment. "
        f"At the same time, the reverse-flow block is too strong to ignore: Retail -> ProZorro retains {_b_pct(reverse_core_share)} core support overall, while the strict retailer-core pairwise Retail -> FarmGateUA NARDL block reaches {_b_pct(fg_reverse_core_pairwise['core_finding_share'])} against {_b_pct(fg_reverse_anchor_pairwise['core_finding_share'])} in the anchored version. "
        f"The pooled Retail -> ProducerUA evidence also remains meaningful, with an ECT of {_b_num(retail_to_producer['ect_coef'])}. "
        "The most defensible interpretation is not simple reverse causality, but retailer-mediated coordination: downstream pricing decisions contain information that is reflected back into the broader chain, and that information becomes cleaner once the consumer anchor is separated from the retailer-core panel."
    )
    para(
        "The discount evidence fits this interpretation closely. Promotions do not look like a random disturbance layered on top of the true price. They behave more like a tactical adjustment instrument that absorbs part of the short-run pressure while preserving a managed baseline path. "
        f"Observed-versus-baseline differences average {_b_num(delta_sr_mean)} in short-run coefficients, {_b_num(delta_lr_mean)} in long-run coefficients, and {_b_num(delta_ect_mean)} in adjustment terms, while pseudo-asymmetry is flagged in {_b_pct(pseudo_asymmetry_share)} of rows. "
        "That combination is more consistent with an everyday-low-price smoothing environment at the category level than with a pure high-low pricing regime."
    )
    para(
        "These findings are economically valuable for several reasons. For processors and procurement managers, they imply that disequilibrium usually does not persist indefinitely, but the timing of correction differs sharply by product and institutional layer. "
        "For retailers, the results quantify how category management can soften or reshape incoming procurement shocks without fully severing the link to upstream conditions. For competition and sector analysts, the combination of concentration metrics, selective asymmetry, and reverse-flow evidence suggests that downstream market power is best understood as control over the timing and visibility of transmission rather than as a static markup wedge."
    )
    para(
        "The statistically awkward or economically non-intuitive coefficients are also informative once read correctly. Large negative long-run estimates, sign reversals in short-run ARDLs, and unreliable nonlinear specifications tend to cluster where categories are broad, overlap is thin, or product definitions absorb multiple packaging and brand regimes. "
        "The remedy is therefore not to smooth the coefficients away, but to tighten the data-generating design: narrower product taxonomies, retailer-specific brand cleaning before pooling, and weekly promo-state panels that can converge without overstating item-level markdown noise."
    )
    para(
        "A clear path for further improvement follows from those bottlenecks. The next version of the analysis should prioritize a more product-resolved farm-gate or processor contract layer, deeper retailer-brand normalization, and a promotion specification that pools enough observations to identify state-dependent adjustment cleanly. "
        "At the same time, the current RW4 results are already sufficient to support a conclusive thesis argument. Vertical coordination in the dairy chain is real; procurement acts as an institutional transmission buffer rather than as a frictionless conduit; and downstream market power appears primarily through category management, discount smoothing, and selective asymmetry. "
        "That is a stronger and more economically meaningful conclusion than any single pass-through coefficient could provide."
    )

    return blocks


def _write_docx_from_template(template_path: Path, output_path: Path, blocks: list[Block]) -> None:
    with zipfile.ZipFile(template_path) as zin:
        document_root = ET.fromstring(zin.read("word/document.xml"))
        rels_root = ET.fromstring(zin.read("word/_rels/document.xml.rels"))
        content_root = ET.fromstring(zin.read("[Content_Types].xml"))

        body = document_root.find(_w("body"))
        if body is None:
            raise RuntimeError("Template document body not found.")
        sect_pr = copy.deepcopy(body.find(_w("sectPr")))
        if sect_pr is None:
            raise RuntimeError("Template section properties not found.")

        for child in list(body):
            body.remove(child)

        _ensure_png_content_type(content_root)

        media_entries: list[tuple[str, bytes]] = []
        image_counter = 0
        for block in blocks:
            if isinstance(block, ParagraphBlock):
                body.append(_make_paragraph(block.text, style=block.style, page_break_before=block.page_break_before))
                continue
            if isinstance(block, TableBlock):
                body.append(_make_paragraph("", style="BodyText"))
                body.append(_make_paragraph(block.caption, style=block.caption_style))
                body.append(_make_table(block.headers, block.rows, style_id=block.style_id))
                body.append(_make_paragraph(block.source, style="source"))
                body.append(_make_paragraph("", style="BodyText"))
                continue

            image_counter += 1
            rel_id = f"rId{R_ID_BASE + image_counter}"
            docpr_id = DOC_PR_ID_BASE + image_counter
            media_name = f"generated_data_estimation_{image_counter:03d}{block.path.suffix.lower()}"
            target = f"media/{media_name}"

            if not block.path.exists():
                raise FileNotFoundError(f"Figure not found: {block.path}")

            body.append(_make_image_paragraph(block.path, rel_id=rel_id, docpr_id=docpr_id, width_in=block.width_in))
            body.append(_make_paragraph(block.caption, style=block.caption_style))
            body.append(_make_paragraph(block.source, style="source"))

            _add_relationship(rels_root, rel_id, target)
            media_entries.append((f"word/{target}", block.path.read_bytes()))

        body.append(sect_pr)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                if info.filename == "word/document.xml":
                    data = ET.tostring(document_root, encoding="utf-8", xml_declaration=True)
                elif info.filename == "word/_rels/document.xml.rels":
                    data = ET.tostring(rels_root, encoding="utf-8", xml_declaration=True)
                elif info.filename == "[Content_Types].xml":
                    data = ET.tostring(content_root, encoding="utf-8", xml_declaration=True)
                else:
                    data = zin.read(info.filename)
                zout.writestr(info, data)

            for target, data in media_entries:
                zout.writestr(target, data)


def generate_data_estimation_updated(docx_path: Path | None = None) -> Path:
    thesis_root = _find_thesis_root()
    template_path = thesis_root / "Charniuk_Maksym_MScThesis_Draft_correctedformat.docx"
    if not template_path.exists():
        raise FileNotFoundError(f"Template DOCX not found: {template_path}")

    output_path = docx_path or (thesis_root / "data_estiamtion_updated.docx")
    blocks = _build_blocks()
    _write_docx_from_template(template_path, output_path, blocks)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the updated Data and Estimation Results thesis chapter DOCX.")
    parser.add_argument("--output", type=Path, help="Optional explicit DOCX output path.")
    args = parser.parse_args()

    output_path = generate_data_estimation_updated(docx_path=args.output)
    print(f"Updated data/estimation DOCX generated: {output_path}")


if __name__ == "__main__":
    main()
