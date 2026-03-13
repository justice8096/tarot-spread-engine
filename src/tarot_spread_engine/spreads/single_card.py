"""Single card draw."""

from ..models import SpreadDefinition, SpreadPosition

SINGLE_CARD = SpreadDefinition(
    name="Single Card",
    description="A single card draw for quick insight or daily guidance.",
    card_count=1,
    positions=[
        SpreadPosition(0, "The Card", "Your message for now", x=0.5, y=0.5),
    ],
    categories=["general", "spiritual", "daily"],
)
