"""
Módulo de interfaz gráfica de usuario (GUI) utilizando Tkinter.
Aplica desacoplamiento modular y el patrón Strategy para los manejadores de conversión.
"""

from typing import Dict, Any, Callable
import tkinter as tk
from tkinter import ttk, messagebox

from conversiones import (
    decimal_a_binario,
    binario_a_decimal,
    decimal_a_octal,
    octal_a_binario
)


class Aplicacion:
    """Controlador principal de la interfaz de usuario."""

    # Constantes de Tema y Estilos
    COLOR_FONDO = "#F4F7FB"
    COLOR_PANEL = "#FFFFFF"
    COLOR_PRINCIPAL = "#172B4D"
    COLOR_SECUNDARIO = "#2F80ED"
    COLOR_HOVER = "#1F6FD1"
    COLOR_TEXTO = "#172B4D"
    COLOR_GRIS = "#6B7280"
    COLOR_BORDE = "#D9E2EC"
    COLOR_RESULTADO_BG = "#EEF5FF"
    COLOR_RESULTADO_BORDE = "#BBD4F5"

    FUENTE_TITULO = ("Segoe UI", 22, "bold")
    FUENTE_SUBTITULO = ("Segoe UI", 11)
    FUENTE_SECCION = ("Segoe UI", 13, "bold")
    FUENTE_TEXTO = ("Segoe UI", 11)
    FUENTE_RESULTADO = ("Consolas", 22, "bold")

    def __init__(self, ventana: tk.Tk) -> None:
        self.ventana = ventana
        self._configurar_ventana_principal()
        self._mapear_estrategias_conversion()
        self._configurar_estilos_ttk()
        self._construir_ui()

    def _configurar_ventana_principal(self) -> None:
        self.ventana.title("Sistemas Digitales | Conversor")
        self.ventana.geometry("760x680")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg=self.COLOR_FONDO)

    def _mapear_estrategias_conversion(self) -> None:
        """Configura el patrón Strategy para eliminar sentencias if-elif en tiempo de conversión."""
        self.estrategias: Dict[str, Dict[str, Any]] = {
            "Decimal → Binario": {
                "etiqueta": "Número decimal",
                "validador": lambda v: v.isdigit(),
                "convertidor": lambda v: decimal_a_binario(int(v))
            },
            "Binario → Decimal": {
                "etiqueta": "Número binario",
                "validador": lambda v: all(d in "01" for d in v),
                "convertidor": lambda v: str(binario_a_decimal(v))
            },
            "Decimal → Octal": {
                "etiqueta": "Número decimal",
                "validador": lambda v: v.isdigit(),
                "convertidor": lambda v: decimal_a_octal(int(v))
            },
            "Octal → Binario": {
                "etiqueta": "Número octal",
                "validador": lambda v: all(d in "01234567" for d in v),
                "convertidor": lambda v: octal_a_binario(v)
            }
        }

    def _configurar_estilos_ttk(self) -> None:
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Combo.TCombobox",
            font=self.FUENTE_TEXTO,
            padding=6,
            fieldbackground="white",
            background="white",
            bordercolor=self.COLOR_BORDE
        )

    def _construir_ui(self) -> None:
        """Ensambla modularmente los componentes gráficos."""
        self._crear_encabezado()
        self._crear_subcabecera()
        
        panel_contenedor = self._crear_panel_contenedor()
        self._crear_menu_opciones(panel_contenedor)
        self._crear_campo_entrada(panel_contenedor)
        self._crear_botones_accion(panel_contenedor)
        self._crear_panel_resultado(panel_contenedor)
        
        self._crear_boton_salir()
        self._crear_pie_pagina()
        
        self.entrada.focus()

    def _crear_encabezado(self) -> None:
        encabezado = tk.Frame(self.ventana, bg=self.COLOR_PRINCIPAL, height=100)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="SISTEMAS DIGITALES",
            font=self.FUENTE_TITULO,
            bg=self.COLOR_PRINCIPAL,
            fg="white"
        ).pack(pady=(16, 2))

        tk.Label(
            encabezado,
            text="Conversor de Sistemas de Numeración",
            font=self.FUENTE_SUBTITULO,
            bg=self.COLOR_PRINCIPAL,
            fg="#D9E6F5"
        ).pack()

    def _crear_subcabecera(self) -> None:
        tk.Label(
            self.ventana,
            text="Ingeniería de Software  •  Sistemas Digitales  •  Semestre V",
            font=("Segoe UI", 9),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_GRIS
        ).pack(pady=(12, 6))

    def _crear_panel_contenedor(self) -> tk.Frame:
        panel_externo = tk.Frame(
            self.ventana,
            bg=self.COLOR_PANEL,
            highlightbackground=self.COLOR_BORDE,
            highlightthickness=1
        )
        panel_externo.pack(padx=60, pady=5, fill="both", expand=True)

        contenido = tk.Frame(panel_externo, bg=self.COLOR_PANEL)
        contenido.pack(padx=30, pady=20, fill="both", expand=True)

        tk.Label(
            contenido,
            text="Seleccione una conversión",
            font=self.FUENTE_SECCION,
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO
        ).pack(anchor="w")

        tk.Label(
            contenido,
            text="Seleccione la operación e ingrese el valor correspondiente.",
            font=("Segoe UI", 9),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_GRIS
        ).pack(anchor="w", pady=(2, 12))

        return contenido

    def _crear_menu_opciones(self, padre: tk.Frame) -> None:
        self.opciones = ttk.Combobox(
            padre,
            state="readonly",
            style="Combo.TCombobox",
            values=list(self.estrategias.keys())
        )
        self.opciones.pack(fill="x", pady=(0, 14))
        self.opciones.current(0)
        self.opciones.bind("<<ComboboxSelected>>", self.actualizar_etiqueta)

    def _crear_campo_entrada(self, padre: tk.Frame) -> None:
        self.etiqueta_numero = tk.Label(
            padre,
            text=self.estrategias[self.opciones.get()]["etiqueta"],
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO
        )
        self.etiqueta_numero.pack(anchor="w")

        self.entrada = tk.Entry(
            padre,
            font=("Segoe UI", 13),
            justify="center",
            bg="white",
            fg=self.COLOR_TEXTO,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground=self.COLOR_BORDE,
            highlightcolor=self.COLOR_SECUNDARIO
        )
        self.entrada.pack(fill="x", ipady=7, pady=(5, 15))
        self.entrada.bind("<Return>", lambda event: self.convertir())

    def _crear_botones_accion(self, padre: tk.Frame) -> None:
        botones_frame = tk.Frame(padre, bg=self.COLOR_PANEL)
        botones_frame.pack(fill="x")

        tk.Button(
            botones_frame,
            text="CONVERTIR",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_SECUNDARIO,
            fg="white",
            activebackground=self.COLOR_HOVER,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.convertir
        ).pack(side="left", padx=(0, 10), ipadx=18, ipady=6)

        tk.Button(
            botones_frame,
            text="LIMPIAR",
            font=("Segoe UI", 10, "bold"),
            bg="#E8EDF3",
            fg=self.COLOR_TEXTO,
            activebackground="#DCE3EB",
            relief="flat",
            cursor="hand2",
            command=self.limpiar
        ).pack(side="left", ipadx=18, ipady=6)

    def _crear_panel_resultado(self, padre: tk.Frame) -> None:
        tk.Label(
            padre,
            text="RESULTADO",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO
        ).pack(anchor="w", pady=(18, 5))

        frame_res = tk.Frame(
            padre,
            bg=self.COLOR_RESULTADO_BG,
            highlightbackground=self.COLOR_RESULTADO_BORDE,
            highlightthickness=1
        )
        frame_res.pack(fill="x")

        self.resultado = tk.Label(
            frame_res,
            text="---",
            font=self.FUENTE_RESULTADO,
            bg=self.COLOR_RESULTADO_BG,
            fg=self.COLOR_PRINCIPAL
        )
        self.resultado.pack(pady=12)

    def _crear_boton_salir(self) -> None:
        tk.Button(
            self.ventana,
            text="SALIR",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_PRINCIPAL,
            fg="white",
            activebackground="#0F1F38",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.ventana.destroy
        ).pack(pady=(10, 6), ipadx=26, ipady=6)

    def _crear_pie_pagina(self) -> None:
        tk.Label(
            self.ventana,
            text="Aplicativo académico • Sistemas Digitales",
            font=("Segoe UI", 9),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_GRIS
        ).pack(pady=(0, 8))

    # --- Manejadores de Eventos ---

    def actualizar_etiqueta(self, evento: tk.Event | None = None) -> None:
        opcion_seleccionada = self.opciones.get()
        configuracion = self.estrategias.get(opcion_seleccionada)
        
        if configuracion:
            self.etiqueta_numero.config(text=configuracion["etiqueta"])

        self.limpiar()

    def convertir(self) -> None:
        numero = self.entrada.get().strip()
        opcion_seleccionada = self.opciones.get()
        estrategia = self.estrategias.get(opcion_seleccionada)

        if not numero:
            messagebox.showwarning(
                "Dato requerido",
                "Debe ingresar un número para realizar la conversión."
            )
            self.entrada.focus()
            return

        if not estrategia or not estrategia["validador"](numero):
            messagebox.showerror(
                "Entrada inválida",
                "El valor ingresado no corresponde al sistema de numeración seleccionado."
            )
            self.entrada.focus()
            return

        try:
            resultado_calculado = estrategia["convertidor"](numero)
            self.resultado.config(text=resultado_calculado)
        except Exception as e:
            messagebox.showerror("Error de conversión", str(e))
            self.entrada.focus()

    def limpiar(self) -> None:
        self.entrada.delete(0, tk.END)
        self.resultado.config(text="---")
        self.entrada.focus()


def iniciar_aplicacion() -> None:
    ventana = tk.Tk()
    Aplicacion(ventana)
    ventana.mainloop()