"""Past, Present, Future spread."""

from ..models import SpreadDefinition, SpreadPosition

PAST_PRESENT_FUTURE = SpreadDefinition(
    name="Past Present Future",
    description="Three cards representing past influences, the present situation, "
    "and future possibilities.",
    card_count=3,
    positions=[
        SpreadPosition(0, "Past", "Past influences and events", x=0.2, y=0.5),
        SpreadPosition(1, "Present", "Current situation and energies", x=0.5, y=0.5),
        SpreadPosition(2, "Future", "Potential outcomes and direction", x=0.8, y=0.5),
    ],
    categories=["general", "career", "spiritual"],
)
