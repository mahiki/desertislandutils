#!/usr/bin/env bash
cat << EOF
REMINDER: You need to manually bump the version numbers in these locations.
tests/test_desertislandutils.py
desertislandutils/__init__.py
pyproject.toml
EOF
