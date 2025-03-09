import requests
from bs4 import BeautifulSoup
import re
import json
import time
from random import randint

query_dict = {}

def scrape_website(url, query_str):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find_all('a', attrs={"class": "result__a"})
    hrefs = [a['href'] for a in result]
  
    query_dict[query_str] = []
    for href in hrefs:
        query_dict[query_str].append(href)
    # result = soup.find_all("script")
    # result_str = [str(tag) for tag in result]
    # for st in result_str:
    #    match = re.search('window\.MESON\.initialState\s*=\s*(\{.*?\});', st, re.DOTALL)
    #    if match: 
    #     json_str = match.group(1)
        
    # try:
    #     initial_state = json.loads(json_str)
          
    #     querySearch = initial_state.get('search',{}).get('webResults', {}).get('results', [])
    #     query_dict[query_str] = []
    #     for query in querySearch:
    #         query_dict[query_str].append(query["url"])
       
    # except json.JSONDecodeError as e:
    #     print("No match found for window.MESON.initialState")
    
            
if __name__ == "__main__":
    with open('100QueriesSet4.txt', 'r') as file:
        for line in file:
            line.strip()
            website_url = 'https://html.duckduckgo.com/html/?q={}'.format(line)
            scrape_website(website_url, line)
            print(query_dict)
            time.sleep(5)
           
            
with open('hw1-duck.json', 'w') as file:
    print(json.dumps(query_dict), file=file)
