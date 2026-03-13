"""Built-in spread definitions."""

from .celtic_cross import CELTIC_CROSS
from .past_present_future import PAST_PRESENT_FUTURE
from .relationship import RELATIONSHIP
from .single_card import SINGLE_CARD
from .three_card import THREE_CARD
from .two_paths import TWO_PATHS

ALL_SPREADS = [
    SINGLE_CARD,
    THREE_CARD,
    PAST_PRESENT_FUTURE,
    CELTIC_CROSS,
    RELATIONSHIP,
    TWO_PATHS,
]

SPREAD_BY_NAME = {s.name: s for s in ALL_SPREADS}

__all__ = [
    "ALL_SPREADS",
    "CELTIC_CROSS",
    "PAST_PRESENT_FUTURE",
    "RELATIONSHIP",
    "SINGLE_CARD",
    "SPREAD_BY_NAME",
    "THREE_CARD",
    "TWO_PATHS",
]
