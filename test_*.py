- name: Test with pytest
  run: |
    pytest tests/
- name: Debug pytest discovery
  run: |
    pytest --collect-only
