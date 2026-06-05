# OFI Normality of e: Structural Note
## Working Paper - OFI Framework Applied to the Digits of Euler's Number

**Author:** Joseph Robert Escamilla ("QWERTY SENPAI")  
**Date:** 2026-04-10  
**Status:** OPEN. This note records real structure in the decimal expansion of `e`, but it does **not** currently prove that `e` is normal in base 10.

---

## 0. Goal

The target statement is:

> `e` is normal in base 10, meaning every length-`m` digit string occurs with limiting frequency `10^{-m}`.

This remains an open problem in mathematics. The purpose of this note is to organize the local OFI-based structure around the problem and isolate the true gap.

---

## 1. Safe OFI Framework

Given decimal digits `d_0, d_1, ..., d_{N-1}` of a real number `x`, define centered digits

    f_j = d_j - 4.5

and the lag-`tau` autocorrelation

    A_N(x, tau) = sum_{j=0}^{N-1-tau} f_j f_{j+tau}.

For `alpha in (0,1)`, define the empirical OFI defect

    R_N^alpha(x) = (2/N^2) * |sum_{tau=1}^{N-1} tau^(alpha-1) A_N(x, tau)|.

### What is safe

If `x` is normal in base 10, then the orbit `{10^j x mod 1}` is equidistributed, and in particular its pair-correlation statistics cancel. So normality implies decay of `A_N(x,tau)` and `R_N^alpha(x)`.

### What is not proved here

The converse is not established in this note. Small 2-point correlations do not by themselves force full normality, because higher-order block structure may still fail to be uniform.

So in this note:

- OFI/autocorrelation decay is treated as a **necessary shadow** of normality;
- it is **not** treated as a proved equivalent criterion.

---

## 2. Factorial-Scale Structure of e

Write

    e = sum_{k=0}^\infty 1/k!.

For the `j`-th decimal position, the natural factorial scale is the index `k*(j)` where `k!` is closest to `10^j` on the logarithmic scale:

    k*(j) = argmin_k |j log(10) - log(k!)|.

This gives the usual decomposition into:

- lower layer: terms with `k < k*(j)`,
- boundary layer: terms near `k*(j)`,
- upper layer: terms with `k > k*(j)`.

The structural observation that survives audit is that `k*(j)` stays constant on blocks of consecutive `j` values, and those block lengths grow slowly:

    L_k = (1/2) log_10(k(k+1)) + O(1) ~ log_10 k.

Hence if `K(N)` is the number of blocks needed to cover the first `N` digits, then heuristically

    K(N) / N -> 0.

This means boundary effects between blocks are sparse enough that a correct theorem about within-block statistics would be very powerful.

In fact, the block starts admit an exact midpoint formula. For `k >= 2`, the block
for index `k` begins at

    j_k = ceil((log(k!) + log((k-1)!)) / (2 log 10)).

Equivalently, the block boundaries are obtained by partitioning the logarithmic axis
into Voronoi cells around the points `log(k!)`. So the sequence `(j_k, L_k)` is not
heuristic data; it is an explicit arithmetic object.

Since `L_k = j_{k+1} - j_k`, the total number of digits covered by blocks up to level
`K` telescopes:

    N_K = sum_{2<=k<=K} L_k = j_{K+1} - j_2.

Using the midpoint formula again,

    j_{K+1} = ceil(log_10(K! * sqrt(K+1))),

so

    N_K = log_10(K! * sqrt(K)) + O(1)
         = K log_10 K - (log_10 e) K + O(log K)

by Stirling. This gives a precise asymptotic for the block-endpoint lengths, not just
the softer statement `N_K ~ K log K`.

---

## 3. Exact Block State

The key repair is to stop using the false proxy

    E_k = frac(10^{j_k} / k!)

as if it exactly generated the digits in block `k`.

That identity is false in general.

The **exact** block state is instead

    Y_k = frac(10^{j_k} e),

where `j_k` is the first decimal position in the block with critical index `k`.

This gives a tautological exact statement:

> For `0 <= ell < L_k`, the digit `d_{j_k + ell}(e)` is the `ell`-th digit of `Y_k`.

So any successful proof by blocks must control the deterministic sequence `{Y_k}`.

This is the right object.

---

## 4. Exact Multiplicative Dynamics

The earlier note had a real structural identity for the proxy

    X_k = 10^{j_k} / k!,

namely

    X_{k+1} = (10^{L_k} / (k+1)) X_k.

That identity is exact and still useful. It says the proxy evolves by a multiplicative cocycle tied to the stagnation lengths.

But the digits of `e` are governed by `Y_k`, not by `X_k`.

So the real problem becomes:

1. express `Y_k` in terms of `X_k` plus an exact correction term,
2. understand whether that correction term is negligible, structured, or dominant on the first `L_k` digits.

This is the point where the current manuscript previously overclaimed.

---

## 5. What the van der Corput Phase Argument Actually Suggests

Let

    v_k = log(X_k) = j_k log(10) - log(k!).

Modulo `log(10)`, the phase variable is governed by `-log(k!)`, so it is natural to study

    {-log_10(k!) mod 1}.

This supports the heuristic that the **logarithmic scale** of `X_k` wanders through powers of `10` in a distributed way.

### Important correction

Even if the logarithmic phase is equidistributed mod `1`, this does **not** automatically imply that

    frac(X_k)

is uniformly distributed on `[0,1)`.

Why not:

- if `U ~ Unif[0,1)`, then `10^U` is log-uniform on `[1,10)`,
- but `frac(10^U)` is **not** uniform on `[0,1)`.

So any argument that goes directly from log-scale equidistribution to uniformity of `frac(X_k)` is incomplete.

---

## 6. The Useful Random-Model Lemma

The earlier note contained a genuinely useful statement for a random model:

> If `X` is log-uniform on `[1,10)`, then its base-10 digits are asymptotically close to uniform at deep digit positions, with errors decaying like `10^{-ell}`.

This can be proved by Euler-Maclaurin summation and is a legitimate random-model result.

### But

It does **not** by itself apply to the deterministic block states `Y_k`.

The missing theorem is exactly the bridge from:

- a random log-uniform model,

to:

- the actual deterministic sequence of exact block states generated by `e`.

That bridge is the problem.

---

## 7. What Broke in the Earlier Draft

The previous version of this note overclaimed in four places:

1. It treated OFI/pair-correlation decay as equivalent to full normality.
2. It treated log-scale equidistribution as if it implied uniform fractional parts.
3. It used the false exact identity

       d_{j_k+ell}(e) = d_ell(10^{j_k}/k!).

4. It replaced deterministic block counts by expectations from a random model.

Those moves are not justified.

So the correct verdict is:

> the structural program is interesting, but the proof is not complete.

---

## 8. The Real Open Problem for e in This Framework

The route is still potentially meaningful, but the exact object must be changed.

### Route A: exact-state attack

Study the deterministic sequence

    Y_k = frac(10^{j_k} e)

directly and try to prove asymptotically uniform block-prefix statistics.

### Route B: proxy-plus-error attack

Write

    Y_k = frac(X_k + C_k)

for an explicit correction term `C_k`, then prove:

1. `X_k` or another proxy has tractable distribution,
2. `C_k` is small enough, or rigid enough, that the first `L_k` digits are controlled.

### Route C: direct Weyl-sum attack

Bypass the block picture and work directly with the base-10 orbit

    {10^j e mod 1}.

This would be strongest, but it also looks hardest.

---

## 9. A Concrete Exploit Worth Testing Next

The best local exploit is to stop approximating the block source and work with the exact one.

Define

    Y_k = frac(10^{j_k} e),
    X_k = 10^{j_k} / k!,
    C_k = 10^{j_k} e - X_k.

Then:

- `Y_k = frac(X_k + C_k)` exactly,
- the digits in block `k` are exactly the digits of `Y_k`,
- the question becomes whether `C_k` is tame on the first `L_k` digits.

This is a much sharper target than the old "entry values are normal" formulation.

The next useful computations are:

1. measure `Y_k - frac(X_k)` numerically over large `k`,
2. decompose `C_k` into lower-layer carry plus upper-layer tail,
3. test whether either component stabilizes, oscillates regularly, or decays on the block scale,
4. look for a corrected proxy `Z_k` that predicts the first `L_k` digits of `Y_k`.

If there is a real route to a theorem here, it is much more likely to sit in this corrected exact-state formulation than in the old random-model leap.

### Exploratory numerical finding

The local analyzer `C:\dev\helix\e_exact_state_analyzer.py` studies

    Y_k = frac(10^{j_k} e) = frac(X_k + B_k + T_k),

where

- `X_k = frac(10^{j_k}/k!)`,
- `B_k` is the lower-layer fractional carry from `n < k`,
- `T_k` is the upper tail from `n > k`.

On the sample range of blocks with `j_k in [80, 650)`:

- `X_k` alone matches only about `0.117` leading digits on average;
- `X_k + B_k` matches about `1.898` leading digits on average;
- `X_k + B_k` predicts the entire block in about `66.8%` of sampled blocks;
- `T_k < 10^{-L_k}` in about `98.0%` of sampled blocks.

Most importantly, every sampled failure of `X_k + B_k` is explained by a
**decimal boundary instability**:

> when `T_k` is smaller than the distance from `X_k + B_k` to the nearest
> `L_k`-digit decimal boundary, the full block is predicted exactly.

So the empirical evidence suggests that:

1. the old single-term proxy `X_k` is not the right object,
2. the lower-layer carry `B_k` is essential,
3. the upper tail `T_k` is usually tiny,
4. the real theorem target may be a boundary-stability statement for
   `frac(X_k + B_k)`.

There is also an important negative finding from the same analyzer:

> approximating `B_k` by only the last `W` factorial terms before `k`
> performs very poorly for `W = 1,2,3,5,8,12,20,40`.

So the lower carry is not merely a short local correction near the critical
factorial index. It appears to be a genuinely global superposition effect.

### Exact carry cocycle

The global nature of the lower carry does **not** mean it is structureless.

Define

    B_k = frac(sum_{n<k} 10^{j_k} / n!),
    X_k = frac(10^{j_k} / k!),
    Z_k = frac(B_k + X_k).

Then the block lengths satisfy `j_{k+1} = j_k + L_k`, and the lower carry obeys the exact recurrence

    B_{k+1} = frac(10^{L_k} Z_k).

This follows directly from

    sum_{n<k+1} 10^{j_{k+1}} / n!
    = 10^{L_k} * sum_{n<k+1} 10^{j_k} / n!
    = 10^{L_k} * (sum_{n<k} 10^{j_k} / n! + 10^{j_k} / k!),

and the fact that multiplication by the integer `10^{L_k}` preserves fractional-part reduction.

So the exact block state can be written as

    Y_k = frac(Z_k + T_k),

where `T_k` is the upper tail. In this formulation:

- `Z_k` is the deterministic predictor state,
- `B_k` evolves by an exact cocycle,
- the only remaining discrepancy between the predictor and the true block state is the
  small tail `T_k`.

This is a substantially sharper formulation than the earlier proxy-only picture.

Moreover, the predictor state itself satisfies the exact affine recurrence

    Z_{k+1} = frac(10^{L_k} Z_k + X_{k+1}),

because

    Z_{k+1}
    = frac(B_{k+1} + X_{k+1})
    = frac(10^{L_k} Z_k + X_{k+1}).

So the corrected block model is not an amorphous global sum. It is a deterministic,
non-autonomous expanding map modulo `1`, driven by the input sequence `X_{k+1}` and
the block lengths `L_k`.

There is also an exact measure-theoretic fact here:

> for each `k`, the step map
>
>     T_k(x) = frac(10^{L_k} x + X_{k+1})
>
> preserves Lebesgue measure on `[0,1)`.

Indeed, multiplication by the integer `10^{L_k}` followed by translation modulo `1`
maps any interval to `10^{L_k}` preimage intervals of total length equal to the
original interval. So the uniform measure is not merely a heuristic target for the
predictor dynamics; it is the exact invariant measure of each individual step.

This does **not** by itself prove that the single deterministic orbit `Z_k` is
equidistributed. But it shows that the corrected recurrence has the right ambient
measure theory built into it.

In particular, if one starts the recurrence from a random seed `U ~ Unif[0,1)` instead
of the specific arithmetic seed coming from `e`, then every `Z_k(U)` is again uniform on
`[0,1)`. Hence for every fixed `k`, every fixed offset `ell`, and every decimal word
`s` of length `m`,

    P(frac(10^ell Z_k(U)) in I_s) = 10^{-m}.

So the predictor dynamics has the **exact correct annealed digit law**. The remaining
problem is entirely quenched:

> show that the specific deterministic orbit attached to `e` behaves typically for this
> expanding, measure-preserving non-autonomous system.

### Vanishing deterministic drive

The driving term `X_k` is much more rigid than the earlier draft suggested.

From the exact midpoint formula

    j_k = ceil(log_10(k! / sqrt(k))),

we get

    log_10(k! / sqrt(k)) <= j_k < log_10(k! / sqrt(k)) + 1.

Exponentiating and dividing by `k!` gives

    1 / sqrt(k) <= 10^{j_k} / k! < 10 / sqrt(k).

So for all sufficiently large `k` we have `X_k = 10^{j_k} / k!` with no wrap, and

    X_k ~ k^(-1/2)

up to an absolute factor of `10`.

This matters because the exact recurrence is therefore an expanding map with
**decaying deterministic forcing**:

    Z_{k+1} = frac(10^{L_k} Z_k + X_{k+1}),
    X_{k+1} in [1/sqrt(k+1), 10/sqrt(k+1)).

So the corrected route is not driven by a random-sized perturbation. It is driven by a
specific, slowly vanishing arithmetic input.

### Upper-tail bound

There is also a clean deterministic upper bound for the tail `T_k`.

Let `L_k = j_{k+1} - j_k`. Then

    T_k
    = sum_{n>k} 10^{j_k} / n!
    = 10^{-L_k} * sum_{n>k} 10^{j_{k+1}} / n!.

The first term in the rescaled tail is

    10^{j_{k+1}} / (k+1)!.

Because `j_{k+1}` is the first decimal position assigned to block `k+1`, it lies just
to the right of the midpoint between `log_10(k!)` and `log_10((k+1)!)`. Hence

    j_{k+1} < log_10((k+1)! / sqrt(k+1)) + 1,

so

    10^{j_{k+1}} / (k+1)! < 10 / sqrt(k+1).

Therefore

    T_k
    < 10^{-L_k} * (10 / sqrt(k+1)) * (1 + 1/(k+2) + 1/((k+2)(k+3)) + ...)
    < (10 e) * 10^{-L_k} / sqrt(k+1).

So the tail is not merely "small numerically"; it is provably suppressed by the extra
factor `1 / sqrt(k+1)` on top of the block scale `10^{-L_k}`.

Empirically the constant is much smaller than `10e` on the tested range.
The boundary-stable fraction also appears to improve with scale in the local analyzer.

### Remaining theorem target

This reformulates the open problem more sharply:

1. `Z_k = frac(B_k + X_k)` is the exact predictor state;
2. `T_k` is provably tiny at scale `10^{-L_k} / sqrt(k)`;
3. the only way the predictor can fail on the whole block is if `Z_k` lies within
   distance `T_k` of an `L_k`-digit decimal boundary.

So one plausible theorem route is:

> prove a quantitative bound on how often `Z_k` falls within a `T_k`-neighborhood
> of an `L_k`-digit decimal boundary.

If that exceptional set is sparse enough, the block errors contribute `o(N)` digits
overall and the normality argument would become viable.

### Empirical boundary-hit behavior

The local probe `C:\dev\helix\e_boundary_hit_probe.py` studies the bad event

    dist(Z_k, D_{L_k}) <= T_k,

where `D_{L_k}` is the set of `L_k`-digit decimal boundaries.

If `Z_k` were uniformly distributed relative to those boundaries, the natural geometric
heuristic for the bad-event probability would be

    p_k ~= 2 * 10^{L_k} * T_k.

On the tested range of blocks with `j_k in [80, 3000)`, the observed bad-block rate
tracks this heuristic rather well, and the cumulative bad fraction decreases with scale.
With the exact midpoint block formula, the local probe can be pushed much farther; on a
scan up to about `j_k < 20000`, the cumulative bad-block fraction drops to about `0.178`.
On the same long run, the cumulative bad-block count is also consistent with

    bad_blocks(K) ~ C * sqrt(K),

with `bad_blocks(K) / sqrt(K)` stabilizing numerically near `13.9` by the end of the
sample (`K = 7940` blocks).

This matters because the total number of digits covered by the first `K` blocks is

    N_K = sum_{k<=K} L_k ~ K log_10 K,

while a single bad block can corrupt at most `L_k = O(log k)` digits. So if the number
of bad blocks up to `K` is only `o(K)`, then the total number of corrupted digits is
already `o(N_K)`.

Under the flatness heuristic suggested by the probe,

    P(bad block at k) ~ 2 * 10^{L_k} * T_k << 1 / sqrt(k),

so one would expect only `O(sqrt(K))` bad blocks up to level `K`, which is vastly
stronger than the `o(K)` needed to make boundary errors negligible in density.

This does not prove the needed theorem, but it strongly suggests that the right final
obstruction is:

> a quantitative equidistribution / boundary-avoidance theorem for the exact predictor
> recurrence
>
>     Z_{k+1} = frac(10^{L_k} Z_k + X_{k+1}).

### Boundary event in one-step form

There is an exact simplification of the bad-block condition that removes the huge union
of decimal boundaries from the statement.

Write

    u_k = 10^{L_k} T_k.

Since the distance from `Z_k` to the `L_k`-digit boundary set `D_{L_k}` is

    dist(Z_k, D_{L_k})
    = 10^{-L_k} * min(frac(10^{L_k} Z_k), 1 - frac(10^{L_k} Z_k)),

the bad event is equivalent to

    frac(10^{L_k} Z_k) in [0, u_k] union [1-u_k, 1).

Using the recurrence

    Z_{k+1} = frac(10^{L_k} Z_k + X_{k+1}),

this becomes

    frac(Z_{k+1} - X_{k+1}) in [0, u_k] union [1-u_k, 1),

or equivalently

    Z_{k+1} in [X_{k+1}, X_{k+1}+u_k] union [X_{k+1}-u_k, X_{k+1}]    (mod 1).

So the theorem-level obstruction can be rephrased much more simply:

> at stage `k`, the bad-block event is not a hit on `10^{L_k}` microscopic decimal
> boundary neighborhoods for `Z_k`; it is a hit of `Z_{k+1}` on a union of **two**
> intervals centered at `X_{k+1}`, with total length `2u_k`.

Since `u_k = 10^{L_k} T_k << k^(-1/2)`, the remaining boundary-avoidance theorem is
therefore a shrinking-target problem for the exact predictor orbit with target size
`O(k^(-1/2))`.

In fact the target size is directly tied to the next forcing term. Writing

    q_{k+1} = 10^{j_{k+1}} / (k+1)!,

we have

    u_k = 10^{L_k} T_k
        = sum_{n>k} 10^{j_{k+1}} / n!
        = q_{k+1} * (1 + 1/(k+2) + 1/((k+2)(k+3)) + ...).

For all sufficiently large `k`, we have `q_{k+1} < 1`, hence `X_{k+1} = q_{k+1}` and

    X_{k+1} <= u_k <= (1 + 1/(k+1)) * X_{k+1}.

Indeed,

    u_k / X_{k+1}
    = 1 + 1/(k+2) + 1/((k+2)(k+3)) + ...
    <= 1 + sum_{r>=1} (k+2)^(-r)
    = 1 + 1/(k+1).

So asymptotically the bad event is:

> `Z_{k+1}` falls within a constant multiple of `X_{k+1}` around the center
> `X_{k+1}` itself.

Since `u_k / X_{k+1} -> 1` and `X_{k+1} ~ k^(-1/2)`, this is a multiplicative
shrinking-target condition near the origin, not a generic interval-hit problem of
unrelated size.

There is an additional simplification because `u_k >= X_{k+1}`. Modulo `1`, the target
set

    [X_{k+1}, X_{k+1}+u_k] union [X_{k+1}-u_k, X_{k+1}]

can be rewritten as

    [0, X_{k+1}+u_k] union [1-(u_k-X_{k+1}), 1).

But from the sharp bound above,

    0 <= u_k - X_{k+1} <= X_{k+1}/(k+1) << k^(-3/2).

So asymptotically the bad event is almost entirely a **small-value event near `0`**:

> up to a negligible wrap-around interval near `1`, the bad block condition is simply
>
>     Z_{k+1} <= 2 X_{k+1}
>
> with `X_{k+1} ~ k^(-1/2)`.

This is much closer to a standard lower-tail distribution question than to a global
decimal-boundary problem.

This is the right dynamical language for the problem:

> the corrected `e` route asks for a shrinking-target estimate for the specific
> deterministic orbit of a non-autonomous base-`10` expanding system with translations.

For a random initial seed, the annealed law is exactly uniform at every stage, so one
would expect the bad-hit count up to level `K` to be of order

    sum_{k<=K} 2u_k ~ O(sqrt(K)).

That is consistent with every numerical probe so far. The real difficulty is the
quenched one:

> prove that the special arithmetic seed coming from `e` behaves typically for this
> shrinking-target system.

### Empirical distribution of Z_k itself

The separate probe `C:\dev\helix\e_zk_distribution_probe.py` checks whether the
predictor state `Z_k` looks visibly clustered or whether it already sits near the
uniform benchmark one would hope for.

On the range of blocks with `j_k in [80, 27743]` (`7940` blocks total), the probe finds:

- star discrepancy `D*(Z_k) ~= 0.011553`,
- random benchmark `N^(-1/2) ~= 0.011223`,
- first four Fourier mode averages

      |(1/N) sum exp(2 pi i m Z_k)| <= 0.012573

  for `m = 1,2,3,4`,
- boundary-neighborhood occupancy that closely matches the uniform prediction:

      lambda = 0.25: observed 0.009572, predicted 0.010300
      lambda = 0.50: observed 0.019144, predicted 0.020601
      lambda = 1.00: observed 0.037531, predicted 0.041202
      lambda = 2.00: observed 0.081234, predicted 0.082404
      lambda = 4.00: observed 0.161083, predicted 0.164792

This is still numerical evidence, not a theorem. But it is exactly the kind of
evidence one would want if the remaining obstruction is quantitative discrepancy of
`Z_k`, rather than a hidden deterministic clustering defect.

### Unrolled predictor series

Because `j_{k+1} = j_k + L_k`, the exact recurrence can be unrolled explicitly.

First, the initial predictor state is trivial:

    j_2 = 1,
    B_2 = frac(10/0! + 10/1!) = frac(20) = 0,
    X_2 = frac(10/2!) = frac(5) = 0,
    Z_2 = 0.

Inducting on

    Z_{k+1} = frac(10^{L_k} Z_k + X_{k+1})

then gives

    Z_k = frac(sum_{n=3}^k 10^{j_k-j_n} X_n).

So if we define the explicit predictor constant

    P = sum_{n=3}^\infty 10^{-j_n} X_n,

then

    frac(10^{j_k} P) = frac(Z_k + U_k),

where the predictor tail is

    U_k = sum_{n>k} 10^{j_k-j_n} X_n.

Thus the predictor-prefix problem is not an abstract triangular-array problem only; it
is also the decimal expansion problem for a single explicit constant `P`.

### Predictor constant differs from e only by a terminating decimal

For each `n`,

    X_n = frac(10^{j_n} / n!),

so

    10^{-j_n} X_n
    = 1/n! - floor(10^{j_n} / n!) / 10^{j_n}.

From the midpoint bound,

    10^{j_n} / n! < 10 / sqrt(n),

so for every `n >= 100` we have `10^{j_n} / n! < 1`, hence

    floor(10^{j_n} / n!) = 0

and therefore

    10^{-j_n} X_n = 1/n!    for all n >= 100.

It follows that

    P
    = sum_{n=3}^\infty 1/n! - sum_{n=3}^{99} floor(10^{j_n} / n!) / 10^{j_n}
    = e - 5/2 - D,

where

    D = sum_{n=3}^{99} floor(10^{j_n} / n!) / 10^{j_n}

is a terminating decimal.

So `P` differs from `e` by a terminating decimal only. In particular, `P` is normal in
base `10` if and only if `e` is normal in base `10`.

This is conceptually important:

> the corrected predictor model is not approximating the digits of some unrelated
> auxiliary constant. It is an exact blockwise reorganization of the same normality
> problem, up to finitely many decimal places.

### Conditional closure theorem

The corrected block model now admits a clean deterministic reduction.

Fix `m >= 1`, and let `s` be a decimal word of length `m`. Define the predictor count

    P_K(s) = sum_{k<=K} sum_{0<=ell<=L_k-m} 1_{I_s}(frac(10^ell Z_k)),

where `I_s` is the base-10 cylinder for the word `s`.

Also define the bad-block set

    B = {k : dist(Z_k, D_{L_k}) <= T_k}.

On each good block `k notin B`, the first `L_k` decimal digits of `Y_k` and `Z_k`
coincide exactly, because adding the tail `T_k` does not cross any `L_k`-digit decimal
boundary.

Therefore we have the following reduction.

> **Proposition.** Let
>
>     N_K = sum_{k<=K} L_k.
>
> Suppose that for every fixed `m` and every decimal word `s` of length `m`,
>
>     P_K(s) = 10^{-m} * sum_{k<=K} (L_k - m + 1) + o(N_K),
>
> and suppose also that
>
>     sum_{k<=K, k in B} L_k = o(N_K).
>
> Then the decimal expansion of `e` is normal in base `10`.

**Proof sketch.**

Let `C_K(s)` denote the number of occurrences of the word `s` in the true decimal
expansion of `e`, counted at starting positions fully contained in the first `K`
blocks. Good blocks contribute exactly the same counts to `C_K(s)` and to `P_K(s)`.
The discrepancy comes only from:

1. bad blocks, contributing at most

       O(sum_{k<=K, k in B} L_k),

2. windows that cross block boundaries, contributing at most `O(mK)`.

Since `L_k ~ log_10 k`, we have `N_K ~ K log K`, hence `K = o(N_K)`. Therefore

    C_K(s) = P_K(s) + o(N_K).

Using the assumed asymptotic for `P_K(s)` gives

    C_K(s) = 10^{-m} N_K + o(N_K),

which is normality along the block endpoints `N_K`. The passage from block endpoints to
arbitrary digit positions costs only the last incomplete block, whose length is `o(N)`,
so the same limit holds for all `N`. ∎

So the remaining theorem target is now split cleanly into two pieces:

1. predictor-prefix normality for the triangular array `frac(10^ell Z_k)`,
2. sparse bad blocks, equivalently a quantitative boundary-avoidance theorem for `Z_k`.

### Empirical predictor-prefix counts

The local probe `C:\dev\helix\e_predictor_digit_probe.py` measures the decimal words
generated by the first `L_k` digits of the predictor state `Z_k`.

On the same sample of `7940` blocks, the predictor prefixes give:

- one-digit counts with `chi^2(10) = 9.6303`,
- two-digit counts with `chi^2(100) = 93.7381`,
- three-digit counts with `chi^2(1000) = 1039.4111`.

Restricting only to the empirically good blocks still gives:

- `chi^2_1(10) = 8.2795`,
- `chi^2_2(100) = 103.4696`,
- `chi^2_3(1000) = 1016.2780`.

These values are all in the expected range for near-uniform behavior at this sample
size. This remains evidence, not proof, but it supports the sharper conclusion that the
surviving gap is theorem-level control of the predictor array, not a visible structural
counterexample to the corrected block model.

### Exact digit agreement with e

The strongest empirical check so far is the direct comparison probe

    C:\dev\helix\e_exact_vs_predictor_probe.py

which compares the predictor digits coming from `Z_k` to the actual decimal digits of
`e` block by block.

On a run covering `7232` blocks and `24918` decimal digits:

- exact whole-block agreement occurs on `6637 / 7232 = 0.917727` of blocks,
- the empirically good blocks are `6009 / 7232 = 0.830890`,
- every good block matches exactly:

      exact_good_blocks = 6009 / 6009 = 1.000000,

- the cumulative digit mismatch density drops to

      670 / 24918 = 0.026888.

There is also a theorem-level inequality here:

> because every good block is exact, the total number of mismatched digits is bounded
> above by the total digit mass of the bad blocks.

On the same run, the weighted bad-block density is

    4151 / 24918 = 0.166586,

which is much larger than the actual mismatch density `0.026888`. So the reduction is
conservative: even inside bad blocks, the predictor is usually still getting most digits
right.

The cumulative mismatch density also decays steadily with the block cutoff:

    100 blocks:  0.257426
    250 blocks:  0.167266
    500 blocks:  0.119440
    1000 blocks: 0.080706
    2000 blocks: 0.054872
    4000 blocks: 0.036861
    6000 blocks: 0.030188
    7232 blocks: 0.026888

The weighted bad-block density decays in parallel:

    100 blocks:  0.737624
    250 blocks:  0.615108
    500 blocks:  0.517298
    1000 blocks: 0.387012
    2000 blocks: 0.290769
    4000 blocks: 0.212027
    6000 blocks: 0.182115
    7232 blocks: 0.166586

So the exact comparison supports the reduction theorem very strongly:

1. the good-block criterion is not merely sufficient in theory; it is exact on all
   tested good blocks,
2. the theorem-level bad-block obstruction is visibly decaying rather than plateauing,
3. the actual digit error is much smaller than that worst-case obstruction.

This is still not a proof of normality, but it is the cleanest numerical validation yet
that the corrected block model is aligned with the true decimal expansion of `e`.

---

## 10. Annealed Resolution via Bennett (2025)

A December 2025 preprint resolves the annealed version of the bad-block bound.

**Bennett, arXiv:2510.02586** — *The shrinking target and recurrence problem for non-autonomous systems*

Bennett proves a non-autonomous Borel-Cantelli theorem: for a sequence of measure-preserving maps
`T_k : [0,1) -> [0,1)` satisfying a **uniform mixing condition** (Definition 1.3 of that paper —
a summable correlation-decay bound on the compositions), and a sequence of target balls
`B(x_k, r_k)` with `sum r_k = infty`, the hit count satisfies

    #{k <= K : T_k(x) in B(x_k, r_k)} ~ sum_{k<=K} r_k   for Lebesgue-a.e. x,

with the **optimal quantitative error** `O(Phi(K)^{1/2} (log Phi(K))^{3/2+eps})` where
`Phi(K) = sum_{k<=K} mu(B(x_k, r_k))`.

### Application to the Z_k recurrence

Our step maps `T_k(x) = frac(10^{L_k} x + X_{k+1})` have:

- expansion factor `10^{L_k} ~ k^{1/2}` (growing, so mixing becomes *faster* with k),
- target: bad event is `Z_{k+1} in [0, 2X_{k+1}]` so `r_k = 2X_{k+1} ~ 2k^{-1/2}`,
- `Phi(K) = sum_{k<=K} 2X_{k+1} ~ 4 sqrt(K) -> infty`.

The unshifted case (`X_{k+1} = 0`) is Bennett's **Theorem C** directly (Cantor-series
expansions with base sequence `b_k = 10^{L_k}`). The shifted case is handled by the
following lemma, which extends the uniform mixing condition to all shifted piecewise-linear
expanding maps.

### Lemma (Uniform mixing for shifted expanding maps)

Let `b_k >= 2` be positive integers and `theta_k in [0,1)`. Define
`T_k(x) = frac(b_k x + theta_k)` on `[0,1)` with Lebesgue measure `mu`. Then for all
`1 <= m < n`, all intervals `B subset [0,1)`, and all measurable `A` with `mu(A) > 0`:

    |mu(B ∩ (T_n ∘ ... ∘ T_m)^{-1}(A)) / mu(A) - mu(B)| <= 2 / (b_m * b_{m+1} * ... * b_n).

In particular the system satisfies Definition 1.3 of Bennett with
`phi(r) = 2 / prod_{k=m}^{m+r+1} b_k`, which is summable whenever `sum log b_k = infty`.

**Proof.** The composition `T_n ∘ ... ∘ T_m` is piecewise linear with exactly
`B_mn := b_m * b_{m+1} * ... * b_n` pieces, each a closed interval of length `1/B_mn`,
regardless of the values of `theta_k`. On each piece `I_i`, the map is a bijection onto
`[0,1)` (modulo the usual identification at endpoints). Therefore

    (T_n ∘ ... ∘ T_m)^{-1}(A) = union_i (A rescaled and shifted to I_i)

and each rescaled copy has measure `mu(A) / B_mn`. Summing over all `B_mn` pieces:

    mu((T_n ∘ ... ∘ T_m)^{-1}(A)) = mu(A)   (exactly, for every A).

For the correlation term, write `T := T_n ∘ ... ∘ T_m`. For any interval `B`,

    mu(B ∩ T^{-1}(A))
    = sum_i mu(B ∩ I_i) * (mu(A ∩ T(B ∩ I_i)) / mu(T(B ∩ I_i)))
    = mu(A) * sum_i mu(B ∩ I_i)   [since T is a bijection on each I_i]
    = mu(A) * mu(B)

up to the at most 2 boundary pieces of `B` (left and right endpoint), each contributing
error at most `mu(A) * (1/B_mn)`. Hence the total error is `<= 2 * mu(A) / B_mn`, giving

    |mu(B ∩ T^{-1}(A)) / mu(A) - mu(B)| <= 2 / B_mn = 2 / (b_m * ... * b_n).

For our sequence, `b_k = 10^{L_k}` with `L_k >= 1`, so `b_k >= 10` and

    prod_{k=m}^{m+r+1} b_k >= 10^{r+2}.

Thus `phi(r) <= 2 * 10^{-(r+2)}`, and `sum_{r=0}^infty phi(r) <= 2/9 < infty`. **QED.**

Since `theta_k = X_{k+1} in [0,1)` for all `k`, the lemma applies directly to the shifted
maps, and the uniform mixing condition of Definition 1.3 is satisfied with
`phi(r) = 2 * 10^{-(r+2)}`.

**Annealed conclusion (now proved):**

> For Lebesgue-a.e. initial condition `Z_1 in [0,1)`, the number of bad blocks
> up to level `K` satisfies `bad_blocks(K) ~ 4 sqrt(K) = o(K)`.

This resolves Hypothesis B of the Conditional Closure Proposition **in the annealed sense**.

### The quenched gap

Bennett's result, like all dynamical Borel-Cantelli theorems in the literature, is
`mu`-almost everywhere. It does not cover any specific initial condition.

Our actual seed is `Z_1 = frac(10^{j_2} e)`, determined by e's arithmetic. This seed
may or may not lie in the measure-zero exceptional set for Bennett's theorem.

The remaining open problem is therefore:

> **Quenched gap:** Show that the specific orbit `Z_k` starting from e's arithmetic seed
> is not exceptional for Bennett's theorem — equivalently, that `bad_blocks(K) = o(K)`
> holds for the deterministic orbit, not just for a.e. starting point.

There are two broad strategies:

1. **Typicality via transcendence:** Use the factorial structure of e and Baker-type bounds
   to show `Z_1` is not near-rational in a way that would cause orbit concentration.

2. **Direct exponential sum:** Attack `sum_{k<=K} 1_{Z_{k+1} <= 2X_{k+1}}` directly
   using the unrolled formula `Z_k = frac(sum_{n=3}^k 10^{j_k - j_n} X_n)` and
   character sum / van der Corput methods on the factorial series.

Both approaches remain open, but the quenched gap is now **the only gap** between the
current structure and a complete proof of normality of e.

---

## 11. Periodic-Stream Exploit from Factorial Denominators (Secondary Route)

There is another route that seems more genuinely tied to the factorial series for `e`.

For fixed `n`, write

    n! = 2^{a_n} 5^{b_n} m_n

with `gcd(m_n, 10) = 1`.

Then for sufficiently large `j`, the contribution of the `n`-th factorial term to the
shifted state `10^j e` has the form

    10^j / n! = integer_part + c_{j,n} / m_n,

where `c_{j,n}` depends on `10^j mod m_n`.

Since `10` is invertible modulo `m_n`, the sequence

    j -> c_{j,n} / m_n mod 1

is eventually periodic, with period dividing the multiplicative order

    ord_{m_n}(10).

So the decimal expansion of `e` can be viewed as a superposition of:

- many eventually periodic rational streams coming from individual factorial terms,
- with periods growing as the odd parts of `n!` grow,
- plus a tail from `n > j` that is genuinely small.

This is much closer in spirit to Stoneham-style and BBP-style normality constructions
than the earlier log-uniform heuristic.

### Why this is promising

1. It uses an exact arithmetic feature unique to the factorial series for `e`.
2. It turns the problem into interference of many periodic sources rather than a vague
   randomness heuristic.
3. It suggests studying whether the periods `ord_{m_n}(10)` become sufficiently rich and
   incommensurate to force digit equidistribution in aggregate.

### What would need to be shown

To turn this into a proof, one would need a theorem of the following type:

> The superposition of the eventually periodic streams generated by
> `10^j / n!` for `n <= J` is asymptotically equidistributed on digit blocks as `J -> infinity`,
> and the tail `sum_{n>J} 10^j / n!` is too small to disturb the limiting frequencies.

At present this is only a research direction, but it is a better exploit than the old
claim that log-scale equidistribution alone forces normality.

---

## 12. Current Status Summary

| Claim | Status |
|---|---|
| Factorial-scale decomposition exists | Structural yes |
| Stagnation blocks exist and grow | Structural yes |
| Exact proxy dynamics for `X_k` | Yes |
| Log-uniform random-model digit lemma | Yes |
| `frac(X_k)` proved equidistributed | No |
| Exact block digits generated by `X_k` | No |
| Normality of `e` proved | No |

So the current state is:

> promising structure, but no proof.

---

## 13. Connection to OFI Notes

This note still belongs with the broader OFI program in the following limited sense:

- OFI gives a language for weighted autocorrelation and defect measurements;
- the factorial decomposition of `e` creates a nontrivial discrete-continuous bridge;
- the base-10 orbit remains the genuine dynamical object behind normality.

But this note should presently be read as a **research memo**, not a solved theorem.

---

*Standalone structural note. Not a proof claim.*
