# prueba_inventario_cargamos
Prueba sobre una REstFul Api realizada en Flask

Para que la aplicación funcione y se pueda ejecutar, debemos crear las siguientes variables de entorno en el fichero activate del entorno virtual.

export FLASK_APP="entrypoint:app"

export FLASK_ENV="development"

export APP_SETTINGS_MODULE="config.default"

Ejecutar los siguientes comandos para hacer las migraciones a la base de datos
flask db init

flask db migrate

flask db upgrade
