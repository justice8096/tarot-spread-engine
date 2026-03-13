"""Year Ahead spread — 13 cards, one per month plus a theme card."""

from ..models import SpreadDefinition, SpreadPosition

_MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December",
]

# Arrange 12 months in a clock-like circle with theme card in center
_positions = [
    SpreadPosition(
        index=0,
        name="Theme",
        meaning="The overarching theme and energy for the year",
        x=0.5, y=0.5,
    ),
]

import math
for i, month in enumerate(_MONTHS):
    angle = (i / 12) * 2 * math.pi - math.pi / 2  # Start from top (12 o'clock)
    x = 0.5 + 0.4 * math.cos(angle)
    y = 0.5 + 0.4 * math.sin(angle)
    _positions.append(
        SpreadPosition(
            index=i + 1,
            name=month,
            meaning=f"Energy and themes for {month}",
            x=x, y=y,
        )
    )

YEAR_AHEAD = SpreadDefinition(
    name="Year Ahead",
    description="A 13-card spread with one card per month plus a central theme card. "
    "Provides a roadmap for the year ahead.",
    card_count=13,
    positions=_positions,
    categories=["general", "spiritual"],
)
