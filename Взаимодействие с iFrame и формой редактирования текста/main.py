from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открыть браузер и перейти по ссылке
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Переключиться на iFrame
iframe = driver.find_element(By.XPATH, '//*[@id="iFrame1"]')
driver.switch_to.frame(iframe)
inpute_pole = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')

#Ввод текста в iFrame
inpute_pole.send_keys(Keys.CONTROL + 'a')
inpute_pole.send_keys('Каждый охотник желает знать, где сидит фазан')
value_pole = inpute_pole.text
print(value_pole)

#Изменение вида текста
inpute_pole.send_keys(Keys.CONTROL + 'a')
bold_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[1]').click()
print('Сделали текст жирным')
uderline_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[5]').click()
print('Подчеркнули текст')

#Проверка, что текст не изменился
new_input_pole = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/b/u').text
print(new_input_pole)
assert value_pole == new_input_pole, 'Ошибка! Текст изменился'
print('Текст не поменялся')
