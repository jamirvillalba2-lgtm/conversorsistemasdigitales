import tkinter as tk
from tkinter import ttk, messagebox

from conversiones import (
    decimal_a_binario,
    binario_a_decimal,
    decimal_a_octal,
    octal_a_binario
)


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana

        self.ventana.title("Sistemas Digitales - Conversor")
        self.ventana.geometry("700x500")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        # Título principal
        titulo = tk.Label(
            self.ventana,
            text="SISTEMAS DIGITALES",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=(25, 5))

        subtitulo = tk.Label(
            self.ventana,
            text="Conversor de Sistemas de Numeración",
            font=("Arial", 13)
        )
        subtitulo.pack(pady=(0, 25))

        # Marco principal
        marco = tk.Frame(self.ventana)
        marco.pack(padx=40, fill="x")

        # Etiqueta del menú
        tk.Label(
            marco,
            text="Seleccione una conversión:",
            font=("Arial", 12, "bold")
        ).pack(anchor="w")

        # Menú de conversiones
        self.opciones = ttk.Combobox(
            marco,
            state="readonly",
            font=("Arial", 11),
            values=[
                "Decimal → Binario",
                "Binario → Decimal",
                "Decimal → Octal",
                "Octal → Binario"
            ]
        )

        self.opciones.pack(fill="x", pady=(8, 20))
        self.opciones.current(0)

        # Etiqueta del número
        self.etiqueta_numero = tk.Label(
            marco,
            text="Ingrese el número decimal:",
            font=("Arial", 12, "bold")
        )
        self.etiqueta_numero.pack(anchor="w")

        # Campo de entrada
        self.entrada = tk.Entry(
            marco,
            font=("Arial", 14),
            justify="center"
        )
        self.entrada.pack(fill="x", pady=(8, 20))

        # Cambiar etiqueta según la conversión
        self.opciones.bind(
            "<<ComboboxSelected>>",
            self.actualizar_etiqueta
        )

        # Botones
        marco_botones = tk.Frame(marco)
        marco_botones.pack(pady=5)

        boton_convertir = tk.Button(
            marco_botones,
            text="CONVERTIR",
            font=("Arial", 11, "bold"),
            width=15,
            command=self.convertir
        )
        boton_convertir.grid(row=0, column=0, padx=8)

        boton_limpiar = tk.Button(
            marco_botones,
            text="LIMPIAR",
            font=("Arial", 11, "bold"),
            width=15,
            command=self.limpiar
        )
        boton_limpiar.grid(row=0, column=1, padx=8)

        # Resultado
        tk.Label(
            marco,
            text="RESULTADO:",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(30, 8))

        self.resultado = tk.Label(
            marco,
            text="---",
            font=("Arial", 22, "bold"),
            relief="sunken",
            height=2
        )
        self.resultado.pack(fill="x")

        # Botón salir
        boton_salir = tk.Button(
            self.ventana,
            text="SALIR",
            font=("Arial", 11, "bold"),
            width=15,
            command=self.ventana.destroy
        )
        boton_salir.pack(pady=25)

    def actualizar_etiqueta(self, evento=None):
        opcion = self.opciones.get()

        etiquetas = {
            "Decimal → Binario": "Ingrese el número decimal:",
            "Binario → Decimal": "Ingrese el número binario:",
            "Decimal → Octal": "Ingrese el número decimal:",
            "Octal → Binario": "Ingrese el número octal:"
        }

        self.etiqueta_numero.config(
            text=etiquetas[opcion]
        )

        self.entrada.delete(0, tk.END)
        self.resultado.config(text="---")

    def convertir(self):
        numero = self.entrada.get().strip()
        opcion = self.opciones.get()

        if not numero:
            messagebox.showwarning(
                "Dato requerido",
                "Debe ingresar un número."
            )
            return

        try:

            if opcion == "Decimal → Binario":

                if not numero.isdigit():
                    raise ValueError

                valor = int(numero)
                resultado = decimal_a_binario(valor)

            elif opcion == "Binario → Decimal":

                if not all(digito in "01" for digito in numero):
                    raise ValueError

                resultado = binario_a_decimal(numero)

            elif opcion == "Decimal → Octal":

                if not numero.isdigit():
                    raise ValueError

                valor = int(numero)
                resultado = decimal_a_octal(valor)

            elif opcion == "Octal → Binario":

                if not all(digito in "01234567" for digito in numero):
                    raise ValueError

                resultado = octal_a_binario(numero)

            self.resultado.config(text=resultado)

        except ValueError:

            messagebox.showerror(
                "Entrada inválida",
                "El número ingresado no corresponde "
                "al sistema seleccionado."
            )

    def limpiar(self):
        self.entrada.delete(0, tk.END)
        self.resultado.config(text="---")
        self.entrada.focus()


def iniciar_aplicacion():
    ventana = tk.Tk()
    Aplicacion(ventana)
    ventana.mainloop()