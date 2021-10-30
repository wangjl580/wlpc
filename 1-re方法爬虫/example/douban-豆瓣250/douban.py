#拿到豆瓣250电影信息列表
#拿到源代码  request 
#通过re来提取需要的信息
import requests
import re
import csv

url="https://movie.douban.com/top250"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15", 
    'Connection': 'keep-alive','Keep-Alive': 'timeout=3',
}
# 注意：headers中有很多内容，主要常用的就是user-agent 和 host，
# 他们是以键对的形式展现出来，如果user-agent 以字典键对形式作为headers的内容，就可以反爬成功，就不需要其他键对；
# 否则，需要加入headers下的更多键对形式。

resp=requests.get(url,headers=headers)
# print(resp.headers) #取得服务器返回来的请求头:
# print(resp.request.headers)  #获得我们发送的请求头:
# print(resp.text)
resp.close()  #关掉请求
page_content = resp.text

#解析数据
obj= re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>'
                r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
#开始匹配
result=obj.finditer(page_content)

# '''
# 用写入列表的形式
with open('data.csv',mode='w') as f:
    csvwriter=csv.writer(f) 
    head=['name','year','rating','num']  #不要用大括号，因为字典在写入的时候顺序随机
    csvwriter.writerow(head)
    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())  #对年份处理  前面有空格
        # print(it.group("rating"))
        # print(it.group("num"))
        dic=it.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic.values())  #写入的是字典的值
print('over')
# '''

#用写入字典的形式，顺序会随机
'''
with open('data.csv',mode='w') as f:
    head={'name','year','rating','num'}
    csvwriter= csv.DictWriter(f,head)
    csvwriter.writeheader()
    for it in result:
        dic=it.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic)  #写入字典需要用csv.DictWriter

print('over')
'''

