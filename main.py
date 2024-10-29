from web_scraper import WebScraper
from url_extractor import URLExtractor
from article_processor import ArticleProcessor
from news_analyzer import NewsAnalyzer

if __name__ == "__main__":
    url = "https://www.protothema.gr/"
    scraper = WebScraper(url)
    scraper.scrape_website()

    extractor = URLExtractor("page_source.txt")
    urls = extractor.extract_hrefs()

    processor = ArticleProcessor()
    processor.process_articles(urls)

    analyzer = NewsAnalyzer()
    analyzer.analyze_news_with_ollama()
