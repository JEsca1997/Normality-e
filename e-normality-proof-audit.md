# Proof Audit: Claim that e is Normal in Base 10

**Auditor:** Adversarial proof-checker  
**Date:** 2026-04-10  
**Verdict:** PROOF IS FATALLY FLAWED — does not establish normality of e.

---

## Overview

The proof attempts to leverage the factorial series expansion of e, partition digit positions into "stagnation blocks" associated with individual factorials, apply van der Corput equidistribution to the fractional parts of log₁₀(k!), and then transfer equidistribution to the digits of e via Weyl's theorem. Each step either asserts non-trivial results without proof or contains a logical error. Step 1 contains the single fatal flaw that collapses the entire argument.

---

## Step 1 — Stagnation Block Structure: FATALLY FLAWED

**The claimed identity:** d_{j_k+ℓ}(e) = d_ℓ(X_k) for ℓ = 0, ..., L_k - 1, where X_k = 10^{j_k}/k!.

This is the load-bearing claim of the entire proof, and it is false as stated.

**Why it fails.** e = Σ_{n=0}^∞ 1/n!. Therefore:

    10^{j_k} · e = Σ_{n=0}^∞ 10^{j_k}/n!
                 = (lower terms) + 10^{j_k}/k! + (tail)

where:
- Lower terms = Σ_{n < k} 10^{j_k}/n!, each of which is an integer or a large rational with a huge integer part.
- Tail = Σ_{n > k} 10^{j_k}/n!, which is small but nonzero.

The digits of 10^{j_k} · e are determined by its fractional part, which equals:

    {10^{j_k} · e} = {Σ_{n < k} 10^{j_k}/n!} + {10^{j_k}/k!} + (tail)  (mod 1)

The lower-order terms Σ_{n < k} 10^{j_k}/n! contribute a fractional part that is not controlled by X_k = 10^{j_k}/k! alone. The proof assumes these lower terms are all exact integers, but they are not — for example, 10^{j_k}/1! = 10^{j_k} is an integer, but 10^{j_k}/(k-1)! is an integer only if (k-1)! | 10^{j_k}, which fails for large k (once k-1 has prime factors other than 2 and 5, specifically any prime p ≤ k-1 with p > 5 will not divide any power of 10).

**Quantitative damage.** Let R_k = {Σ_{n=1}^{k-1} 10^{j_k}/n!}. This residual is not small; it is an arbitrary element of [0,1) whose distribution is not controlled. The actual fractional part of 10^{j_k} · e is R_k + u_k (mod 1) where u_k = {log₁₀(X_k)} is what Step 2 equidistributes. Since R_k is uncontrolled, the joint value R_k + u_k (mod 1) is not shown to equidistribute, and may not equidistribute at all.

**Conclusion on Step 1:** The identity d_{j_k+ℓ}(e) = d_ℓ(X_k) is not exact. It holds only if the lower-order factorial terms contribute no fractional carry into the digit positions [j_k, j_k + L_k), which is a highly non-trivial number-theoretic statement that is not proved and is almost certainly false in general.

---

## Step 2 — Equidistribution of u_k: ASSERTED, NOT PROVED

The claim is that {-log₁₀(k!)} equidistributes on [0,1) by van der Corput's theorem.

**Van der Corput's theorem** applies to sequences {f(k)} where f is smooth with f'(k) → ∞ monotonically. Here f(k) = log₁₀(k!), so f'(k) = log₁₀(k), which does diverge. However, van der Corput's criterion in its standard form applies to sequences of the form {f(k)} where f is a real-analytic function with uniformly growing derivative — for a sum like log₁₀(k!) = Σ_{j=1}^k log₁₀(j), one must invoke the van der Corput differencing lemma more carefully, or use Weyl's inequality for smooth sequences.

**The gap:** The proof says "by van der Corput's theorem" and cites f'(k) = log₁₀(k) → ∞. This is the right general idea, but van der Corput's theorem does not literally apply to the sequence {log₁₀(k!)} directly with this justification — the theorem requires bounds on exponential sums Σ e^{2πi h f(k)}, and the argument is nontrivial. A rigorous proof would require, e.g., the van der Corput A- and B-processes or Weyl's method for Diophantine approximation. The assertion is plausible but unproved here.

---

## Step 3 — Log-uniform Digit Lemma: MINOR ISSUE, MOSTLY CORRECT

The claim that f_{ℓ,s}(u) = 1[(d_ℓ(10^u), ..., d_{ℓ+m-1}(10^u)) = s] is Riemann-integrable on [0,1) and integrates to 10^{-m} + O_m(10^{m-ℓ}) is essentially correct for ℓ = 0, but the error term structure needs care.

**Issue:** The function f_{ℓ,s} has discontinuities only on a measure-zero set (boundaries between digit blocks), so it is indeed Riemann-integrable. The integral computes exactly the measure of {u ∈ [0,1) : m-tuple at position ℓ of 10^u equals s}. For ℓ = 0 this is exactly 10^{-m}; for ℓ > 0 the dependence on lower digits means the answer is 10^{-m} exactly (the digits are independently uniform for a log-uniform X). The O_m(10^{m-ℓ}) error term is claimed via Euler-Maclaurin, but this is an approximation method for sums, not integrals — its invocation here is puzzling and unexplained. The integral is exactly 10^{-m}, not 10^{-m} + O_m(10^{m-ℓ}).

---

## Step 4 — Weyl Equidistribution Application: STRUCTURALLY CORRECT BUT DEPENDS ON BROKEN STEP 1

The structure of Step 4 is logically valid: if u_k equidistributes and f is Riemann-integrable, then the Cesàro averages of f(u_k) converge to the integral. The proof correctly identifies this as the content of Weyl's equidistribution theorem for Riemann-integrable test functions.

**However:** This step is computing the equidistribution of digit patterns within the X_k sequence, i.e., within 10^{j_k}/k!. It does NOT compute the digit patterns of e. The connection between X_k and e requires Step 1, which is broken. Step 4 is internally valid but is measuring the wrong object.

---

## Step 5 — Exchange of Summation: UNJUSTIFIED

The exchange of Σ_k Σ_ℓ to Σ_ℓ Σ_k is presented with the bound |E(N)| = O(m·K(N) + L_{K(N)}) = o(N). This is asserted, not proved.

**The gap:** As N → ∞, both K(N) → ∞ and L_max → ∞. The exchange requires uniform convergence of the inner Cesàro averages over ℓ as ℓ → ∞ simultaneously with K_ℓ → ∞. This is a double-limit interchange that requires justification — specifically, the rate at which (1/K_ℓ)Σ_k 1[...] → 10^{-m} must be quantified and shown to be summable after weighting by K_ℓ/N. The proof waves at an O(K(N)/N) bound but does not establish the rate of convergence in Step 4, making the interchange unverified.

Additionally, the claim K(N)/N → 0 needs proof. K(N) is the number of blocks up to position N, and N ~ Σ_{k=1}^{K(N)} L_k. Since L_k ~ log₁₀(k log k), we have N ~ Σ_{k ≤ K} log log k, which grows much slower than K itself... this actually suggests K(N)/N → 0 is false in general or requires more careful analysis. Specifically if L_k ~ log k, then N ~ K log K, so K ~ N/log N, giving K(N)/N ~ 1/log N → 0. This part is probably salvageable, but is asserted.

---

## Step 6 — Combining: INTERNALLY CONSISTENT, COLLAPSES WITH STEP 1

Given the outputs of Steps 4 and 5, Step 6 is algebraically coherent. The remainder bound (1/N) Σ_ℓ K_ℓ · 10^{m-ℓ} ≤ (K(N)/N) · 10^m · Σ_ℓ 10^{-ℓ} = O(K(N)/N) → 0 is correct in form if K(N)/N → 0. The conclusion follows from the previous steps formally.

**But Step 6 proves:** (1/N)#{j < N : m-tuple of X_{k(j)} at offset ℓ(j) = s} → 10^{-m}. This is about the digit patterns of the fractional parts of 10^{j}/k(j)!, not about the digit patterns of e.

---

## Single Most Likely Fatal Flaw

**Step 1 is the fatal flaw.** The proof conflates the digits of X_k = 10^{j_k}/k! with the digits of e at positions [j_k, j_k + L_k). The fractional part of 10^{j_k} · e contains a contribution R_k from all lower factorial terms Σ_{n < k} 10^{j_k}/n!, and this residual is neither controlled nor shown to be negligible. For primes p with 5 < p ≤ k, the term 10^{j_k}/p! has a non-integer fractional part that perturbs the digits. The identity is not exact, and the approximation error is not shown to be o(1) uniformly in k. Without this identity, the proof establishes equidistribution of digits of 1/k! (scaled), not of e.

**This is not a fixable gap via a minor correction.** Controlling R_k for all k simultaneously is essentially as hard as proving normality of e directly, or requires deep results about how factorial sums approximate e. No such result is proved or cited.

---

## Assessment of What Is Actually Proved

If Steps 1–6 were all correct, the proof would establish:

> The sequence formed by reading off the digit blocks of the numbers X_k = {10^{j_k}/k!} (fractional parts of scaled inverse factorials) equidistributes over all m-tuples with frequency 10^{-m}.

This would be a non-trivial result about the distribution of fractional parts of {10^j/k!}, but it is not a statement about the normality of e.

**The normality of e in base 10 remains an open problem.** This proof does not resolve it.

---

## Summary Table

| Step | Claim | Status |
|------|-------|--------|
| 1 | d_{j_k+ℓ}(e) = d_ℓ(X_k) exactly | FATAL ERROR — false due to lower factorial residuals |
| 2 | {log₁₀(k!)} equidistributes via van der Corput | ASSERTED — plausible but unproved as written |
| 3 | f_{ℓ,s} is Riemann-integrable, integrates to 10^{-m} | MOSTLY CORRECT — Euler-Maclaurin invocation unexplained |
| 4 | Weyl's theorem applied correctly | STRUCTURALLY VALID — but applied to wrong sequence |
| 5 | Exchange of summation, E(N) = o(N) | UNJUSTIFIED — double-limit interchange unverified |
| 6 | Final limit equals 10^{-m} | INTERNALLY CONSISTENT — inherits all prior flaws |

**Overall verdict: The proof is invalid. The normality of e in base 10 is not established.**
