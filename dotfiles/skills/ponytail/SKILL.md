---
name: ponytail
description: Minimum-build reuse ladder and B.U.I.L.D scoring framework prioritizing Borrow and Upgrade over novel builds.
license: MIT
---

# Ponytail — Minimum-Build Ladder

**Origin:** https://github.com/dietrichgebert/ponytail  
**License:** MIT License  

## Summary
Ponytail enforces a strict pre-build discipline: **code is a liability unless it preserves unique, irreplaceable value.** Proposals must prove that existing tools, stdlib components, and contracts cannot solve the requirement before any novel code is authorized.

## The B.U.I.L.D Scoring Framework
1. **B (Borrow — Value 4–5, Effort 1–2)**: Assemble existing stdlib, package dependencies, or public APIs.
2. **U (Upgrade — Value 4–5, Effort 3)**: Extend or configure existing contracts; avoid rebuilds.
3. **I (Innovate — Value 4–5, Effort 4–5)**: Build only the proven differentiating residual gap.
4. **L (Later — Value 1–3, Effort 4–5)**: Defer and document rationale.
5. **D (Drop — Value 1–2, any effort)**: Reject low-ROI feature weight immediately.

Any proposal scoring `L` or `D` is rejected at the gate.
