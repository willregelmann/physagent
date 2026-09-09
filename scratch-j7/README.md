# scratch/j7 — J-7a: the fourth-order boundary problems, defined (2026-09-08)

Working-memory record for `programs/no-boundary-junction/notes/2026-09-08-j7a-boundary-problems-defined.md` (issue #215).
Never merged, never deleted (AUTONOMY.md, explorer scratch tier). Scripts import the J-6 machinery
(`ccaps.py`, steelman H's `invariant.py`) from `scratch/j6/2026-09-06-saddle-debate-scripts`.

- `j7/ostro.py`, `hj_check.py` — Ostrogradsky momenta of the ESU-frame Lagrangian (C = 8), Hamilton–Jacobi test of position T's cut-sphere action, the fixed-(a,R) boundary term of the ESU scheme, the sharp-cone log coefficient.
- `j7/hjcheck.py` — Hamilton–Jacobi verification that I_inv is the fixed-(a,v) action with Q = (ε/4)a²R, P = p_a^{ESU} (8 points).
- `j7/ar_table.py`, `qcross.py` — fixed-(q,R) comparison with the R²-GHY boundary term: ε table, crossover ε* = 0.3304, q*(ε).
- `j7/vfamily.py`, `vfine.py` — the real regular-cap family at a = 2 and the two Laplace-transform exponents.
- `j7/av_table.py`, `av_fix.py` — fixed-(a,v) census (3, −i√8) re-evaluated with I_inv; gauge repair for the six failures; complex-pair continuation.
- `j7/cone_num.py` — smoothed-cone action, numerical confirmation of the log coefficient.
- `j7/aR_onshell.py`, `kzero_caps.py` — on-shell fixed-(a,R) action along the real family; the K = 0 turning-point caps at fixed radius (R-marginal saddles).
- `j7/av_six.py` — gauge repair + constant-lapse test for the six census saddles the real-seed secant could not gauge.
- `j7/attack-j7a.md` with `atk_hj_fine.py`, `atk_family.py`, `atk_cone.py`, `atk_census.py` — attack pass (18 items).
- `j7/steelman-j7a.md` with `stm_cone.py`, `stm_aR_onshell.py`, `stm_lapse_census.py`, `stm_complex_caps.py`, `stm_complex_caps_lapse0.py`, `stm_pair.py`, `stm_pair2.py` — steelman pass (per-flaw verdicts, corrected statements).
- `j7/dh09.txt`, `fs95.txt`, `hhj15.txt` — pdftotext extracts of Dyer–Hinterbichler 2009, Fursaev–Solodukhin 1995, Herzog–Huang–Jensen 2015 used for passage-level citation verification.
