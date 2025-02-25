#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открытие окна браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Выбрать radio-button
radio_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/label')
radio_button.click()

#Проверка, что выбран radio-button
radio_button_input = driver.find_element(By.XPATH, '//*[@id="impressiveRadio"]')
assert radio_button_input.is_selected(), 'Ошибка! radio-button не выбран!'
print('radio-button выбран')

