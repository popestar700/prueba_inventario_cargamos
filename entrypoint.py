"""Creando la instancia de la app de Flask 
indicando dónde están definidos los parámetros de configuración 
(el fichero de configuración se especifica en la variable de entorno APP_SETTINGS_MODULE)."""

import os
from app import create_app
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)