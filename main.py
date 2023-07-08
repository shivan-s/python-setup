"""Example code using httpx and pytest."""

import httpx
import pytest


def main() -> int:
    """Enter main function."""
    URL = "https://shivan.xyz"
    response = httpx.get(URL)
    return response.status_code


def main_fail() -> int:
    """Enter main fail function."""
    URL = "https://shivan.xyz/doesnotexist"
    response = httpx.get(URL)
    return response.status_code


@pytest.mark.anyio
def test_main():
    """Test the main function."""
    assert main() == 200


@pytest.mark.anyio
def test_main_fail():
    """Test the main function."""
    assert main_fail() == 404
