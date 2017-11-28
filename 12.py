import json
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests

def get_page_index(offset,keyword):
    data ={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
    url = 'https://www.toutiao.com/search_content/?'+ urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('fail')
        return None

def parse_page_index(html):
    data = json.loads(html)
    print(data.keys())
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('fail detail',url)
        return None

def main():
    html = get_page_index(0,'街拍')
    for url in parse_page_index(html):
        print(url)



if __name__ == '__main__':
    main()