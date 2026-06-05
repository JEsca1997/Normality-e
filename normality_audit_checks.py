"""
Hostile audit checks for the local OFI normality manuscripts.

This script does not try to prove or disprove normality. It only reproduces
two concrete objections to the current `e` draft:

1. Log-uniform significands do not induce a uniform distribution on
   fractional parts.
2. The draft's block identity
      d_{j_k + ell}(e) = d_ell(X_k),  X_k = 10^{j_k} / k!
   fails on explicit computed examples.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from math import factorial, log, log10


def benford_fractional_part_obstruction() -> float:
    """Return P(frac(10^U) < 0.1) for U ~ Unif[0, 1)."""
    return sum(log10((n + 0.1) / n) for n in range(1, 10))


def compute_e(terms: int = 400) -> Decimal:
    getcontext().prec = 2500
    fact = 1
    total = Decimal(0)
    for n in range(terms):
        if n > 0:
            fact *= n
        total += Decimal(1) / Decimal(fact)
    return total


def decimal_digits_after_point(x: Decimal) -> str:
    text = format(x, "f")
    return text.split(".")[1]


def make_log_factorials(max_k: int) -> list[float]:
    out = [0.0] * (max_k + 1)
    for k in range(1, max_k + 1):
        out[k] = out[k - 1] + log(k)
    return out


def k_star(j: int, log_factorials: list[float]) -> int:
    target = j * log(10)
    best_k = 1
    best_gap = float("inf")
    for k in range(1, len(log_factorials)):
        gap = abs(target - log_factorials[k])
        if gap < best_gap:
            best_gap = gap
            best_k = k
    return best_k


def first_block_mismatch(start_j: int = 100, max_j: int = 600) -> dict[str, object]:
    """
    Find the first block with j >= start_j where the current manuscript's
    identity fails.
    """
    e_digits = decimal_digits_after_point(compute_e())
    log_factorials = make_log_factorials(800)

    seen = {}
    blocks = []
    prev = None
    block_start = 0
    for j in range(max_j):
        k = k_star(j, log_factorials)
        if k != prev:
            if prev is not None:
                blocks.append((prev, block_start, j - block_start))
            seen.setdefault(k, j)
            block_start = j
            prev = k
    blocks.append((prev, block_start, max_j - block_start))

    for k, j0, length in blocks:
        if j0 < start_j or length <= 0:
            continue
        x_k = (Decimal(10) ** j0) / Decimal(factorial(k))
        x_text = format(x_k, "f")
        x_frac = x_text.split(".")[1] if "." in x_text else ""
        m = min(length, 8)
        e_block = e_digits[j0 : j0 + m]
        x_block = (x_frac + "0" * (m + 4))[:m]
        if e_block != x_block:
            return {
                "k": k,
                "j0": j0,
                "length": length,
                "e_block": e_block,
                "x_block": x_block,
            }

    raise RuntimeError("No mismatch found in the requested search range.")


def main() -> None:
    p = benford_fractional_part_obstruction()
    mismatch = first_block_mismatch()

    print("Audit check 1: log-uniform != uniform fractional part")
    print(f"  P(frac(10^U) < 0.1) with U ~ Unif[0,1) = {p:.12f}")
    print("  Uniform[0,1) would give exactly 0.100000000000")
    print()

    print("Audit check 2: current block identity fails explicitly")
    print(
        "  First mismatch with j >= {j0}: k={k}, block start j0={j0}, "
        "block length={length}".format(**mismatch)
    )
    print(f"  digits of e in that block:      {mismatch['e_block']}")
    print(f"  digits of X_k = 10^j0 / k!:     {mismatch['x_block']}")
    print()

    print("Interpretation")
    print("  These checks do NOT disprove normality of e.")
    print("  They do show that the current local proof draft overclaims.")


if __name__ == "__main__":
    main()
