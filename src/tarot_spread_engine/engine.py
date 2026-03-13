"""Spread engine — draws cards for a spread."""

from __future__ import annotations

import random
from datetime import datetime

from tarot_deck_reader import Card, Deck, Orientation

from .models import DrawnCard, SpreadDefinition, SpreadResult
from .spreads import ALL_SPREADS, SPREAD_BY_NAME

# Default orientation weights: "between" is rarer than upright/reversed
DEFAULT_WEIGHTS: dict[Orientation, float] = {
    Orientation.UPRIGHT: 0.4,
    Orientation.REVERSED: 0.4,
    Orientation.BETWEEN: 0.2,
}


class SpreadEngine:
    """Draws cards from a deck for a given spread."""

    def __init__(self, deck: Deck, rng: random.Random | None = None) -> None:
        self.deck = deck
        self.rng = rng or random.Random()

    def draw(
        self,
        spread: SpreadDefinition | str,
        question: str | None = None,
        orientation_weights: dict[Orientation, float] | None = None,
        exclude_cards: list[str] | None = None,
        seed: int | None = None,
    ) -> SpreadResult:
        """Draw cards for the given spread.

        Args:
            spread: A SpreadDefinition or the name of a built-in spread.
            question: The user's question (optional, stored in result).
            orientation_weights: Weight per orientation for random selection.
            exclude_cards: Card names to exclude from the draw.
            seed: Random seed for reproducibility.

        Returns:
            A SpreadResult with all drawn cards.
        """
        if isinstance(spread, str):
            if spread not in SPREAD_BY_NAME:
                raise ValueError(
                    f"Unknown spread '{spread}'. "
                    f"Available: {list(SPREAD_BY_NAME.keys())}"
                )
            spread = SPREAD_BY_NAME[spread]

        if seed is not None:
            self.rng.seed(seed)

        weights = orientation_weights or DEFAULT_WEIGHTS
        excluded = set(exclude_cards or [])

        # Build candidate pool
        candidates = [c for c in self.deck.cards if c.name not in excluded]

        if len(candidates) < spread.card_count:
            raise ValueError(
                f"Not enough cards in deck ({len(candidates)}) "
                f"for spread '{spread.name}' ({spread.card_count} needed)."
            )

        # Draw without replacement
        selected = self.rng.sample(candidates, spread.card_count)

        drawn_cards: list[DrawnCard] = []
        for card, position in zip(selected, spread.positions):
            orientation = self._pick_orientation(card, weights)
            drawn_cards.append(DrawnCard(card=card, orientation=orientation, position=position))

        return SpreadResult(
            spread=spread,
            drawn_cards=drawn_cards,
            question=question,
            timestamp=datetime.now(),
            seed=seed,
        )

    def _pick_orientation(
        self, card: Card, weights: dict[Orientation, float]
    ) -> Orientation:
        """Pick a random orientation, respecting weights and available orientations."""
        available = card.orientations
        available_weights = [weights.get(o, 0.0) for o in available]
        total = sum(available_weights)
        if total == 0:
            return self.rng.choice(available)
        return self.rng.choices(available, weights=available_weights, k=1)[0]

    def available_spreads(self) -> list[SpreadDefinition]:
        """Return all registered spread definitions."""
        return list(ALL_SPREADS)

    def get_spread(self, name: str) -> SpreadDefinition:
        """Look up a spread by name."""
        if name not in SPREAD_BY_NAME:
            raise KeyError(
                f"Spread '{name}' not found. "
                f"Available: {list(SPREAD_BY_NAME.keys())}"
            )
        return SPREAD_BY_NAME[name]
