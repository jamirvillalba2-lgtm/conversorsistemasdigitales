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

        # Configuración principal
        self.ventana.title("Sistemas Digitales | Conversor")
        self.ventana.geometry("760x620")
        self.ventana.resizable(False, False)

        # Colores
        self.fondo = "#F4F7FB"
        self.panel = "#FFFFFF"
        self.principal = "#172B4D"
        self.secundario = "#2F80ED"
        self.secundario_hover = "#1F6FD1"
        self.texto = "#172B4D"
        self.gris = "#6B7280"
        self.borde = "#D9E2EC"
        self.resultado_fondo = "#EEF5FF"

        self.ventana.configure(bg=self.fondo)

        self.configurar_estilos()
        self.crear_interfaz()

    # ---------------------------------------------------------
    # ESTILOS
    # ---------------------------------------------------------

    def configurar_estilos(self):

        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "Combo.TCombobox",
            font=("Segoe UI", 11),
            padding=8,
            fieldbackground="white",
            background="white",
            bordercolor=self.borde
        )

    # ---------------------------------------------------------
    # INTERFAZ
    # ---------------------------------------------------------

    def crear_interfaz(self):

        # =========================
        # ENCABEZADO
        # =========================

        encabezado = tk.Frame(
            self.ventana,
            bg=self.principal,
            height=120
        )

        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        titulo = tk.Label(
            encabezado,
            text="SISTEMAS DIGITALES",
            font=("Segoe UI", 24, "bold"),
            bg=self.principal,
            fg="white"
        )

        titulo.pack(pady=(22, 2))

        subtitulo = tk.Label(
            encabezado,
            text="Conversor de Sistemas de Numeración",
            font=("Segoe UI", 12),
            bg=self.principal,
            fg="#D9E6F5"
        )

        subtitulo.pack()

        # =========================
        # INFORMACIÓN
        # =========================

        informacion = tk.Label(
            self.ventana,
            text="Ingeniería de Software  •  Sistemas Digitales  •  Semestre V",
            font=("Segoe UI", 10),
            bg=self.fondo,
            fg=self.gris
        )

        informacion.pack(pady=(18, 10))

        # =========================
        # PANEL PRINCIPAL
        # =========================

        panel = tk.Frame(
            self.ventana,
            bg=self.panel,
            highlightbackground=self.borde,
            highlightthickness=1
        )

        panel.pack(
            padx=70,
            pady=5,
            fill="both",
            expand=True
        )

        contenido = tk.Frame(
            panel,
            bg=self.panel
        )

        contenido.pack(
            padx=35,
            pady=25,
            fill="both",
            expand=True
        )

        # =========================
        # TÍTULO DEL PANEL
        # =========================

        titulo_panel = tk.Label(
            contenido,
            text="Seleccione una conversión",
            font=("Segoe UI", 14, "bold"),
            bg=self.panel,
            fg=self.texto
        )

        titulo_panel.pack(anchor="w")

        descripcion = tk.Label(
            contenido,
            text="Seleccione la operación e ingrese el valor correspondiente.",
            font=("Segoe UI", 10),
            bg=self.panel,
            fg=self.gris
        )

        descripcion.pack(anchor="w", pady=(3, 15))

        # =========================
        # MENÚ
        # =========================

        self.opciones = ttk.Combobox(
            contenido,
            state="readonly",
            style="Combo.TCombobox",
            values=[
                "Decimal → Binario",
                "Binario → Decimal",
                "Decimal → Octal",
                "Octal → Binario"
            ]
        )

        self.opciones.pack(
            fill="x",
            pady=(0, 20)
        )

        self.opciones.current(0)

        self.opciones.bind(
            "<<ComboboxSelected>>",
            self.actualizar_etiqueta
        )

        # =========================
        # ENTRADA
        # =========================

        self.etiqueta_numero = tk.Label(
            contenido,
            text="Número decimal",
            font=("Segoe UI", 11, "bold"),
            bg=self.panel,
            fg=self.texto
        )

        self.etiqueta_numero.pack(anchor="w")

        self.entrada = tk.Entry(
            contenido,
            font=("Segoe UI", 14),
            justify="center",
            bg="white",
            fg=self.texto,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground=self.borde,
            highlightcolor=self.secundario
        )

        self.entrada.pack(
            fill="x",
            ipady=9,
            pady=(7, 20)
        )

        self.entrada.bind(
            "<Return>",
            lambda event: self.convertir()
        )

        # =========================
        # BOTONES
        # =========================

        botones = tk.Frame(
            contenido,
            bg=self.panel
        )

        botones.pack(fill="x")

        boton_convertir = tk.Button(
            botones,
            text="CONVERTIR",
            font=("Segoe UI", 10, "bold"),
            bg=self.secundario,
            fg="white",
            activebackground=self.secundario_hover,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.convertir
        )

        boton_convertir.pack(
            side="left",
            padx=(0, 10),
            ipadx=20,
            ipady=8
        )

        boton_limpiar = tk.Button(
            botones,
            text="LIMPIAR",
            font=("Segoe UI", 10, "bold"),
            bg="#E8EDF3",
            fg=self.texto,
            activebackground="#DCE3EB",
            relief="flat",
            cursor="hand2",
            command=self.limpiar
        )

        boton_limpiar.pack(
            side="left",
            ipadx=20,
            ipady=8
        )

        # =========================
        # RESULTADO
        # =========================

        tk.Label(
            contenido,
            text="RESULTADO",
            font=("Segoe UI", 11, "bold"),
            bg=self.panel,
            fg=self.texto
        ).pack(
            anchor="w",
            pady=(25, 7)
        )

        resultado_frame = tk.Frame(
            contenido,
            bg=self.resultado_fondo,
            highlightbackground="#BBD4F5",
            highlightthickness=1
        )

        resultado_frame.pack(
            fill="x"
        )

        self.resultado = tk.Label(
            resultado_frame,
            text="---",
            font=("Consolas", 22, "bold"),
            bg=self.resultado_fondo,
            fg=self.principal
        )

        self.resultado.pack(
            pady=17
        )

        # =========================
        # BOTÓN SALIR
        # =========================

        boton_salir = tk.Button(
            self.ventana,
            text="SALIR",
            font=("Segoe UI", 10, "bold"),
            bg=self.principal,
            fg="white",
            activebackground="#0F1F38",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.ventana.destroy
        )

        boton_salir.pack(
            pady=(15, 10),
            ipadx=30,
            ipady=7
        )

        # =========================
        # PIE
        # =========================

        pie = tk.Label(
            self.ventana,
            text="Aplicativo académico • Sistemas Digitales",
            font=("Segoe UI", 9),
            bg=self.fondo,
            fg=self.gris
        )

        pie.pack(
            pady=(0, 12)
        )

        self.entrada.focus()

    # ---------------------------------------------------------
    # CAMBIAR TIPO DE ENTRADA
    # ---------------------------------------------------------

    def actualizar_etiqueta(self, evento=None):

        opcion = self.opciones.get()

        etiquetas = {
            "Decimal → Binario": "Número decimal",
            "Binario → Decimal": "Número binario",
            "Decimal → Octal": "Número decimal",
            "Octal → Binario": "Número octal"
        }

        self.etiqueta_numero.config(
            text=etiquetas[opcion]
        )

        self.entrada.delete(0, tk.END)
        self.resultado.config(text="---")
        self.entrada.focus()

    # ---------------------------------------------------------
    # CONVERSIONES
    # ---------------------------------------------------------

    def convertir(self):

        numero = self.entrada.get().strip()
        opcion = self.opciones.get()

        if not numero:

            messagebox.showwarning(
                "Dato requerido",
                "Debe ingresar un número para realizar la conversión."
            )

            self.entrada.focus()
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

            self.resultado.config(
                text=resultado
            )

        except ValueError:

            messagebox.showerror(
                "Entrada inválida",
                "El valor ingresado no corresponde "
                "al sistema de numeración seleccionado."
            )

            self.entrada.focus()

    # ---------------------------------------------------------
    # LIMPIAR
    # ---------------------------------------------------------

    def limpiar(self):

        self.entrada.delete(0, tk.END)

        self.resultado.config(
            text="---"
        )

        self.entrada.focus()


def iniciar_aplicacion():

    ventana = tk.Tk()

    Aplicacion(ventana)

    ventana.mainloop()