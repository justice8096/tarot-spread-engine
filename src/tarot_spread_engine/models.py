"""Data models for spreads and drawn cards."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from tarot_deck_reader import Card, Orientation


@dataclass(frozen=True)
class SpreadPosition:
    """A position in a spread layout."""
    index: int
    name: str
    meaning: str
    x: float  # Normalized 0-1 for rendering
    y: float
    rotation: float = 0.0  # Degrees


@dataclass(frozen=True)
class SpreadDefinition:
    """Defines a spread type."""
    name: str
    description: str
    card_count: int
    positions: list[SpreadPosition]
    categories: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class DrawnCard:
    """A card drawn into a specific spread position."""
    card: Card
    orientation: Orientation
    position: SpreadPosition


@dataclass(frozen=True)
class SpreadResult:
    """The complete result of a spread drawing."""
    spread: SpreadDefinition
    drawn_cards: list[DrawnCard]
    question: str | None = None
    timestamp: datetime = field(default_factory=datetime.now)
    seed: int | None = None
