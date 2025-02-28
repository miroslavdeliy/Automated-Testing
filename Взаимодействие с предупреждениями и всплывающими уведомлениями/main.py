import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Открыть браузер и перейти по ссылке
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.set_window_size(1920,1080)

# Тестирование работы окна alert
alert_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
print('Открылось окно alert')
time.sleep(2)
driver.switch_to.alert.accept()
print('Закрылось окно alert')

# Проверка корректности работы alert
result_alert = driver.find_element(By.XPATH, '//*[@id="result"]').text
assert result_alert == 'You successfully clicked an alert', 'Ошибка! Alert работает некорректно'
print('Alert работает корректно')

# Тестирование работы окна confirm
confirm_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
print('Открылось окно confirm')
time.sleep(2)
driver.switch_to.alert.dismiss()
print('Закрылось окно confirm')

# Проверка корректности работы confirm
result_confirm = driver.find_element(By.XPATH, '//*[@id="result"]').text
assert result_confirm == 'You clicked: Cancel', 'Ошибка! Alert работает некорректно'
print('Confirm работает корректно')

#
# Тестирование работы окна confirm
promt_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
print('Открылось окно promt')
time.sleep(2)
message = 'Hello'
driver.switch_to.alert.send_keys(message)
print('Ввели текст: ' + message)
driver.switch_to.alert.accept()
print('Закрылось окно promt')

# Проверка корректности работы promt
result_promt = driver.find_element(By.XPATH, '//*[@id="result"]').text
assert result_promt == 'You entered: ' + message, 'Ошибка! Promt работает некорректно'
print('Promt работает корректно')