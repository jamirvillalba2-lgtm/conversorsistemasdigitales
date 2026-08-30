"""
Módulo de lógica pura para conversiones numéricas entre distintas bases.
Diseñado sin dependencias de UI para garantizar máxima portabilidad.
"""


def decimal_a_binario(valor: int) -> str:
    """Convierte un entero decimal no negativo a representación binaria."""
    if valor < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    return bin(valor)[2:]


def binario_a_decimal(valor: str) -> int:
    """Convierte una cadena de caracteres binaria a entero decimal."""
    return int(valor, 2)


def decimal_a_octal(valor: int) -> str:
    """Convierte un entero decimal no negativo a representación octal."""
    if valor < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    return oct(valor)[2:]


def octal_a_binario(valor: str) -> str:
    """Convierte una cadena octal a su representación binaria equivalente."""
    decimal = int(valor, 8)
    return bin(decimal)[2:]