"""Relationship spread — 7 cards for exploring a partnership."""

from ..models import SpreadDefinition, SpreadPosition

RELATIONSHIP = SpreadDefinition(
    name="Relationship Spread",
    description="A 7-card spread exploring the dynamics between two people. "
    "Covers each person's perspective, the relationship's foundation, "
    "challenges, strengths, and potential.",
    card_count=7,
    positions=[
        SpreadPosition(0, "You", "How you see yourself in this relationship", x=0.2, y=0.3),
        SpreadPosition(1, "Partner", "How your partner sees themselves", x=0.8, y=0.3),
        SpreadPosition(2, "Your View of Partner", "How you see your partner", x=0.2, y=0.6),
        SpreadPosition(3, "Partner's View of You", "How your partner sees you", x=0.8, y=0.6),
        SpreadPosition(4, "Foundation", "The foundation of the relationship", x=0.5, y=0.8),
        SpreadPosition(5, "Challenge", "The main challenge to overcome", x=0.5, y=0.5),
        SpreadPosition(6, "Potential", "The relationship's potential", x=0.5, y=0.2),
    ],
    categories=["love"],
)
