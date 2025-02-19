#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #Headless режим
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)
print('Открыто окно браузера')

#Ввести логин
user_name = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
user_name.send_keys('standard_user')
print('Введен логин')

#Ввести пароль
password = driver.find_element(By.XPATH, "//input[@id = 'password']")
password.send_keys('secret_sauce')
print('Введен пароль')

#Нажатие на кнопку авторизации
button_click = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
button_click.click()
print('Нажата кнопка авторизации')

#Добавить все товары в корзину и перейти в нее
add_backcap_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
add_bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
add_t_short_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
add_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
add_onesie_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
add_T_short_red_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
shopping_cart_link = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
print('Добавили все товары в корзину')

#Наведение на последний элемент в корзине
actions = ActionChains(driver)
element = driver.find_element(By.ID, 'item_3_title_link')
actions.move_to_element(element).perform()
print('Навелись на последний элемент')

