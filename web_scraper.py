import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page_source_file = "page_source.txt"

    def scrape_website(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(self.url)
        time.sleep(2)
        page_source = driver.page_source
        with open(self.page_source_file, "w", encoding="utf-8") as file:
            file.write(page_source)
        driver.quit()
        print("HTML content has been saved to page_source.txt")
