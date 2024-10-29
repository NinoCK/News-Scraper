import os
import base64
import fitz
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class ArticleProcessor:
    def __init__(self):
        self.pdf_folder = "pdf_files"
        self.txt_folder = "txt_files"
        self._setup_folders()

    def _setup_folders(self):
        if not os.path.exists(self.pdf_folder):
            os.makedirs(self.pdf_folder)
        if not os.path.exists(self.txt_folder):
            os.makedirs(self.txt_folder)

    def process_articles(self, urls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        for i, url in enumerate(urls):
            try:
                driver.get(url)
                time.sleep(2)
                base_file_name = f"article_{i+1}"
                pdf_file_name = os.path.join(self.pdf_folder, base_file_name + ".pdf")
                txt_file_name = os.path.join(self.txt_folder, base_file_name + ".txt")

                result = driver.execute_cdp_cmd("Page.printToPDF", {
                    "format": 'A4',
                    "printBackground": True
                })
                pdf_data = base64.b64decode(result['data'])
                with open(pdf_file_name, "wb") as pdf_file:
                    pdf_file.write(pdf_data)
                print(f"Saved PDF for URL {i+1}: {url}")

                text = self._extract_text_from_pdf(pdf_file_name)
                text = self._truncate_text(text)
                with open(txt_file_name, "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)
                print(f"Extracted text for URL {i+1} and saved to {txt_file_name}")
            except Exception as e:
                print(f"Failed to process {url}: {e}")
        driver.quit()
        print("Finished processing all articles.")

    def _extract_text_from_pdf(self, pdf_file_name):
        text = ""
        doc = fitz.open(pdf_file_name)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text("text")
        doc.close()
        return text

    def _truncate_text(self, text):
        truncation_point_1 = text.find("Ειδήσεις σήμερα:")
        truncation_point_2 = text.find("Ακολουθήστε το")
        truncation_positions = [pos for pos in [truncation_point_1, truncation_point_2] if pos != -1]
        if truncation_positions:
            earliest_truncation_point = min(truncation_positions)
            text = text[:earliest_truncation_point]
        return text