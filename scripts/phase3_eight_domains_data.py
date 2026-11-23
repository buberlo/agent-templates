"""Merged Phase-3 template bodies for eight domains."""
from phase3_payload_immobilien import PAYLOAD as IMMO
from phase3_payload_recht_verwaltung import PAYLOAD as RECHT
from phase3_payload_reisen_events import PAYLOAD as REISEN
from phase3_payload_gaming_modding import PAYLOAD as GAMING
from phase3_payload_hardware_embedded import PAYLOAD as HARDWARE
from phase3_payload_gesundheit_fitness import PAYLOAD as GESUND
from phase3_payload_persoenlich_lifestyle import PAYLOAD as LIFESTYLE
from phase3_payload_wissenschaft_engineering import PAYLOAD as WISS

TEMPLATES = {
    **IMMO,
    **RECHT,
    **REISEN,
    **GAMING,
    **HARDWARE,
    **GESUND,
    **LIFESTYLE,
    **WISS,
}

assert len(TEMPLATES) == 32, len(TEMPLATES)