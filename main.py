import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import click
import os
import re



def gepard_automation(userid, passwo):
    url = "https://www.message-center.com.mx/"
    # Configuración para evitar notificaciones
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "RUTA_DE_DESCARGA_AQUI",
        "profile.default_content_setting_values.notifications": 1,
        "download.prompt_for_download": False,  # Desactiva la ventana emergente de descarga
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False,  # Desactiva la verificación de seguridad de descargas
    "plugins.always_open_pdf_externally": True,
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

gepard_automation("f.lozada@coperva.com", "12345678")

