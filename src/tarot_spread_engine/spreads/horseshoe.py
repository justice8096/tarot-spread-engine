"""Horseshoe spread — 7 cards in a horseshoe arc."""

from ..models import SpreadDefinition, SpreadPosition

HORSESHOE = SpreadDefinition(
    name="Horseshoe",
    description="A 7-card spread arranged in a horseshoe pattern. Covers the past, present, "
    "hidden influences, the querent, attitudes of others, what should be done, and the outcome.",
    card_count=7,
    positions=[
        SpreadPosition(0, "Past", "Past influences on the situation",
                        x=0.1, y=0.7),
        SpreadPosition(1, "Present", "The current state of affairs",
                        x=0.2, y=0.4),
        SpreadPosition(2, "Hidden Influences", "Unseen forces at work",
                        x=0.35, y=0.2),
        SpreadPosition(3, "The Querent", "You and your role in this",
                        x=0.5, y=0.15),
        SpreadPosition(4, "Others", "How others see the situation",
                        x=0.65, y=0.2),
        SpreadPosition(5, "Action", "What should be done",
                        x=0.8, y=0.4),
        SpreadPosition(6, "Outcome", "The likely result",
                        x=0.9, y=0.7),
    ],
    categories=["general", "career", "finance"],
)
