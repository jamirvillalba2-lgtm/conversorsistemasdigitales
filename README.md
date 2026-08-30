# Conversor de Sistemas Digitales

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-00599C?style=flat)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows%2064--bit-0078D6?style=flat&logo=windows)
![Licencia](https://img.shields.io/badge/Licencia-Acad%C3%A9mica-green?style=flat)

Aplicativo de escritorio desarrollado en Python para realizar conversiones de números entre distintos sistemas de numeración (Decimal, Binario y Octal). Proyecto desarrollado para la asignatura **Sistemas Digitales** del programa de **Ingeniería de Software (Semestre V)** de la **Universidad de Cartagena**.

---

## 🚀 Funcionalidades

* **Decimal → Binario:** Convierte números enteros decimales no negativos a su representación binaria.
* **Binario → Decimal:** Convierte cadenas binarias válidas a números decimales.
* **Decimal → Octal:** Convierte enteros decimales a sistema octal (base 8).
* **Octal → Binario:** Realiza la conversión de octal a binario.
* **Validación de Entradas:** Impide el ingreso de caracteres no válidos según la base seleccionada.
* **Interfaz Moderna y Adaptativa:** Soporte nativo para pantallas de alta densidad de píxeles (High-DPI / 4K).

---

## 🛠️ Tecnologías y Patrones de Diseño

* **Lenguaje:** Python 3.13.3
* **Interfaz Gráfica:** Tkinter / `ttk` (Tema `clam` personalizado)
* **Empaquetado:** PyInstaller 6.22
* **Patrones de Diseño:**
  * **Arquitectura en Capas:** Separación limpia entre Lógica de Negocio (`conversiones.py`) y Presentación (`interfaz.py`).
  * **Patrón Strategy:** Mapeo dinámico de estrategias de conversión mediante estructuras de datos para eliminar condicionales complejos (`if-elif`).

---

## 📁 Estructura del Proyecto

```text
conversorsistemasdigitales/
├── dist/
│   └── SistemasDigitalesConversor.exe   # Ejecutable compilado independiente
├── src/
│   ├── conversiones.py                  # Lógica pura de conversiones numéricas
│   ├── interfaz.py                      # Interfaz gráfica de usuario (Tkinter)
│   └── main.py                          # Punto de entrada y configuración High-DPI
├── venv/                                # Entorno virtual de Python
├── SistemasDigitalesConversor.spec      # Archivo de configuración de PyInstaller
└── README.md                            # Documentación del proyecto