# News Article Scraper and Analyzer

This repository contains a set of Python scripts designed to scrape news articles from the "Protothema" website, process the content into PDFs and text files, and analyze the articles using a local Llama-based API for generating summaries.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Modules Overview](#modules-overview)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NinoCK/News-Scraper.git
   cd news-scraper-analyzer
   ```

2. **Install dependencies**:
   This project uses several external libraries. Install them using:
   ```bash
   pip install selenium webdriver_manager requests pymupdf

   ```

3. **Setup ChromeDriver**:
   The scripts use ChromeDriver for Selenium to handle browser automation. Ensure ChromeDriver is in your PATH or install it using `webdriver_manager` (already handled in code).

## Usage

1. Run the main script to start the scraping, processing, and analysis:
   ```bash
   python main.py
   ```

   This will:
   - Scrape the "Protothema" website and save the HTML source.
   - Extract article URLs from the HTML source.
   - Save each article as a PDF and extract the text content.
   - Summarize each article using the Llama API.

## Modules Overview

1. **main.py**  
   This is the entry point of the application. It orchestrates the web scraping, URL extraction, article processing, and news analysis.

2. **web_scraper.py**  
   Contains the `WebScraper` class, which scrapes the HTML content from the specified URL and saves it to `page_source.txt`.

3. **url_extractor.py**  
   Defines the `URLExtractor` class, which reads the saved HTML file, extracts valid article URLs, and returns a list of up to 5 URLs.

4. **article_processor.py**  
   Implements the `ArticleProcessor` class. It:
   - Converts each article page to a PDF.
   - Extracts text from the PDF and saves it to a text file.
   - Includes text truncation to remove specific unwanted sections.

5. **news_analyzer.py**  
   Contains the `NewsAnalyzer` class, which uses the Llama API to generate summaries of each article. The API request is sent to `http://localhost:11434/api/generate`.
