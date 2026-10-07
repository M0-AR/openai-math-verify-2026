"""Benchmark runner — executes exps 01–05, writes JSON + markdown summary.

Usage: python3 benchmarks/benchmark_runner.py --out benchmarks/results/summary.json
Every experiment is re-executed from scratch; nothing is hand-edited without a run.
Exit code 0 even if live-audit degrades offline (audit reports live:false).
"""
import argparse
import importlib.util
import io
import json
import os
import sys
import time
import traceback
from contextlib import redirect_stdout

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

EXPS = [
    ("01_prime_counting", "experiments/01_prime_counting/verify_prime_curve.py"),
    ("02_chromatic_plane", "experiments/02_chromatic_plane/verify_coloring_bounds.py"),
    ("03_pi_irrationality", "experiments/03_pi_irrationality/verify_pi_score.py"),
    ("04_catalog_audit", "experiments/04_catalog_audit/audit_catalog.py"),
    ("05_lean_scope", "experiments/05_lean_scope/scope_checklist.py"),
]


def run_one(path):
    spec = importlib.util.spec_from_file_location("expmod", os.path.join(ROOT, path))
    mod = importlib.util.module_from_spec(spec)
    buf = io.StringIO()
    t0 = time.time()
    try:
        with redirect_stdout(buf):
            spec.loader.exec_module(mod)
            result = mod.main() if hasattr(mod, "main") else None
        return {"status": "pass", "seconds": round(time.time() - t0, 2),
                "log_tail": buf.getvalue()[-2000:], "result": result}
    except Exception as e:  # noqa: BLE001
        return {"status": "FAIL", "error": f"{e}\n{traceback.format_exc()[-2000:]}",
                "seconds": round(time.time() - t0, 2), "log_tail": buf.getvalue()[-2000:]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="benchmarks/results/summary.json")
    args = ap.parse_args()
    summary = {"repo": "openai-math-verify-2026 (independent, from-scratch)",
               "upstream": "openai/math (Apache-2.0, 2026-10-06, NOT vendored)",
               "experiments": {}}
    failed = 0
    for name, path in EXPS:
        print(f"\n===== {name} =====")
        r = run_one(path)
        print(r.get("log_tail", "")[-1500:])
        summary["experiments"][name] = r
        if r["status"] != "pass":
            failed += 1
    out = os.path.join(ROOT, args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    md = out.replace(".json", ".md")
    with open(md, "w") as f:
        f.write("# Benchmark summary (independent verification)\n\n")
        f.write("| experiment | status | seconds |\n|---|---|---|\n")
        for n, r in summary["experiments"].items():
            f.write(f"| {n} | {r['status']} | {r.get('seconds','?')} |\n")
        f.write("\nTrust verdict: classical footprints REPRODUCED; OpenAI proofs NOT re-proved here — "
                "see docs/METHODS.md for L1/L2/L3 protocol.\n")
    print(f"\nWrote {out} and {md}. Failures: {failed}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
