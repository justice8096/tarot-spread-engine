"""Two Paths spread — for decision-making between two options."""

from ..models import SpreadDefinition, SpreadPosition

TWO_PATHS = SpreadDefinition(
    name="Two Paths",
    description="A 5-card spread for choosing between two options. "
    "Shows the current situation, where each path leads, "
    "and what each path requires.",
    card_count=5,
    positions=[
        SpreadPosition(0, "Current Situation", "Where you stand now", x=0.5, y=0.8),
        SpreadPosition(1, "Path A", "Where the first option leads", x=0.25, y=0.4),
        SpreadPosition(2, "Path A Requires", "What path A demands of you", x=0.25, y=0.15),
        SpreadPosition(3, "Path B", "Where the second option leads", x=0.75, y=0.4),
        SpreadPosition(4, "Path B Requires", "What path B demands of you", x=0.75, y=0.15),
    ],
    categories=["decision"],
)
