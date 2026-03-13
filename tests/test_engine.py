"""Tests for the spread engine."""

from pathlib import Path

import pytest

from tarot_deck_reader import Deck, Orientation, load_deck
from tarot_spread_engine import SpreadEngine, SpreadResult

DECK_JSON = Path("D:/data/cards/Standard/Deck.json")


@pytest.fixture(scope="module")
def deck() -> Deck:
    return load_deck(DECK_JSON)


@pytest.fixture
def engine(deck: Deck) -> SpreadEngine:
    return SpreadEngine(deck)


class TestDrawing:
    def test_single_card(self, engine: SpreadEngine) -> None:
        result = engine.draw("Single Card")
        assert len(result.drawn_cards) == 1
        assert result.spread.name == "Single Card"

    def test_three_card(self, engine: SpreadEngine) -> None:
        result = engine.draw("Three Card")
        assert len(result.drawn_cards) == 3

    def test_celtic_cross(self, engine: SpreadEngine) -> None:
        result = engine.draw("Celtic Cross")
        assert len(result.drawn_cards) == 10

    def test_no_duplicate_cards(self, engine: SpreadEngine) -> None:
        result = engine.draw("Celtic Cross")
        card_names = [dc.card.name for dc in result.drawn_cards]
        assert len(card_names) == len(set(card_names))

    def test_positions_match_spread(self, engine: SpreadEngine) -> None:
        result = engine.draw("Celtic Cross")
        for dc in result.drawn_cards:
            assert dc.position in result.spread.positions


class TestReproducibility:
    def test_seed_produces_same_result(self, engine: SpreadEngine) -> None:
        r1 = engine.draw("Three Card", seed=42)
        r2 = engine.draw("Three Card", seed=42)
        names1 = [(dc.card.name, dc.orientation) for dc in r1.drawn_cards]
        names2 = [(dc.card.name, dc.orientation) for dc in r2.drawn_cards]
        assert names1 == names2


class TestOrientation:
    def test_orientations_are_valid(self, engine: SpreadEngine) -> None:
        result = engine.draw("Celtic Cross", seed=123)
        for dc in result.drawn_cards:
            assert dc.orientation in dc.card.orientations


class TestQuestion:
    def test_question_stored(self, engine: SpreadEngine) -> None:
        result = engine.draw("Single Card", question="What should I focus on?")
        assert result.question == "What should I focus on?"


class TestErrors:
    def test_unknown_spread_name(self, engine: SpreadEngine) -> None:
        with pytest.raises(ValueError, match="Unknown spread"):
            engine.draw("Nonexistent Spread")

    def test_available_spreads(self, engine: SpreadEngine) -> None:
        spreads = engine.available_spreads()
        assert len(spreads) >= 6
        names = [s.name for s in spreads]
        assert "Celtic Cross" in names
        assert "Single Card" in names
