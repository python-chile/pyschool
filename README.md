# PySchool

Sitio web oficial de **PySchool**, una iniciativa educativa de [Python Chile](https://www.pythonchile.cl) para enseñar programación Python a la comunidad hispanohablante.

## ¿Qué es PySchool?

PySchool es un espacio de aprendizaje donde cualquier persona puede dar sus primeros pasos en Python directamente desde el navegador, sin necesidad de instalar nada. El sitio incluye un intérprete de Python interactivo potenciado por [Pyodide](https://pyodide.org/) y recursos de las ediciones anteriores del evento.

## Tecnologías

- **[Pelican](https://getpelican.com/)** - Generador de sitios estáticos en Python
- **Jinja2** - Motor de plantillas HTML
- **Pyodide** - Python compilado a WebAssembly para ejecutarse en el navegador
- **CSS puro** - Diseño brutalista personalizado sin frameworks externos

## Estructura del proyecto

```
pyschool/
├── content/          # Contenido estático (imágenes, etc.)
│   └── img/          # Imágenes del sitio
├── theme/            # Tema personalizado de Pelican
│   ├── templates/    # Plantillas Jinja2
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── welcome.html
│   │   ├── python_interpreter.html
│   │   ├── projects.html
│   │   └── footer.html
│   └── static/
│       └── css/
│           └── styles.css
├── pelicanconf.py    # Configuración de Pelican (desarrollo)
├── publishconf.py    # Configuración de Pelican (producción)
└── requirements.txt  # Dependencias Python
```

## Instalación y uso local

### Requisitos

- Python 3.9+

### Pasos

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/python-chile/pyschool.git
   cd pyschool
   ```

2. **Crear un entorno virtual e instalar dependencias**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Levantar el servidor de desarrollo**

   ```bash
   pelican --listen
   ```

   El sitio estará disponible en [http://localhost:8000](http://localhost:8000).

4. **Reconstruir automáticamente al guardar cambios**

   ```bash
   pelican --autoreload --listen
   ```

## Comunidad

- Sitio web: [www.pythonchile.cl](https://www.pythonchile.cl)
- Contacto: [contacto@pythonchile.com](mailto:contacto@pythonchile.com)

## Licencia

Este proyecto es parte de la comunidad Python Chile. Consulta el repositorio para más detalles sobre la licencia.
