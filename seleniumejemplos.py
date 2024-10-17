from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Captura de pantalla de la página
driver.save_screenshot("wikipedia_homepage.png")
print("Captura de pantalla guardada como 'wikipedia_homepage.png'.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Simular un clic que podría generar una alerta (esto es solo un ejemplo, Wikipedia no genera alertas)
driver.execute_script("alert('Esto es una alerta de prueba!');")

# Esperar a que la alerta aparezca
time.sleep(2)

# Aceptar la alerta
alert = driver.switch_to.alert
alert.accept()
print("Alerta aceptada.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Desplazarse hacia el campo de búsqueda
search_input = driver.find_element(By.ID, "searchInput")
actions = ActionChains(driver)
actions.move_to_element(search_input).perform()

time.sleep(2)  # Espera para observar el desplazamiento
print("Desplazado al campo de búsqueda.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Obtener el valor del atributo 'title' de un enlace
element = driver.find_element(By.LINK_TEXT, "English")
attribute_value = element.get_attribute("title")
print("Valor del atributo title del enlace 'English':", attribute_value)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Obtener el texto de un encabezado específico
header_text = driver.find_element(By.TAG_NAME, "h1").text
print("Texto del encabezado:", header_text)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
# Verifica si un enlace específico está presente
link_present = driver.find_elements(By.LINK_TEXT, "English")
if link_present:
    print("El enlace 'English' está presente.")
else:
    print("El enlace 'English' no está presente.")

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Verifica si hay más de un elemento presente
elements_present = driver.find_elements(By.CLASS_NAME, "central-featured-lang")
if len(elements_present) > 1:
    print("Hay múltiples elementos de idiomas presentes.")
else:
    print("No hay suficientes elementos de idiomas.")

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Espera hasta que el texto 'Wikipedia' esté presente en el título
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Wikipedia")
)
print("El texto 'Wikipedia' está presente en el título.")

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Espera hasta que el botón de búsqueda sea clickeable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
print("El botón de búsqueda es clickeable.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Espera hasta que el elemento sea visible
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchInput"))
)
print("Elemento visible:", element.get_attribute("placeholder"))

driver.quit()
#Obtener el valor de un atributo de un elemento
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Obtener el valor de un atributo
element = driver.find_element(By.CLASS_NAME, "central-featured-lang")
attribute_value = element.get_attribute("lang")
print("Valor del atributo lang:", attribute_value)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Obtener el valor de un atributo
element = driver.find_element(By.CLASS_NAME, "central-featured-lang")
attribute_value = element.get_attribute("lang")
print("Valor del atributo lang:", attribute_value)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Verifica si el elemento está presente
element_present = driver.find_elements(By.ID, "searchInput")
if element_present:
    print("El campo de búsqueda está presente.")
else:
    print("El campo de búsqueda no está presente.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

# Espera hasta que el elemento esté presente
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchInput"))
)
print("El campo de búsqueda está presente.")

driver.quit()
