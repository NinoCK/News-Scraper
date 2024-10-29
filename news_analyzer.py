import requests
import json
import os

class NewsAnalyzer:
    def __init__(self, api_url="http://localhost:11434/api/generate"):
        self.api_url = api_url
        self.txt_folder = "txt_files"

    def analyze_news_with_ollama(self):
        for txt_file_name in os.listdir(self.txt_folder):
            txt_file_path = os.path.join(self.txt_folder, txt_file_name)
            with open(txt_file_path, "r", encoding="utf-8") as file:
                text = file.read()
            prompt = f"Please summarize the following news article:\n\n{text}"
            payload = {
                "model": "llama3.2:1b",
                "prompt": prompt
            }
            try:
                response = requests.post(self.api_url, json=payload, stream=True)
                if response.status_code == 200:
                    output = ''
                    for line in response.iter_lines():
                        if line:
                            data = line.decode('utf-8')
                            chunk = json.loads(data)
                            output += chunk.get('response', '')
                    print(f"News summary for {txt_file_name}:")
                    print(output)
                else:
                    print(f"Failed to analyze {txt_file_name}: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"Failed to analyze {txt_file_name} with Ollama: {e}")