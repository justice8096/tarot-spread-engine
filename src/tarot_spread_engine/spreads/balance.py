"""Balance spread — I-Ching inspired dual-polarity reading.

This spread is designed to work with the deck's three orientations
(upright/reversed/between) as a yin-yang-harmony triad, aligning
with the I-Ching balance model referenced in the project philosophy.
"""

from ..models import SpreadDefinition, SpreadPosition

BALANCE = SpreadDefinition(
    name="Balance",
    description="An I-Ching inspired 8-card spread exploring opposing forces and their "
    "resolution. Examines the active and receptive aspects of a situation, "
    "their interplay, and the path to harmony.",
    card_count=8,
    positions=[
        # Yang (active) column
        SpreadPosition(0, "Yang Essence", "The active, assertive force at play",
                        x=0.2, y=0.25),
        SpreadPosition(1, "Yang Expression", "How this active force manifests",
                        x=0.2, y=0.55),

        # Yin (receptive) column
        SpreadPosition(2, "Yin Essence", "The receptive, yielding force at play",
                        x=0.8, y=0.25),
        SpreadPosition(3, "Yin Expression", "How this receptive force manifests",
                        x=0.8, y=0.55),

        # Center (interaction)
        SpreadPosition(4, "Tension", "Where the forces create friction",
                        x=0.5, y=0.2),
        SpreadPosition(5, "Synergy", "Where the forces complement each other",
                        x=0.5, y=0.45),

        # Resolution
        SpreadPosition(6, "Transformation", "The change that wants to happen",
                        x=0.5, y=0.7),
        SpreadPosition(7, "Harmony", "The balanced state being sought",
                        x=0.5, y=0.9),
    ],
    categories=["spiritual", "decision", "general"],
)
