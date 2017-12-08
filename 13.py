import json
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests




def get_page_index(offset,keyword):
    data = {
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoloda':'true',
        'count':20,
        'cur_tab':3
    }

    headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8',
        'Connection': 'keep - alive',
        'Cookie': 'laravel_session = eyJpdiI6ImJtendRSDd2N01ibDFBNVpvSnFycFE9PSIsInZhbHVlIjoiVnBsWDk3QlJHekFuY3NcL01pakxzMHJYNHlnMUtOSDJmc3dKTm9sR3BDTWZ5cUdMVm5XWllFVGRmY2ZoNmNlZitOU0J1MVwvWFwvbU1ySFNKWkZJWEtEOVE9PSIsIm1hYyI6ImY0ZGFjMTAwOGJjZGI5Njk4MzMzZTQ5MTUyYzczODA1NzczYThlZjRjZTRkZGExNzNjYTllYTQ0YjQ4OTQyNzAifQ % 3D % 3D;PASS_ID = 0c72b6b09ba24f1bab78d70f120f893c;auc_token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdWMiLCJ1aWQiOjQyMCwibmFtZSI6IuWHieS7iyIsImp0aSI6IktyQVJqNTNpZUwiLCJleHAiOjE1MTIwNjA4MzM5NjV9.TvKPU5BK9ngLRYMCJ4B2B4m1hP679FyfXmDjyaDUQb4;Hm_lvt_df3f672cabd7e98ed9defe423766f3f5=1510663541,1510672638,1510812751,1511882227; Hm_lpvt_df3f672cabd7e98ed9defe423766f3f5=1512111683',
        'Host': 'mms.qa3.test.yiran.com',
        'Referer': 'http: // mms.qa3.test.yiran.com / Pdd.html',
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 62.0.3202.94Safari / 537.36'

    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('fail')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def main():
    html = get_page_index(0,'雪景')
    f = open('urls1.txt','w')
    for url in parse_page_index(html):
        f.write(url + '\n')
        print(url)
    f.close()


if __name__ == '__main__':
    main()