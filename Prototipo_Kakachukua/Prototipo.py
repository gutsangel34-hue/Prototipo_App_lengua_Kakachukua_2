# Importamos tkinter para hacer ventanas
import tkinter as tk
import pygame
pygame.mixer.init()
import os

# Lista con las palabras en Kakachukua
palabras = [
    {"palabra": "Anchaye", "significado": "Hola", "audio": "audios/Anchaye.mp3"},
    {"palabra": "Yône", "significado": "Yerno","audio":"audios/Yone.mp3" },
    {"palabra": "Yonkuro", "significado": "Topónimo","audio":"audios/Yonkuro.mp3"},
    {"palabra": "Yosagaka", "significado": "Comida","audio":"audios/Yosagaka.mp3"},
    {"palabra": "Yue", "significado": "Huella","audio":"audios/Yue.mp3"},
    {"palabra": "Yuianichin", "significado": "Hoy","audio":"audios/Yuainichin.mp3"},
    {"palabra": "Yuikúmake", "significado": "Oro","audio":"audios/Yuikumake.mp3"},
    {"palabra": "Zarkáua", "significado": "Ciempiés","audio":"audios/Zarkaua.mp3"},
    {"palabra": "Zukánka", "significado": "Bonito","audio":"audios/zukanka.mp3"},
    {"palabra": "Zuminjánu", "significado": "Buenos días","audio":"audios/Zuminjanu.mp3"},
    {"palabra": "Zumizani", "significado": "Bueno","audio":"audios/Zumizani.mp3"}
]

# Colores que vamos a usar
COLOR_VERDE = "#2C5F4F"
COLOR_BEIGE = "#F7E6D7"
COLOR_NARANJA = "#D4813E"
COLOR_BLANCO = "#FFFFFF"

# Variable global para saber qué palabra está seleccionada
palabra_seleccionada = None

# Función que muestra la pantalla principal
def mostrar_menu():
    # Limpiamos todo lo que hay en la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Título grande
    titulo = tk.Label(ventana, text="Anchaye Kakachukua", 
                     font=("Arial", 24, "bold"), 
                     bg=COLOR_VERDE, fg=COLOR_BLANCO)
    titulo.pack(fill="x", pady=20)
    
    # Subtítulo
    subtitulo = tk.Label(ventana, text="Aprende Lengua Kankuama", 
                        font=("Arial", 12), 
                        bg=COLOR_BEIGE)
    subtitulo.pack(pady=10)
    
    # Botón para ver vocabulario
    boton_vocabulario = tk.Button(ventana, text="Ver Vocabulario", 
                                 command=mostrar_vocabulario,
                                 font=("Arial", 14), 
                                 bg=COLOR_NARANJA, fg=COLOR_BLANCO,
                                 width=20, height=2)
    boton_vocabulario.pack(pady=10)
    
    # Botón para ver información
    boton_info = tk.Button(ventana, text="Información", 
                          command=mostrar_info,
                          font=("Arial", 14), 
                          bg=COLOR_NARANJA, fg=COLOR_BLANCO,
                          width=20, height=2)
    boton_info.pack(pady=10)
    
    # Botón para salir
    boton_salir = tk.Button(ventana, text="Salir", 
                           command=ventana.quit,
                           font=("Arial", 14), 
                           bg="#8B4545", fg=COLOR_BLANCO,
                           width=20, height=2)
    boton_salir.pack(pady=10)
    
    # Pie de página
    pie = tk.Label(ventana, text="Universidad De La Salle\n2025", 
                  font=("Arial", 9), bg=COLOR_BEIGE)
    pie.pack(side="bottom", pady=10)

# Función que muestra la lista de palabras
def mostrar_vocabulario():
    # Limpiar pantalla
    for widget in ventana.winfo_children():
        widget.destroy()

    # Título
    titulo = tk.Label(ventana, text="Vocabulario",
                      font=("Arial", 24, "bold"),
                      bg=COLOR_VERDE, fg=COLOR_BLANCO)
    titulo.pack(fill="x", pady=20)

    info = tk.Label(ventana, text=f"Total: {len(palabras)} palabras",
                    font=("Arial", 11), bg=COLOR_BEIGE)
    info.pack(pady=10)

    # FRAME CONTENEDOR
    frame_lista = tk.Frame(ventana, bg=COLOR_BEIGE)
    frame_lista.pack(fill="both", expand=True, padx=20)

    # CANVAS
    canvas = tk.Canvas(frame_lista, bg=COLOR_BEIGE, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    # SCROLLBAR
    scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # FRAME INTERNO
    frame_palabras = tk.Frame(canvas, bg=COLOR_BEIGE)
    canvas.create_window((0, 0), window=frame_palabras, anchor="nw")

    # ELEMENTOS (botones de palabras)
    for p in palabras:
        boton = tk.Button(
            frame_palabras,
            text=f"{p['palabra']}\n{p['significado']}",
            command=lambda palabra=p: mostrar_detalle(palabra),
            font=("Arial", 12),
            bg=COLOR_BLANCO,
            width=30, height=3,
            relief="solid", bd=1
        )
        boton.pack(pady=10, padx=40, anchor="center")

    # Ajuste de scroll
    frame_palabras.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # --- SCROLL CON RUEDA CORRECTO ---

    def _on_mousewheel(event):
        # Windows y MacOS
        if event.delta:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        # Linux
        else:
            if event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

    def bind_scroll(event):
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_mousewheel)
        canvas.bind_all("<Button-5>", _on_mousewheel)

    def unbind_scroll(event):
        canvas.unbind_all("<MouseWheel>")
        canvas.unbind_all("<Button-4>")
        canvas.unbind_all("<Button-5>")

    canvas.bind("<Enter>", bind_scroll)
    canvas.bind("<Leave>", unbind_scroll)

    # --------------------------------------------------

    boton_volver = tk.Button(ventana, text="← Volver",
                             command=mostrar_menu,
                             font=("Arial", 12),
                             bg=COLOR_VERDE, fg=COLOR_BLANCO,
                             width=15, height=2)
    boton_volver.pack(pady=10)


# Función que simula reproducir audio
def reproducir_audio():
    global palabra_seleccionada

    ruta = palabra_seleccionada.get("audio", None)

    if not ruta:
        label_audio.config(text="⚠ No hay audio disponible.")
        return

    try:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
        label_audio.config(text="▶ Reproduciendo audio...")
    except Exception as e:
        label_audio.config(text=f"⚠ Error al reproducir: {e}")


def mostrar_detalle(palabra):
    global palabra_seleccionada
    palabra_seleccionada = palabra

    # Limpiar pantalla
    for widget in ventana.winfo_children():
        widget.destroy()

    # Título
    titulo = tk.Label(ventana, text=palabra["palabra"],
                      font=("Arial", 24, "bold"),
                      bg=COLOR_VERDE, fg=COLOR_BLANCO)
    titulo.pack(fill="x", pady=20)

    # Significado
    label_significado = tk.Label(ventana,
                                 text=f"Significado:\n{palabra['significado']}",
                                 font=("Arial", 14),
                                 bg=COLOR_BEIGE,
                                 justify="center")
    label_significado.pack(pady=20)

    # Recuadro para mostrar estado del audio
    global label_audio
    label_audio = tk.Label(ventana, text="",
                           font=("Arial", 12),
                           bg=COLOR_BEIGE,
                           fg="#444")
    label_audio.pack(pady=5)

    # Botón reproducir audio
    boton_audio = tk.Button(ventana, text="🔊 Escuchar",
                            command=reproducir_audio,
                            font=("Arial", 14),
                            bg=COLOR_NARANJA,
                            fg=COLOR_BLANCO,
                            width=15, height=2)
    boton_audio.pack(pady=10)

    # Botón volver
    boton_volver = tk.Button(ventana, text="← Volver",
                             command=mostrar_vocabulario,
                             font=("Arial", 12),
                             bg=COLOR_VERDE,
                             fg=COLOR_BLANCO,
                             width=15, height=2)
    boton_volver.pack(pady=20)

# Función que muestra información de la app
def mostrar_info():
    # Limpiamos la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Título
    titulo = tk.Label(ventana, text="Información", 
                     font=("Arial", 24, "bold"), 
                     bg=COLOR_VERDE, fg=COLOR_BLANCO)
    titulo.pack(fill="x", pady=20)
    
    # Información de la app
    info_texto = """
    Anchaye Kakachukua
    
    App para aprender la lengua Kankuama
    
    Objetivo:
    Preservar la lengua ancestral Kakachukua
    
    Proyecto de Semestre
    Ingeniería de Software
    Universidad De La Salle
    2025
    
    Desarrollador:
    Angel Vasquez Sequeda
    """
    
    label_info = tk.Label(ventana, text=info_texto, 
                         font=("Arial", 11), 
                         bg=COLOR_BEIGE,
                         justify="center")
    label_info.pack(pady=20, padx=20)
    
    # Botón para volver
    boton_volver = tk.Button(ventana, text="← Volver", 
                            command=mostrar_menu,
                            font=("Arial", 12), 
                            bg=COLOR_VERDE, fg=COLOR_BLANCO,
                            width=15, height=2)
    boton_volver.pack(pady=20)

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Anchaye Kakachukua")
ventana.geometry("400x600")
ventana.config(bg=COLOR_BEIGE)

# Iniciamos mostrando el menú
mostrar_menu()

# Ejecutamos la aplicación
ventana.mainloop()

