#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открытие окна браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.set_window_size(1920,1080)

action = ActionChains(driver)

#Двойной клик
double_click_button = driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
action.double_click(double_click_button).perform()
print('Произведен двойной клик')

#Проверка, что был произведен двойной клик
double_click_button_message = driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]').text
assert double_click_button_message == 'You have done a double click', 'Ошибка! Двойной клик не был совершен!'
print('Двойной клик был совершен')

#Правая кнопка мыши
right_click_button = driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
action.context_click(right_click_button).perform()
print('Произвели клик правой кнопки мыши')

#Проверка, что был произведен клик правой кнопкой
right_click_button_message = driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]').text
assert right_click_button_message == 'You have done a right click', 'Ошибка! Клик правой кнопкой не был совершен!'
print('Клик правой кнопкой был совершен')
