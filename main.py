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


@click.command()
@click.option('--de', prompt = 'Buscar mensajes de la fecha (AAA/MM/DD)', help = 'La primera fecha del intervalo')
@click.option('--hasta', prompt = 'A la fecha (AAA/MM/DD)', help = 'La segunda fecha del intervalo')
@click.option('--userid', prompt = 'Ingresa nombre de usuario', help = 'Nombre de Usuario')
@click.option('--passwo', prompt = 'Ingresa contraseña', help = 'Contraseña')

def gepard_automation(de, hasta, userid, passwo):
    url = "https://www.message-center.com.mx/"
    # Configuración para evitar notificaciones
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
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
    desde = wait.until(EC.presence_of_element_located((By.ID, 'FIni')))
    desde.click()
    desde.send_keys(de)
    hastaa = wait.until(EC.element_to_be_clickable((By.ID, 'FFin')))
    hastaa.click()
    hastaa.send_keys(hasta)
    buscar = driver.find_element(By.CLASS_NAME, 'cssBtn')
    buscar.click()
    


if __name__ == '__main__':
    gepard_automation()