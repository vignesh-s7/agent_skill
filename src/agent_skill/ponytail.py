"""agent_skill.ponytail - Pure Python implementation of the Ponytail B.U.I.L.D scoring and pre-build ladder.

Origin: https://github.com/dietrichgebert/ponytail
License: MIT License

Methodology:
- Code is liability unless strictly justified by residual gap.
- Smallest change outranks big change; reuse outranks new builds.
- Evaluates proposals against B.U.I.L.D (Borrow, Upgrade, Innovate, Later, Drop).
"""

from __future__ import annotations

import hashlib
from typing import Any, Dict


def score_build(value: int, effort: int) -> Dict[str, Any]:
    """Score a proposal against the B.U.I.L.D reuse ladder.

    Scale:
    - value: 1 (lowest ROI) to 5 (highest value)
    - effort: 1 (lowest friction/hours) to 5 (highest complexity/weeks)
    """
    if not (1 <= value <= 5):
        raise ValueError("value must be an integer between 1 and 5")
    if not (1 <= effort <= 5):
        raise ValueError("effort must be an integer between 1 and 5")

    if value >= 4 and effort <= 2:
        category = "B"
        action = "BORROW"
        recommendation = "Assemble existing stdlib, APIs, or proven tools. Zero new code."
        proceed = True
    elif value >= 4 and effort == 3:
        category = "U"
        action = "UPGRADE"
        recommendation = "Extend or configure existing contracts; never rebuild."
        proceed = True
    elif value >= 4 and effort >= 4:
        category = "I"
        action = "INNOVATE"
        recommendation = "Build only the proven differentiating residual gap."
        proceed = True
    elif value <= 3 and effort >= 4:
        category = "L"
        action = "LATER"
        recommendation = "Defer proposal. Value does not justify effort."
        proceed = False
    else:
        category = "D"
        action = "DROP"
        recommendation = "Reject maintenance weight and low ROI."
        proceed = False

    receipt = hashlib.sha256(f"ponytail-score:{category}:{value}:{effort}".encode("utf-8")).hexdigest()

    return {
        "category": category,
        "action": action,
        "value": value,
        "effort": effort,
        "proceed": proceed,
        "recommendation": recommendation,
        "receipt": receipt,
    }
