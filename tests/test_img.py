#!/usr/bin/env python3

"""Provides test cases for webexmemebot/img.py."""

import pytest

from app import img  # pragma: no cover


def test_get_templates() -> None:
    """Test to ensure that we can successfully contact the API."""
    result = img.get_templates()
    assert isinstance(result, list) and isinstance(result[0], dict)


@pytest.mark.parametrize("test_input,expected", img.CHAR_REPLACEMENTS)
def test_format_meme_string(test_input, expected):
    """Test to ensure we correctly reformat special chars in the meme URL."""
    test_str: str = f"abc{test_input}123"
    assert img.format_meme_string(test_str) == f"abc{expected}123"
