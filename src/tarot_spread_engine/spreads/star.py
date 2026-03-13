"""Star spread — 6 cards in a hexagram pattern for spiritual insight."""

from ..models import SpreadDefinition, SpreadPosition

STAR = SpreadDefinition(
    name="Star",
    description="A 6-card spread arranged in a star/hexagram pattern. "
    "Explores spiritual growth, inner truth, challenges, support, "
    "the path forward, and higher purpose.",
    card_count=6,
    positions=[
        SpreadPosition(0, "Higher Self", "Your spiritual essence and potential",
                        x=0.5, y=0.1),
        SpreadPosition(1, "Inner Truth", "What your intuition is telling you",
                        x=0.2, y=0.35),
        SpreadPosition(2, "Support", "What supports your growth",
                        x=0.8, y=0.35),
        SpreadPosition(3, "Challenge", "What tests your spirit",
                        x=0.2, y=0.65),
        SpreadPosition(4, "Path Forward", "The way ahead",
                        x=0.8, y=0.65),
        SpreadPosition(5, "Integration", "How to bring it all together",
                        x=0.5, y=0.85),
    ],
    categories=["spiritual"],
)
