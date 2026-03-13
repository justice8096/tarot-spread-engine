"""Three card spread."""

from ..models import SpreadDefinition, SpreadPosition

THREE_CARD = SpreadDefinition(
    name="Three Card",
    description="A versatile three-card spread. Positions can represent "
    "mind/body/spirit, situation/action/outcome, or any triad.",
    card_count=3,
    positions=[
        SpreadPosition(0, "First", "The first aspect", x=0.2, y=0.5),
        SpreadPosition(1, "Second", "The second aspect", x=0.5, y=0.5),
        SpreadPosition(2, "Third", "The third aspect", x=0.8, y=0.5),
    ],
    categories=["general", "love", "career", "health"],
)
