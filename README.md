# Prototipo_App_lengua_Kakachukua_2
# Anchaye Kakachukua

Aplicación educativa para aprender la lengua ancestral Kankuama (Kakachukua).

## Descripción

Anchaye Kakachukua es una herramienta didáctica desarrollada como proyecto de semestre en la carrera de Ingeniería de Software de la Universidad De La Salle. La aplicación permite a los usuarios explorar vocabulario en lengua Kakachukua con pronunciación de audio.

## Características

- 📚 Vocabulario con más de 10 palabras en Kakachukua
- 🔊 Reproducción de audio para pronunciación correcta
- 🎨 Interfaz gráfica amigable con Tkinter
- 📱 Navegación intuitiva entre menús

## Requisitos

- Python 3.7+
- tkinter (incluido en la mayoría de instalaciones de Python)
- pygame

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/anchaye-kakachukua.git
cd anchaye-kakachukua
```

2. Instala las dependencias en la terminal:
```bash
pip install pygame
```

## Estructura del Proyecto

```
anchaye-kakachukua/
├── main.py                 # Archivo principal de la aplicación
├── audios/                 # Carpeta con los archivos de audio
│   ├── Anchaye.mp3
│   ├── Yone.mp3
│   ├── Yonkuro.mp3
│   ├── Yosagaka.mp3
│   ├── Yue.mp3
│   ├── Yuainichin.mp3
│   ├── Yuikumake.mp3
│   ├── Zarkaua.mp3
│   ├── zukanka.mp3
│   ├── Zuminjanu.mp3
│   └── Zumizani.mp3
└── README.md               # Este archivo
```

## Uso

Ejecuta la aplicación con:
```bash
python main.py
```

### Agregar Nuevas Palabras

Para agregar nuevas palabras al vocabulario, edita la lista `palabras` en `main.py`. Cada palabra debe tener la siguiente estructura:

```python
{
    "palabra": "Nombre de la palabra",
    "significado": "Traducción al español",
    "audio": "audios/nombre_del_archivo.mp3"
}
```

**⚠️ Importante:** Los archivos de audio deben ubicarse en la carpeta `audios/` y el campo `"audio"` debe apuntar a la ruta relativa `audios/nombre_del_archivo.mp3`.

### Ejemplo:
```python
palabras = [
    {
        "palabra": "Anchaye", 
        "significado": "Hola", 
        "audio": "audios/Anchaye.mp3"
    },
    {
        "palabra": "Nueva Palabra", 
        "significado": "Significado", 
        "audio": "audios/Nueva_Palabra.mp3"
    }
]
```

## Navegación de la Aplicación

- **Menú Principal:** Acceso a vocabulario e información
- **Ver Vocabulario:** Visualiza la lista completa de palabras
- **Detalle de Palabra:** Muestra significado y permite reproducir audio
- **Información:** Detalles sobre el proyecto

## Autor

- Angel Vasquez Sequeda

## Institución

Universidad De La Salle  
Ingeniería de Software  
2025

## Licencia

Este proyecto es de uso educativo.
