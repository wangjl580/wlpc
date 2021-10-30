# 从北京新发地网页抓取蔬菜价格数据

import requests
import re
import os

def myWrite(i):  #从第i个网页,抓取数据写入out/data{i}.csv文件
    data={
        "limit": "20",
        "current": f"{i}",  #通过更改current的值可以请求获得不同页面的数据，当然也可以改limit的值。
    }
    #首先看页面源代码中是否含有需要抓取的数据，发现没有，然后通过抓包工具(开发者工具)判断数据所在的网页，
    #而且我发现headers文件中的请求方法变成了post, 在最下面可以看到请求的数据表
    url="http://www.xinfadi.com.cn/getPriceData.html"
    resp=requests.post(url,data)
    resp.close()
    # print(resp.text)
    
    # 这里通过re方法获取数据，当然也可以通过beautifulsoup方法
    pattern = re.compile(r'"prodName":"(?P<name>.*?)","prodCatid":.*?,"prodCat":".*?",'
                        r'"prodPcatid":null,"prodPcat":"","lowPrice":"(?P<lowPrice>.*?)",'
                        r'"highPrice":"(?P<highPrice>.*?)","avgPrice":"(?P<avePrice>.*?)",'
                        r'"place":"(?P<place>.*?)"',re.S)
    result=re.finditer(pattern,resp.text)
    
    if not os.path.isdir('out'):
        os.mkdir('out')
     
    #写入数据
    fname=f'./out/data{i}.csv'
    with open(fname,mode='w') as f:
        for it in result:
            name=it.group('name')
            # print(name)
            lowPrice=it.group('lowPrice')
            # print(lowPrice)
            highPrice=it.group('highPrice')
            # print(highPrice)
            avePrice=it.group("avePrice")
            # print(avePrice)
            place=it.group("place")
            # print(place)
            dic=it.groupdict()
            print(*list(dic.values()),file=f,sep=',')
            # a=','.join(list(dic.values()));print(a,file=f)

from concurrent.futures import ThreadPoolExecutor

print("开始抓取数据...")
with ThreadPoolExecutor(10) as t:
    for j in range(1,21):
        t.submit(myWrite,i=j)

print("over")


