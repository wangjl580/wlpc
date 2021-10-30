# 爬取电影天堂网站数据
# 1. 定位到2021必看片
# 2. 从中提取到子页面的链接地址
# 3. 请求子页面的链接地址，拿到下载地址和电影名

import requests
import re
import csv

domain="https://www.dytt89.com"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}
resp=requests.get(domain,headers=headers)#,verify=False) #去掉安全验证，如果出现SSLError可以尝试使用取消验证
# print(resp.request.headers)
resp.close()
resp.encoding='gb2312'  # 指定字符集，要与页面的源代码中的charset=gb2312 一致
# print(resp.text)

obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)

#拿到ul里面的li
result1 = obj1.finditer(resp.text)
for it in result1:
    ul=it.group('ul')
    print(ul)
# ul=list(result1)[0].group('ul'); print(ul)

obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title=", re.S)
result2= obj2.finditer(ul)
href=[]
for it in result2:
    href.append(it.group('href'))
# print(href)

sub_url=[] 
for i in range(len(href)):
    sub_url.append(domain+href[i])
# print(sub_url[0])


for i in sub_url:
#     print(i)

    resp=requests.get(i,headers=headers)
    resp.encoding='gb2312'
    # print(resp.text)
    resp.close()
    obj3=re.compile(r'<div class="co_area2">.*?<h1>(?P<h1>.*?)</h1>.*?'
                    r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">.*?<a href="(?P<download>.*?)"', re.S)
                    # r'<div class=player_list>.*?<a href="(?P<download>.*?)">', re.S)

    result=obj3.finditer(resp.text)
    with open('data1.csv',mode='a+') as f:
        csvwriter=csv.writer(f)
        for it in result:
        #     h1=it.group('h1')
        #     download=it.group('download')
        #     print(h1,download)
            dic=it.groupdict()
            csvwriter.writerow(dic.values())
            print(dic.values())

print('over')

