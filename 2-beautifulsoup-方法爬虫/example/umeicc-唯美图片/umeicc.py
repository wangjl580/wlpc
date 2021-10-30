# 下载唯美壁纸的图片
# 1 拿到主页面的源代码，提取子页面的herf
# 2 从子页面找到下载地址img->src 里面的值
# 3 下载大图

# bs学习参考网址：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

import requests
from bs4 import BeautifulSoup
import time,os

url="https://umei.cc/bizhitupian/weimeibizhi/"
resp=requests.get(url)
resp.encoding='utf-8'  #与页面的meta->charset 保持一致
resp.close()

main_page=BeautifulSoup(resp.text,'html.parser') #html.parser 指定html解析器
# print(main_page)
# alist=main_page.find_all('div', class_='TypeList') #把范围第一次缩小
# print(alist)
alist=main_page.find('div', class_='TypeList').find_all('a') #找到里面的所有a标签
# 可以根据提取出的数据，如alist 再次进行bs解析，如soup=BeautifulSoup(alist,'html.parser'); soup.find()等
num=1
for a in alist:
    herf=a.get('href') #通过get直接拿到属性值
    # print(herf)
    child_url=url+str(herf).split('/')[-1]
    # print(child_url)
    #拿到子页面的源代码
    resp=requests.get(child_url)
    resp.encoding='utf-8'
    resp.close()
    child_page_content=resp.text
    #从子页面拿到下载路径
    child_page=BeautifulSoup(child_page_content,'html.parser')
    img=child_page.find('div',class_="ImageBody",id="ArticleId{dede:field.reid/}")\
    .find('p').find('img')  #多次缩小范围
    img_url=img.get('src')
    # print(img_url)
    #下载图片
    img_resp=requests.get(img_url) #直接请求图片网址
    img_resp.close()
    img_resp.content #这里拿到的是字节
    # img_name=img_url.split('/')[-1]  #根据/分离字符串取最后一个
    img_name=str(num)+'.jpg'
    # print(img_name)
    if not os.path.exists('img'):  #建立文件夹
        os.mkdir('img')
    with open('img/'+img_name,mode='wb') as f: #写入文件
        f.write(img_resp.content)
    num=num+1
    print('over =>','img/'+img_name)
    time.sleep(0.2)
print('all over')

    





