import threading
import time
import requests 
from bs4 import BeautifulSoup

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(len(soup.text))
    
threads = []
urls = [
    'https://www.python.org/',
    'https://www.github.com/',
    'https://www.stackoverflow.com/',
]

for url in urls:
    thread = threading.Thread(target = fetch_content, args = (url,))
    threads.append(thread)
    thread.start()
    
for th in threads:
    th.join()