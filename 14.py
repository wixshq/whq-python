
import  requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_taylor_music(id):
    data = {
        "id":id
    }
    url = 'http://music.163.com/artist'
    response = requests.get(url,params=data)
    try:
        if response.status_code == 200 :
            return response.text
        return None
    except RequestException:
        print('fail')
        return None

def parse_taylor_music():
    soup = BeautifulSoup(get_taylor_music(44266), 'lxml')
    f = open("taylorMusic.txt", "w")
    for li in soup.find_all('ul')[1]:
        r = li.find_all('a')
        f.write(r[0].string + '\n')
        print(r[0].string)
    f.close()

def main():
   parse_taylor_music()

if __name__ == '__main__':
    main()