from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time

CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
EMAIL = os.environ["EMAIL"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
DOWN_INTERNET_PROVIDER = 120
UP_INTERNET_PROVIDER = 60


class InternetSpeedTwitterBot:
    def __init__(self):
        option = Options()
        option.add_experimental_option("detach", True)

        web_driver_path = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(options=option, service=web_driver_path)
        self.internet_provider = ''
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        info = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        info.click()
        time.sleep(3)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(100)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.internet_provider = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]').text

    def tweet_at_provider(self):
        self.get_internet_speed()

        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(8)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.click()
        time.sleep(3)
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(4)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)

        time.sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        cookie = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]')
        cookie.click()

        time.sleep(5)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()
        time.sleep(5)
        tweet_text = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div'
                                                        '/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div'
                                                        '/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div'
                                                        '/div/div/div[2]/div/div/div/div')
        tweet_text.send_keys(f"Hello {self.internet_provider}, why is my internet speed {self.down}down/{self.up}up "
                             f"when I pay for {DOWN_INTERNET_PROVIDER}down/{UP_INTERNET_PROVIDER}up?")
        time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()


x = InternetSpeedTwitterBot()

if x.down < DOWN_INTERNET_PROVIDER or x.up < UP_INTERNET_PROVIDER:
    x.tweet_at_provider()