"""Mind, Body, Spirit spread — holistic wellness check."""

from ..models import SpreadDefinition, SpreadPosition

MIND_BODY_SPIRIT = SpreadDefinition(
    name="Mind Body Spirit",
    description="A 5-card spread examining mental, physical, and spiritual wellbeing. "
    "Includes an integration card and guidance card.",
    card_count=5,
    positions=[
        SpreadPosition(0, "Mind", "Your mental state and thought patterns",
                        x=0.2, y=0.3),
        SpreadPosition(1, "Body", "Your physical wellbeing and material world",
                        x=0.5, y=0.3),
        SpreadPosition(2, "Spirit", "Your spiritual connection and inner life",
                        x=0.8, y=0.3),
        SpreadPosition(3, "Integration", "How these aspects interact and influence each other",
                        x=0.5, y=0.6),
        SpreadPosition(4, "Guidance", "What you need to focus on for overall balance",
                        x=0.5, y=0.85),
    ],
    categories=["health", "spiritual", "general"],
)
