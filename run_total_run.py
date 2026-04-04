#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from run_all_rw4 import main as run_all_main
from total_run_builder import build_total_run
from generate_rw4_interpretation_report import generate_report as generate_interpretation_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run full RW4 modular pipeline and build one combined Total Run output "
            "(xlsx + pdf + md) with all module tables/graphs."
        )
    )
    parser.add_argument(
        "--skip-run-all",
        action="store_true",
        help="Do not execute modules; only rebuild Total Run from existing outputs.",
    )
    parser.add_argument(
        "--rebuild-total-after-run-all",
        action="store_true",
        help="Run Total Run builder once more after run_all (normally run_all already calls it).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parent
    outputs = root / "outputs"
    interpretation_md: Path | None = None
    interpretation_docx: Path | None = None

    if args.skip_run_all:
        print("Mode: skip module execution; rebuilding Total Run from existing outputs.")
        total_dir = build_total_run(outputs_root=outputs)
    else:
        print("Mode: full run_all_rw4 execution + Total Run.")
        run_all_main()
        if args.rebuild_total_after_run_all:
            print("Rebuilding Total Run after run_all as requested.")
            total_dir = build_total_run(outputs_root=outputs)
        else:
            total_dir = outputs / "total_run"

    interpretation_md, interpretation_docx = generate_interpretation_report()

    print("\nRun complete.")
    print(f"Total Run directory: {total_dir}")
    print(f"Total Run xlsx: {total_dir / 'Total_Run.xlsx'}")
    print(f"Total Run pdf: {total_dir / 'Total_Run.pdf'}")
    print(f"Total Run md: {total_dir / 'Total_Run.md'}")
    print(f"Interpretation report md: {interpretation_md}")
    print(f"Interpretation report docx: {interpretation_docx}")


if __name__ == "__main__":
    main()
