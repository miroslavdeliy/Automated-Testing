#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открытие окна браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Выбрать чек бокс
check_box = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
check_box.click()

#Проверка, что выбран
check_box_input = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
assert check_box_input.is_selected(), 'Ошибка! Чек-бокс не выбран!'
print('Чек-бокс выбран')
