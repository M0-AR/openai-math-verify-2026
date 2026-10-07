# Data — all public, all regenerated at runtime

- No vendored data. Experiments compute locally (sieve, coloring exhaustion,
  mpmath π) or query live public endpoints at runtime:
  - `raw.githubusercontent.com/openai/math/main/{CONTENTS,README}.md`
  - `.../lean/formalization.yaml`
- `benchmarks/results/` holds machine receipts (`summary.json/md`).
- To share: `docker compose up` → results appear in `benchmarks/results/`.
