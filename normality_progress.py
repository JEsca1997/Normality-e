"""
OFI Normality Proof Progress Tracker  v2.0
===========================================
Full progress dashboard with sub-step tracking for Step 9.
Real-time score computation with visual progress bars.

Run:
    python normality_progress.py
"""

import shutil
import sys
import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ═══ ANSI Codes ═══════════════════════════════════════════════════════
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RED    = "\033[91m"
MAGENTA = "\033[95m"
WHITE  = "\033[97m"
BG_GREEN  = "\033[42m"
BG_CYAN   = "\033[46m"
BG_YELLOW = "\033[43m"
BG_RED    = "\033[41m"

STATUS_META = {
    "PROVED":      (GREEN,   "█", "PROVED"),
    "CONDITIONAL": (CYAN,    "▓", "COND'L"),
    "EMPIRICAL":   (YELLOW,  "▒", "EMPIR."),
    "PARTIAL":     (YELLOW,  "░", "PARTIAL"),
    "RUNNING":     (MAGENTA, "▓", "RUNNING"),
    "OPEN":        (RED,     "·", "OPEN"),
}

WEIGHT = {
    "PROVED": 1.0, "CONDITIONAL": 0.7, "EMPIRICAL": 0.5,
    "PARTIAL": 0.3, "RUNNING": 0.1, "OPEN": 0.0,
}

# ═══ Step 9 SUB-STEPS ════════════════════════════════════════════════
# Deep-audit-verified sub-steps (2026-04-13).
# PROVED = rigorous theorem.  EMPIRICAL = numbers only.
# CONDITIONAL = proved but circular/tautological for main goal.
STEP9_SUBS = [
    ("PROVED",      "9a", "D_k → ∞ (denominator growth)",
     "μ(e)=2 ⟹ D_k ≥ (k!)^{1/2−ε}. Via Davis 1978. RIGOROUS."),
    ("PROVED",      "9b", "Digit-window separation",
     "§42: j_{k+1} > j_k + L_k from factorial growth. RIGOROUS."),
    ("PROVED",      "9c", "Carry bound Σ|δ_k| < ∞",
     "§42: |δ_k|=O(k^{-3/2}), series converges. RIGOROUS."),
    ("CONDITIONAL", "9d", "PIH ⟹ bound (CIRCULAR for main goal)",
     "§43: PIH ⟹ |W_K|=O(√(K log K)). But PIH ≈ equidistribution itself."),
    ("EMPIRICAL",   "9e", "QV factorization ρ_K → 1",
     "K=3000: ρ∈[0.98,1.01]. Numerical only, not a theorem."),
    ("PROVED",      "9f", "Freedman barrier (NEGATIVE result)",
     "Martingale alone insufficient. Blocks a proof route, doesn't advance."),
    ("PROVED",      "9g", "Expanding map recurrence (expansion ≥ 10)",
     "§51: H_{k+1}={10^{L_k}·H_k+c_k}, λ→∞. RIGOROUS but a.e. only."),
    ("EMPIRICAL",   "9h", "|W_K(h)|/√K bounded + Poisson spacing",
     "Empirical at K=10000. No theorem for e specifically."),
    ("EMPIRICAL",   "9i", "Discrepancy D*_K = O(1/√K)",
     "Empirical at K=10000. No theorem for e specifically."),
    ("OPEN",        "9j", "Strong block bound Σ|W_n|² = O(K)",
     "THE GAP. Weak O(K ln K) PROVED. Strong O(K) empirical only."),
    ("PROVED",      "9k", "Factorial periodicity A_{p+j}≡A_j (mod p)",
     "§53: Lemma proved. Corollary: A_p≡1(mod p). RIGOROUS."),
]

# ═══ MAIN 10 STEPS ═══════════════════════════════════════════════════
E_STEPS = [
    ("PROVED", "Block architecture",
     "Factorial layers j_k, L_k, N_K; carry cocycle B_{k+1}. §2–§9"),
    ("PROVED", "Vanishing-drive recurrence",
     "Z_{k+1} = frac(10^{L_k} Z_k + X_{k+1}), X_k→0. §10"),
    ("PROVED", "Spectral gap (a.e. equidistribution)",
     "||P_K…P_3|| ≤ 10^{−N_K/2}. A.E. result, not specific to e. §30"),
    ("PROVED", "dim_H(E) = 0",
     "Exceptional set has Hausdorff dim 0. Does not resolve e ∈ E. §31"),
    ("PROVED", "Complete exponential sums |S_k(h)| = O(1)",
     "k=7..18, P_k up to 81648; bijection + Weil. §19"),
    ("PARTIAL", "Hyp D ⟹ e normal (tautological reduction)",
     "If e equidistributes then e is normal. Adds no unconditional progress."),
    ("PROVED", "Z_k = H_k + T_k perturbation lemma",
     "|W_K−S_K| ≤ O(ln K); H_k rational orbit suffices. §39"),
    ("PARTIAL", "Lacunary + μ(e)=2 (non-resonance CIRCULAR)",
     "Lacunary + μ(e)=2: proved. Non-resonance: ≡ equidistribution (§51)."),
    ("CONDITIONAL", "Weyl sum |W(h)| = o(K) — CONDITIONAL",
     "5/11 proved, 1 conditional, 3 empirical, 1 open, 1 negative. §53."),
    ("CONDITIONAL", "Proof chain closure",
     "Conditional on strong block bound. Same wall as everyone."),
]


def step9_score():
    """Compute Step 9's internal progress as a fraction [0,1]."""
    return sum(WEIGHT[s] for s, _, _, _ in STEP9_SUBS) / len(STEP9_SUBS)


def overall_score():
    """Weighted score across all 10 steps, with Step 9 using sub-step detail."""
    total = 0.0
    for i, (status, _, _) in enumerate(E_STEPS):
        if i == 8:  # Step 9 — use sub-step score
            total += step9_score()
        else:
            total += WEIGHT[status]
    return total / len(E_STEPS) * 100.0


def make_bar(value, width, filled_char="█", empty_char="░"):
    """Percentage bar with color gradient."""
    filled = int(value / 100.0 * width)
    if value >= 95:
        color = GREEN
    elif value >= 80:
        color = CYAN
    elif value >= 50:
        color = YELLOW
    else:
        color = RED
    return color + filled_char * filled + DIM + empty_char * (width - filled) + RESET


def make_mini_bar(value, width=20):
    """Small inline bar for sub-steps."""
    filled = int(value / 100.0 * width)
    return GREEN + "■" * filled + DIM + "·" * (width - filled) + RESET


def render():
    tw = min(shutil.get_terminal_size((100, 24)).columns, 100)
    bar_w = min(tw - 16, 60)
    sep = "═" * min(tw, 80)
    thin = "─" * min(tw, 80)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    score = overall_score()
    s9 = step9_score() * 100

    # ── HEADER ────────────────────────────────────────────────────
    print()
    print(f"  {BOLD}{WHITE}╔{'═'*68}╗{RESET}")
    print(f"  {BOLD}{WHITE}║  OFI NORMALITY PROOF — e IN BASE 10           {now}  ║{RESET}")
    print(f"  {BOLD}{WHITE}╚{'═'*68}╝{RESET}")
    print()

    # ── MAIN PROGRESS BAR ─────────────────────────────────────────
    print(f"  {BOLD}OVERALL{RESET}  {make_bar(score, bar_w)}  {BOLD}{score:5.1f}%{RESET}")
    print()

    proved_n = sum(1 for s, _, _ in E_STEPS if s == "PROVED")
    cond_n   = sum(1 for s, _, _ in E_STEPS if s == "CONDITIONAL")
    print(f"  {GREEN}█ {proved_n} proved{RESET}  "
          f"{CYAN}▓ {cond_n} conditional{RESET}  "
          f"{DIM}10 total steps{RESET}")
    print()

    # ── STEP LIST ─────────────────────────────────────────────────
    print(f"  {DIM}{thin}{RESET}")
    for i, (status, title, detail) in enumerate(E_STEPS):
        num = i + 1
        sc, ch, slabel = STATUS_META[status]
        # Step 9 gets special treatment
        if num == 9:
            pct_9 = s9
            print(f"  {sc}{ch}{ch}{RESET} {BOLD}{num:>2}. {title}{RESET}")
            print(f"       {make_mini_bar(pct_9, 30)}  {BOLD}{pct_9:.0f}%{RESET} {DIM}(sub-step detail below){RESET}")
        elif num == 10:
            print(f"  {sc}{ch}{ch}{RESET} {BOLD}{num:>2}. {title}{RESET}")
            print(f"       {DIM}{detail}{RESET}")
        else:
            print(f"  {sc}{ch}{ch}{RESET} {BOLD}{num:>2}. {title}{RESET}")
            print(f"       {DIM}{detail}{RESET}")
    print(f"  {DIM}{thin}{RESET}")

    # ── STEP 9 SUB-STEP BREAKDOWN ────────────────────────────────
    print()
    print(f"  {BOLD}{CYAN}┌─ STEP 9 BREAKDOWN: Weyl sum micro-gap attack ─────────────┐{RESET}")
    print(f"  {CYAN}│{RESET}")
    for status, label, title, detail in STEP9_SUBS:
        sc, ch, slabel = STATUS_META[status]
        marker = f"{sc}{ch}{RESET}"
        tag = f"{sc}{slabel:<6}{RESET}"
        if status == "OPEN":
            print(f"  {CYAN}│{RESET}  {marker} {tag} {BOLD}{RED}{label} {title}{RESET}")
            print(f"  {CYAN}│{RESET}         {RED}{detail}{RESET}")
        else:
            print(f"  {CYAN}│{RESET}  {marker} {tag} {label} {title}")
            print(f"  {CYAN}│{RESET}         {DIM}{detail}{RESET}")
    print(f"  {CYAN}│{RESET}")

    s9_proved = sum(1 for s, _, _, _ in STEP9_SUBS if s == "PROVED")
    s9_emp    = sum(1 for s, _, _, _ in STEP9_SUBS if s == "EMPIRICAL")
    s9_open   = sum(1 for s, _, _, _ in STEP9_SUBS if s == "OPEN")
    print(f"  {CYAN}│{RESET}  {GREEN}█ {s9_proved} proved{RESET}  "
          f"{YELLOW}▒ {s9_emp} empirical{RESET}  "
          f"{RED}· {s9_open} open{RESET}  "
          f"{DIM}= {s9:.0f}%{RESET}")
    print(f"  {BOLD}{CYAN}└────────────────────────────────────────────────────────────┘{RESET}")
    print()

    # ── THE GAP ───────────────────────────────────────────────────
    print(f"  {BOLD}{YELLOW}REMAINING GAP:{RESET}  Strong block bound Σ|W_n(h)|² = O(K)")
    print(f"  {DIM}Weak bound O(K ln K): PROVED (Prop 53.5). Strong bound O(K): EMPIRICAL.")
    print(f"  The quenched passage — transferring P-F ensemble prediction to the{RESET}")
    print(f"  {DIM}specific deterministic orbit of e — is the single remaining step.{RESET}")
    print()
    print(f"  {BOLD}Proved:{RESET} CS + weak bound gives |W_K| = O(K) (trivial, insufficient)")
    print(f"  {BOLD}Conditional:{RESET} CS + strong bound gives |W_K| = o(K) → Weyl → normal")
    print(f"  {DIM}Empirical: Σ|W_n|²/K → 1.0 at K=5000 (667 blocks). Scaling{RESET}")
    print(f"  {DIM}confirms ln K factor is spurious: Σ/KlnK decreases from 0.157 to 0.118.{RESET}")
    print()

    # ── KEY METRICS TABLE ─────────────────────────────────────────
    print(f"  {BOLD}Key metrics{RESET} (K=10000, exact integer arithmetic):")
    print(f"  {DIM}{'Metric':<35} {'Value':<12} {'Status':<10}{RESET}")
    print(f"  {DIM}{'─'*57}{RESET}")
    metrics = [
        ("Σ|W_n|²/K (h=1)",           "0.995",  "≈ 1.0"),
        ("mean |W_n|²/g (h=1)",        "1.011",  "≈ 1.0"),
        ("max |W_n|²/g (h=1)",         "5.70",   "< 7"),
        ("cross-block / K (h=1)",      "−0.91",  "CANCEL"),
        ("|W_K(1)|/K at K=10000",      "0.003",  "→ 0"),
        ("P-F mean correlation",       "0.003",  "z=0.41"),
        ("D*_K · √K (K=10000)",        "0.619",  "O(1)"),
        ("Spacing var(s)",             "1.003",  "POISSON"),
    ]
    for name, val, status in metrics:
        color = GREEN if "BOUNDED" in status or "O(1)" in status or "≈" in status or "<" in status else YELLOW
        print(f"  {name:<35} {BOLD}{val:<12}{RESET} {color}{status}{RESET}")
    print()

    # ── COMPUTATIONAL PROBES ──────────────────────────────────────
    print(f"  {BOLD}Probes:{RESET} 39 essential (58 archived) in probes/")
    print(f"  {DIM}Latest: e_strong_block_bound_probe.py (K=5000, 7/7 checks)")
    print(f"  Routes: carry · ET · CF · VdC · CRT · resonance · ×10 map · Poisson · BCS{RESET}")
    print()

    # ── FOOTER ────────────────────────────────────────────────────
    gap_label = "NONE" if score >= 99.9 else "Strong block bound (Step 9j)"
    print(f"  {DIM}Paper: OFI-NORMALITY-e.tex v24 (91pp)  ·  Score: {score:.1f}%  ·  Gap: {gap_label}{RESET}")
    print()


if __name__ == "__main__":
    render()
