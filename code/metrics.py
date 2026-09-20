"""Metric definitions used in the chapter's case study.

Q    : composite image-quality score (Eq. 1)
NCSE : Normalized Cross-Severity Error for ordinal damage levels (Eq. 2)

Run `python code/metrics.py` for a quick self-check.
"""
from __future__ import annotations

from collections.abc import Sequence


def quality_score(contrast: float, sharpness: float, niqe_proxy: float) -> float:
    """Q = 0.4*C + 0.4*S + 0.2*N, with each term already normalized to [0, 1]."""
    return 0.4 * contrast + 0.4 * sharpness + 0.2 * niqe_proxy


def ncse(y_true: Sequence[int], y_pred: Sequence[int], k: int = 3) -> float:
    """Mean absolute severity gap divided by (k - 1).

    Classes are ordered integers 0..k-1 (0 = minor, k-1 = severe).
    0 means perfect agreement; 1 means every prediction sits in the most
    distant class. Adjacent confusions cost 1/(k-1), far ones cost more.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not y_true:
        raise ValueError("empty input")
    total = sum(abs(int(t) - int(p)) for t, p in zip(y_true, y_pred))
    return total / (len(y_true) * (k - 1))


if __name__ == "__main__":
    assert abs(quality_score(1, 1, 1) - 1.0) < 1e-9
    assert ncse([0, 1, 2], [0, 1, 2]) == 0.0
    assert ncse([0, 0, 0], [2, 2, 2]) == 1.0
    assert abs(ncse([0, 1, 2, 2], [1, 1, 2, 0]) - (1 + 0 + 0 + 2) / (4 * 2)) < 1e-9
    print("metrics ok")
