#!/usr/bin/env python3
from __future__ import annotations

import argparse

from run_all_rw3 import main as run_all_main
from total_run_builder import build_total_run


def main() -> None:
    parser = argparse.ArgumentParser(description="Run all RW3 modules and build Total Run outputs.")
    parser.add_argument(
        "--skip-run-all",
        action="store_true",
        help="Skip module execution and build Total Run from existing outputs.",
    )
    args = parser.parse_args()

    if not args.skip_run_all:
        run_all_main()
    build_total_run()


if __name__ == "__main__":
    main()
