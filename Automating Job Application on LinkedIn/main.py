import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

CHROME_WEBDRIVER_PATH = os.environ["CHROME_WEBDRIVER_PATH"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

option = Options()
option.add_experimental_option("detach", True)

chrome_webdriver_path = Service(CHROME_WEBDRIVER_PATH)
driver = webdriver.Chrome(options=option, service=chrome_webdriver_path)
linkedin_link = "https://www.linkedin.com/"
driver.get(linkedin_link  + "login")

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
sing_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sing_in_button.click()
time.sleep(5)

driver.get(linkedin_link + "jobs")
time.sleep(8)
search = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember25"]')
search.click()
search.send_keys("Python developer")
time.sleep(5)
search.send_keys(Keys.ENTER)
time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR, '.ember-view a')
results_list = []
for result in results:
    results_list.append(result.text)
    time.sleep(5)
    result.click()
    time.sleep(5)
    easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button span")
    if easy_apply.text == "Candidatură simplă":
        easy_apply.click()
        time.sleep(5)
        apply = driver.find_element(By.CSS_SELECTOR, ".pv4 button span")
        if apply.text == "Trimiteți candidatura":
            apply.click()
        else:
            x = driver.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-modal button")
            x.click()
            time.sleep(5)
            remove = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar--confirm-dialog button span")
            remove.click()
    time.sleep(5)


