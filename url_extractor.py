import re

class URLExtractor:
    def __init__(self, page_source_file):
        self.page_source_file = page_source_file

    def extract_hrefs(self):
        with open(self.page_source_file, "r", encoding="utf-8") as file:
            html_content = file.read()
        hrefs = re.findall(r'href=["\'](.*?)["\']', html_content)
        url_pattern = re.compile(r'https://www\.protothema\.gr/world/article/\d+/[\w-]+/')
        filtered_urls = set(href for href in hrefs if url_pattern.match(href))
        print(f"Found {len(filtered_urls)} valid URLs")
        return list(filtered_urls)[:5]