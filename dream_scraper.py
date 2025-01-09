import requests
from bs4 import BeautifulSoup
import json
import re

dream_urls = [
    "https://dreambank.net/random_sample.cgi?series=izzy12&min=50&max=500&n=100",
    "https://dreambank.net/random_sample.cgi?series=phil2&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=miami-home&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=kenneth&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=peru-m&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=midwest_teens-f&min=50&max=500&n=111", 
    "https://dreambank.net/random_sample.cgi?series=midwest_teens-m&min=50&max=500&n=83",
    "https://dreambank.net/random_sample.cgi?series=b-baseline&min=50&max=300&n=100",
    "https://dreambank.net/random_sample.cgi?series=madeline4-postgrad&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=jasmine&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=emma&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=vietnam_vet3&min=10&max=1000&n=10000",
    "https://dreambank.net/random_sample.cgi?series=bea1&min=10&max=1000&n=10000"
]

file_name = "dreams/dreamsall.json"
all_dreams = []

for url in dream_urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for span in soup.find_all('span'):
            for br in span.find_all('br'):
                br.decompose()
            dream_content = span.get_text(strip=True)
            dream_only = re.sub(r"^#\S+\s\(.*?\)\s*", "", dream_content)
            dream_only = re.sub(r"\(\d+\swords\)$", "", dream_only).strip()
            dream_only = re.sub(r"\s*\[.*?\]\s*$", "", dream_only).strip()
            if dream_only and not dream_only.startswith(("#", ")", "(")):
                all_dreams.append({"dream_content": dream_only})

print(len(all_dreams))
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(all_dreams, f, ensure_ascii=False, indent=4)

print(f"Sny zapisane do '{file_name}'")
