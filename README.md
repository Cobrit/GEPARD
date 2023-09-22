# 📩 GEPARD MESSAGE 📩
Este script de Python automatiza el proceso de inicio de sesión y descarga de archivos desde el portal de Message Center (Gepard) utilizando Selenium WebDriver.

## Requisitos
Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas de Python:

1. Selenium WebDriver:
```bash
pip install selenium
```
3. ChromeDriver: Asegúrate de que ChromeDriver esté instalado y en tu PATH.

## Configuración
Antes de ejecutar el script, asegúrate de configurar las siguientes variables en el código según tus necesidades:

* userid: Tu nombre de usuario para el portal de Gepard.
* passwo: Tu contraseña para el portal de Gepard.
* source_directory: La ubicación del directorio donde se descargan los archivos (por defecto, la carpeta de descargas de Chrome).
* target_directory: La ubicación donde se moverán los archivos descargados.
* file_extension: La extensión de archivo de los archivos que deseas mover.
## Uso
Para ejecutar el script, simplemente llama a la función gepard_automation con tu nombre de usuario y contraseña de Gepard:

python
Copy code
gepard_automation("TuUsuario", "TuContraseña")
El script realizará las siguientes acciones:

Ingresará a la página de inicio de Message Center (Gepard).
Ingresará tus credenciales de usuario y contraseña.
Accederá a la sección de mensajes.
Agregará datos (según la lógica específica de tu aplicación).
Exportará datos a un archivo CSV (ajusta el selector CSS según tus necesidades).
Cerrará el navegador Chrome.
Además, el script moverá los archivos descargados desde la ubicación de descarga predeterminada a la ubicación especificada en target_directory, añadiendo la fecha y hora actual al nombre del archivo.

## Notas
Asegúrate de que ChromeDriver esté instalado y en tu PATH. Puedes descargarlo desde aquí.
Si deseas cambiar la extensión de archivo de los archivos a mover, ajusta la variable file_extension según tus necesidades.
Asegúrate de que las bibliotecas mencionadas anteriormente estén instaladas antes de ejecutar el script.
¡Esperamos que este script te ayude a automatizar tus tareas en el portal de Gepard! Si tienes alguna pregunta o encuentras algún problema, no dudes en preguntar.

Recuerda ajustar la información en el README según tus necesidades específicas y proporcionar instrucciones adicionales si es necesario. ¡Buena suerte con tu automatización!
