import os
import sys
sys.path.append(os.path.dirname(__file__))

SITENAME = 'PySchool - Una iniciativa de Python Chile'
SITEURL = ""
PATH = "content"
TIMEZONE = 'America/Santiago'
DEFAULT_LANG = 'es'
THEME = "theme"


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Todos las carpetas con archivos estáticos dentro de content/
STATIC_PATHS = [
    'img',
]

# Carpeta donde se alojan los archivos para crear post. Pelican por defecto tiene basepath content/
ARTICLE_PATHS = ['post']

