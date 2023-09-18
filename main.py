from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import click
import os
import shutil
from datetime import datetime



def gepard_automation(userid, passwo):
    url = "https://www.message-center.com.mx/"
    # Configuración para evitar notificaciones
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,  # Desactiva la ventana emergente de descarga
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False,  # Desactiva la verificación de seguridad de descargas
})
    # Configuración para ingresar al explorador
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # Configurar credenciales
    user = driver.find_element(By.ID,'Usr')
    user.send_keys(userid)
    password = driver.find_element(By.ID, 'Pass')
    password.send_keys(passwo)
    ingresar = driver.find_element(By.CLASS_NAME, 'cssButtonMn')
    ingresar.click()
    time.sleep(10)

    # Ir a mensajes
    mensajes = driver.find_element(By.XPATH, '//*[@id="MenuPanel"]/table/tbody/tr/td[2]/img')
    mensajes.click()
    time.sleep(5)
    # Agregar datos
    buscar = driver.find_element(By.CLASS_NAME, 'cssBtn')
    buscar.click()
    # Exportar Excel
    export = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="Exportar a Excel..."]')))
    export.click()
    time.sleep(10)
    driver.quit()


def move_downloaded_file(source_directory, target_directory, file_extension):
    # Enumera los archivos en el directorio de origen
    for filename in os.listdir(source_directory):
        if filename.endswith(file_extension):
            
            # Obtén la fecha actual en el formato deseado (A-M-D-H-M-S)
            current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Construye el nuevo nombre de archivo con la fecha actual
            new_filename = f"{filename[:-len(file_extension)]}_{current_datetime}{file_extension}"
            
            # Construye la ruta completa del archivo de origen
            source_filepath = os.path.join(source_directory, filename)

            # Construye la ruta completa del archivo de destino en la nueva ubicación
            target_filepath = os.path.join(target_directory, new_filename)

            # Mueve el archivo a la ubicación deseada
            shutil.move(source_filepath, target_filepath)

            if os.path.exists(target_filepath):
                print(f"Archivo movido correctamente a: {target_filepath}")
            else:
                print(f"No se pudo mover el archivo a la ubicación deseada: {target_filepath}")


source_directory = r'C:\Users\DSTHREE\Downloads'  # Directorio de descarga predeterminado
target_directory = r'Z:\SMS'  # Nueva ubicación de destino
file_extension = '.csv'  # Extensión del archivo a mover (ajusta según sea necesario)



gepard_automation("f.lozada@coperva.com", "12345678")
# Llama a la función para mover el archivo
move_downloaded_file(source_directory, target_directory, file_extension)

