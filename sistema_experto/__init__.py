"""Paquete del sistema experto de productividad personal."""

from .hechos import obtener_hechos_iniciales
from .motor_inferencia import evaluar_sistema_experto
from .reglas import REGLAS

__all__ = [
    "obtener_hechos_iniciales",
    "evaluar_sistema_experto",
    "REGLAS",
]
