from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Нажать на Dropdwon выбора страны
click_drop_state = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]/span')
click_drop_state.click()

#Выбрать страну
select_state = driver.find_element(By.XPATH, '//li[@class="select2-results__option"][10]')
select_state.click()

#Нажать на Dropdwon выбора штата
click_drop_state = driver.find_element(By.XPATH, '//input[@class="select2-search__field"]')
click_drop_state.click()

#Выбрать штат
select_state = driver.find_element(By.XPATH, '//li[@class="select2-results__option"][3]')
select_state.click()