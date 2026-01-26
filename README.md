# Twitter Internet Speed Complaint Bot 🚀

An automated Python bot that checks your internet speed using **Speedtest.net** and posts a complaint tweet to your ISP on **Twitter (X)** if the speed is below the promised limits.

This project demonstrates **Selenium WebDriver automation**, **object-oriented programming**, and **real-world browser interaction**.

---

## 📌 Features

* 🌐 Automatically measures **download and upload speed**
* 🤖 Uses **Selenium WebDriver** to control Chrome
* 📊 Extracts speed results using **CSS selectors**
* 🐦 Logs into Twitter and posts a complaint tweet
* 🔁 Runs **every hour** to continuously monitor internet performance

---

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **Google Chrome**
* **ChromeDriver**

---

## 🧠 Concepts Used

* Classes & constructors
* Explicit waits (`WebDriverWait`)
* CSS selectors & XPath
* Exception handling (`TimeoutException`)
* Browser automation
* Infinite loops with scheduled execution

---

## ⚙️ Prerequisites

Before running the bot, ensure you have:

* Python 3.x installed
* Google Chrome installed
* ChromeDriver installed and accessible

Check Chrome version:

```bash
google-chrome --version
```

Download matching ChromeDriver:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/twitter-speed-complaint-bot.git
cd twitter-speed-complaint-bot
```

2. Install dependencies:

```bash
pip install selenium
```

3. Update credentials inside the script:

```python
TWITTER_ID = "your phone number or email"
TWITTER_PASSWORD = "your password"
```

4. Update ChromeDriver path:

```python
bot = InternetSpeedTwitterBot(driver_path="/usr/local/bin/chromedriver")
```

---

## 🚦 How It Works

1. Opens **[https://www.speedtest.net](https://www.speedtest.net)**
2. Runs an internet speed test
3. Extracts:

   * Download speed
   * Upload speed
4. Compares against promised ISP speeds
5. Logs into Twitter
6. Tweets a complaint tagging the ISP
7. Sleeps for **1 hour** and repeats

---

## 🐦 Sample Tweet

```
My internet speed is 45Mbps down and 12Mbps up.
@Airtel, why is my speed below the promised 1000Mbps down and 100Mbps up?
```

---

## ⚠️ Important Notes

* Twitter frequently updates its UI — selectors may need updates
* Use this project for **educational purposes**
* Avoid excessive automation to prevent account restrictions
* Consider using environment variables instead of hardcoding credentials

---

## 🔮 Future Improvements

* Use Twitter API instead of UI automation
* Store speed history in a database
* Add email/Slack notifications
* Headless browser support
* Dockerize the application

---

## 👨‍💻 Author

**Arnab
