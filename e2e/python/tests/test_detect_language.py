"""Test that detect_language is exposed in the public API."""

from tree_sitter_language_pack import detect_language


def test_detect_language_returns_language_for_known_extension():
    assert detect_language("main.py") == "python"


def test_detect_language_returns_none_for_unknown():
    assert detect_language("Makefile") is None
