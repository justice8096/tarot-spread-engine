"""Celtic Cross — the classic 10-card spread."""

from ..models import SpreadDefinition, SpreadPosition

CELTIC_CROSS = SpreadDefinition(
    name="Celtic Cross",
    description="The classic 10-card spread for comprehensive insight into a situation. "
    "Covers the present, challenges, past, future, conscious, subconscious, "
    "advice, external influences, hopes/fears, and outcome.",
    card_count=10,
    positions=[
        SpreadPosition(0, "Present", "The current situation", x=0.35, y=0.5),
        SpreadPosition(1, "Challenge", "The immediate challenge or crossing energy",
                        x=0.35, y=0.5, rotation=90.0),
        SpreadPosition(2, "Foundation", "The root cause or distant past", x=0.35, y=0.8),
        SpreadPosition(3, "Recent Past", "Recent events and influences", x=0.15, y=0.5),
        SpreadPosition(4, "Crown", "Best possible outcome or conscious goal", x=0.35, y=0.2),
        SpreadPosition(5, "Near Future", "What is approaching", x=0.55, y=0.5),
        SpreadPosition(6, "Self", "Your attitude and approach", x=0.75, y=0.8),
        SpreadPosition(7, "Environment", "External influences and others' views", x=0.75, y=0.6),
        SpreadPosition(8, "Hopes and Fears", "Your hopes and fears about the outcome",
                        x=0.75, y=0.4),
        SpreadPosition(9, "Outcome", "The likely outcome", x=0.75, y=0.2),
    ],
    categories=["general", "love", "career", "finance", "spiritual"],
)
