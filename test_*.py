- name: Test with pytest
  run: |
    pytest tests/
- name: Debug pytest discovery
  run: |
    pytest --collect-only

import pytest

def test_example():
    assert 1 + 1 == 2

def test_annotation() -> None:
    x: int = 5  # Correct annotation
    assert x == 5
