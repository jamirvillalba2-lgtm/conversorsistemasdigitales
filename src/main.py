"""
Punto de entrada de la aplicación.
Incluye soporte para escalado de alta densidad de píxeles (High DPI) en Windows.
"""

import sys
import os
import ctypes
from interfaz import iniciar_aplicacion


def habilitar_soporte_high_dpi() -> None:
    """Configura el escalado nativo para pantallas de alta resolución en Windows."""
    if sys.platform == "win32":
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass  # Failsafe para versiones antiguas de Windows


if __name__ == "__main__":
    habilitar_soporte_high_dpi()
    iniciar_aplicacion()