import requests
from bs4 import BeautifulSoup
import json
import re

url_midwest_f_teens = "https://dreambank.net/random_sample.cgi?series=midwest_teens-f&min=50&max=500&n=111"
#url_midwest_m_teens = "https://dreambank.net/random_sample.cgi?series=midwest_teens-m&min=50&max=500&n=83"
#url_barb_sanders = "https://dreambank.net/random_sample.cgi?series=b-baseline&min=50&max=300&n=100"

file_name = "dreams_teens_f.json"

response = requests.get(url_midwest_f_teens)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    dreams = []

    for span in soup.find_all('span'):
        for br in span.find_all('br'):
            br.decompose()
        
        dream_content = span.get_text(strip=True)
        dream_only = re.sub(r"^#\d+\s\(.*?\)\s*", "", dream_content)
        dream_only = re.sub(r"\(\d+\swords\)$", "", dream_only).strip()
        dream_only = re.sub(r"\s*\[.*?\]\s*$", "", dream_only).strip()

        if dream_only:
            dreams.append({"dream_content": dream_only})
    
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dreams, f, ensure_ascii=False, indent=4)
    
    print(f"Sny zapisane do '{file_name}'")
else:
    print(f"Nie udało się pobrać strony. Kod statusu: {response.status_code}")
