#!/usr/bin/env python3
"""Mechanical English replacements only (no network)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "domains"
TARGETS = [ROOT / "data-analytics", ROOT / "devops-cloud", ROOT / "education"]

# imported from _translate_three_domains_once - PLAIN list
from _translate_three_domains_once import PLAIN  # noqa: E402 - won't work as module