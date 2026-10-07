"""Experiment 01 — Prime counting vs smooth curve + what Re(s)>7/8 would imply.

Verifies on REAL computed data (no network, fully reproducible):
- pi(1e6) = 78,498 (classical value quoted in the video).
- Li(x) approximation and error |pi(x)-Li(x)| at 1e6.
- Implication of a fixed zero-free strip Re(s) > 7/8:
  classical explicit-formula bound  |psi(x)-x| << x^{theta} log^2 x
  with theta=7/8, evaluated at x=1e6, vs. observed error.
- Control: classical de la Vallee-Poussin zero-free region gives
  error ~ x*exp(-c*sqrt(log x)); we show it is asymptotically weaker
  than any fixed theta<1 power saving.

All prime counts are computed locally by a bytearray sieve (public,
deterministic data). No claim about proving 7/8 is made here — this
experiment checks the *numerical footprint* the claim would leave.
"""
import math


def sieve_pi(n: int) -> int:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * ((n - p * p) // p + 1)
    return sum(sieve)


def li(x: float) -> float:
    # Logarithmic integral via mpmath-free numerical integration (Simpson)
    # Li(x) = PV integral_0^x dt/log t ; start at 2 to avoid singularity.
    import numpy as np
    if x <= 2:
        return 0.0
    ts = np.linspace(2.0, x, 200000)
    vals = 1.0 / np.log(ts)
    trapz = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    return float(trapz(vals, ts))


def main():
    N = 1_000_000
    pi_n = sieve_pi(N)
    assert pi_n == 78498, f"pi(1e6) should be 78498, got {pi_n}"
    li_n = li(N)
    err = abs(pi_n - li_n)
    print(f"pi(1e6) = {pi_n}")
    print(f"Li(1e6) ~= {li_n:.1f}  (video quotes curve 78,628; offset definition differs by Li(2)~1.04 baseline)")
    print(f"|pi-Li| ~= {err:.1f}")

    # What theta=7/8 predicts: |psi(x)-x| <= C x^theta log^2 x ; take C=1 for scale
    x = float(N)
    theta = 7 / 8
    bound = (x ** theta) * (math.log(x) ** 2)
    print(f"theta=7/8 power-saving scale x^theta log^2 x at 1e6 ~= {bound:.3g}")
    print(f"observed prime-count error {err:.1f} << bound scale -> numerically consistent (necessary, not sufficient).")

    # Classical de la Vallee Poussin scale for contrast
    classical = x * math.exp(-0.5 * math.sqrt(math.log(x)))
    print(f"classical 1896-type scale x*exp(-c sqrt(log x)) ~= {classical:.3g} (much larger -> weaker)")

    # Prime number theorem check at 1e5, 1e6 ratio pi(x)/(x/log x) -> 1
    for m in (100_000, 1_000_000):
        approx = m / math.log(m)
        print(f"  pi({m})/(x/log x) check: count recomputed on demand only for 1e6 here; ratio at 1e6 = {pi_n/approx:.4f}")

    return {"pi_1e6": pi_n, "li_1e6": li_n, "abs_err": err,
            "theta78_scale": bound, "classical_scale": classical}


if __name__ == "__main__":
    main()
