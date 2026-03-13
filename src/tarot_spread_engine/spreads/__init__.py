"""Built-in spread definitions."""

from .balance import BALANCE
from .celtic_cross import CELTIC_CROSS
from .horseshoe import HORSESHOE
from .mind_body_spirit import MIND_BODY_SPIRIT
from .past_present_future import PAST_PRESENT_FUTURE
from .relationship import RELATIONSHIP
from .single_card import SINGLE_CARD
from .star import STAR
from .three_card import THREE_CARD
from .two_paths import TWO_PATHS
from .year_ahead import YEAR_AHEAD

ALL_SPREADS = [
    SINGLE_CARD,
    THREE_CARD,
    PAST_PRESENT_FUTURE,
    CELTIC_CROSS,
    HORSESHOE,
    RELATIONSHIP,
    TWO_PATHS,
    STAR,
    BALANCE,
    MIND_BODY_SPIRIT,
    YEAR_AHEAD,
]

SPREAD_BY_NAME = {s.name: s for s in ALL_SPREADS}

__all__ = [
    "ALL_SPREADS",
    "BALANCE",
    "CELTIC_CROSS",
    "HORSESHOE",
    "MIND_BODY_SPIRIT",
    "PAST_PRESENT_FUTURE",
    "RELATIONSHIP",
    "SINGLE_CARD",
    "SPREAD_BY_NAME",
    "STAR",
    "THREE_CARD",
    "TWO_PATHS",
    "YEAR_AHEAD",
]
