def decimal_a_binario(numero):
    """Convierte un número decimal a binario."""
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado
        numero = numero // 2

    return resultado


def binario_a_decimal(numero):
    """Convierte un número binario a decimal."""
    decimal = 0
    potencia = 0

    for digito in reversed(numero):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    return str(decimal)


def decimal_a_octal(numero):
    """Convierte un número decimal a octal."""
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        residuo = numero % 8
        resultado = str(residuo) + resultado
        numero = numero // 8

    return resultado


def octal_a_binario(numero):
    """Convierte un número octal a binario."""
    tabla = {
        "0": "000",
        "1": "001",
        "2": "010",
        "3": "011",
        "4": "100",
        "5": "101",
        "6": "110",
        "7": "111"
    }

    resultado = ""

    for digito in numero:
        resultado += tabla[digito]

    # Eliminar ceros innecesarios al comienzo
    resultado = resultado.lstrip("0")

    return resultado if resultado else "0"