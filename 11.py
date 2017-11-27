import requests,json


def get_urls(key,sum):
    url = "https://image.baidu.com/search/index"
    headers = {
                'cookie': "td_cookie=2373937907; BDqhfp=%E6%B5%B7%E8%BE%B9%26%260-10-1undefined%26%260%26%261; BAIDUID=E26F8B2E16E037DF58FED1FDEAD8A636:FG=1; BIDUPSID=E26F8B2E16E037DF58FED1FDEAD8A636; PSTM=1506000312; pgv_pvi=229598208; td_cookie=2463294905; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E6%B5%B7%E8%BE%B9%22%2C%22%E6%B5%B7%E5%B2%B8%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'accept': "text/plain, */*; q=0.01",
        'referer': "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%B5%B7%E8%BE%B9&oq=%E6%B5%B7%E8%BE%B9&rsp=-1",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'postman-token': "c1717c49-7d6f-b452-0005-026e525e7b43"
    }
    pn = 0
    n = 0

    flag = True
    s = set()

    for pn in range(0,2):
        print ("pn=" + str(pn*30))
        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=" + key + "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=" + key + "&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=" + str(pn*30) + "&rn=30"

        r = requests.get(url,headers = headers)
        try:
            dictinfo = json.loads(r)
            for i in range(0,30):
                temp = dictinfo["data"][i]["thumbURL"]
                s.add(str(temp)+"\n")
        except:
            print ("请求发送失败")
    print (len(s))

    f = open("urls.txt","w")
    for url in s:
        f.write(url)
    f.close()
    print ("get_urls done")
