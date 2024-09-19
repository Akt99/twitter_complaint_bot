from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

PROMISED_UP= 100
PROMISED_DOWN=1000
#CHROME_DELIVERED_PATH= "/usr/local/bin/chromedriver"
TWITTER_ID = "your phone number/email"
TWITTER_PASSWORD="your password"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        service=Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.up=0
        self.down=0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        go_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
        )
        go_button.click()

        time.sleep(40)
        self.down = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed"))
        ).text

        self.up = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed"))
        ).text

        print(f"Download speed: {self.down}, Upload speed: {self.up}")


    def tweet_at_provider(self):
            self.driver.get("https://twitter.com/login")
            time.sleep(5)
            phone_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']"))
            )
            phone_field.send_keys(TWITTER_ID)
            #input("Pause to inspect the Next button... Press Enter to continue after selecting the correct selector.")

            next_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
            )
            next_button.click()
            #input("Paused after clicking 'Next'. Press Enter to continue after capturing the password selector...")

            # Wait for password input field and enter the password
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
            )
            password_field.send_keys(TWITTER_PASSWORD)
            #input("Paused after entering the password. Press Enter to continue after capturing the login button selector...")

            # Click the 'Log In' button
            login_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
            )
            login_button.click()

            time.sleep(5)

            # Wait for a few seconds to ensure login is successful
           #input("Login successful. Inspect the page and press Enter to continue...")
            try:
                # Now proceed to tweet (you'll need to adapt this part to navigate to the tweet box)
                tweet_button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a"))
                )
                tweet_button.click()
            except TimeoutException:
                print("Could not find the 'Tweet' button on the home page.")
                return

            #input("wait for identifying css")
            tweet_box = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.public-DraftStyleDefault-block"))
            )
            tweet_text = f"My internet speed is {self.down}Mbps down and {self.up}Mbps up. @Airtel, why is my speed below the promised {PROMISED_DOWN}Mbps down and {PROMISED_UP}Mbps up?"
            tweet_box.send_keys(tweet_text)
            #input("wait for identifying css")

            tweet_submit = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']"))
            )
            try:
                tweet_submit.click()
            except:
                self.driver.execute_script("arguments[0].click();", tweet_submit)

            print("Tweet sent successfully!")
while True:
    bot = InternetSpeedTwitterBot(driver_path="/usr/local/bin/chromedriver")
    bot.get_internet_speed()
    bot.tweet_at_provider()
    time.sleep(3600)