from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import time

option = Options()
option.add_experimental_option("detach", True)

webdriver_chrome_path = Service("your path to chrome driver")
driver = webdriver.Chrome(options=option, service=webdriver_chrome_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

store = driver.find_elements(By.CSS_SELECTOR, "#store b")
items_prices = []
items_names = []

for item in store:
    try:
        items_prices.append(int(item.text.split(' - ')[1].replace(",", "")))
        items_names.append(item.text.split(' - ')[0])
    except IndexError:
        pass

numbers_of_items = len(items_prices)
end_time = time() + 60*5
five_secs = time() + 5
items = []
while time() < end_time:
    id_click = ''
    cookie.click()
    if time() >= five_secs:
        nr_of_cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        for i in range(numbers_of_items):
            if nr_of_cookies >= items_prices[i]:
                if items_names[i] not in items:
                    items.append(items_names[i])
                    id_click = "buy" + items_names[i]
                    driver.find_element(By.ID, id_click).click()
        five_secs = time() + 5
print(items)

