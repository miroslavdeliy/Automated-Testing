from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открыть браузер и перейти по ссылке
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Открытие новой вкладки
new_tab = driver.find_element(By.XPATH, '//*[@id="tabButton"]').click()
driver.switch_to.window(driver.window_handles[1])

#Проверка, что на новой вкладке
check_text_tab = driver.find_element(By.XPATH, '//*[@id="sampleHeading"]').text
assert check_text_tab == 'This is a sample page', 'Ошибка! Новая вкладка не открылась!'
print('Открылась новая вкладка')

#Закрытие вкладки и возврат на предыдущую страницу
driver.close()
driver.switch_to.window(driver.window_handles[0])

#Открытие нового окна и переход в него
new_window = driver.find_element(By.XPATH, '//*[@id="windowButton"]').click()
driver.switch_to.window(driver.window_handles[1])

#Проверка, что находимся в новом окне
check_text_window = driver.find_element(By.XPATH, '//*[@id="sampleHeading"]').text
assert check_text_window == 'This is a sample page', 'Ошибка! Новое окно не открылось!'
print('Открылось новое окно')

#Закрытие окна и возврат на предыдущую страницу
driver.close()
driver.switch_to.window(driver.window_handles[0])