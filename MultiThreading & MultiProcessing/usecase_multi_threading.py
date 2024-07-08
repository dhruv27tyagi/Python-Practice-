'''
Real-world Example: Multithreading for I/O- bound tasks
Scenario: Web Scraping 
Web scraping often involves making numerous network requests to fetch web pages. 
These tasks are I/O-bound because the spend a lot of time waiting for response from servers.
Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently. 


https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_contents(url):
    response=requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread= threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")