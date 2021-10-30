# 获取猪八戒网的一些信息
# 1. 拿页面源代码 看源代码中是否有需要的信息
# 2. 解析和提取数据
import requests
from lxml import etree
import csv

url='https://xinxiang.zbj.com/search/f/?kw=saas'
resp=requests.get(url)
resp.close()
# print(resp.text)

page_content=resp.text
tree=etree.HTML(page_content)
# print(tree)

#确定要提取数据的div块s
divs=tree.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div') 
# print(divs[0])
#可以查看divs[0]中的内容
# result=etree.tostring(divs[0]).decode('utf-8')
# print(result)
zbj_data=[]
with open('zbj.csv',mode='w') as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(['com_name','price','com_intro','com_loc'])
    for div in divs:
        com_name=div.xpath('./div/div/a[1]/div[1]/p/text()')[1].strip('\n')
        # print(com_name)
        com_loc=div.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]
        # print(com_loc)
        price=div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
        # print(price)
        com_intro=div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()')
        com_intro='saas'.join(com_intro)
        # print(com_intro)
        csvWriter.writerow([com_name,price,com_intro,com_loc])
        #这是用来去除重复内容的
        zbj_data.append([com_name,price,com_intro,com_loc])

print('over')

#这是用来去除重复内容的
list1=zbj_data
list2=[]
for i in zbj_data:
    if i not in list2:
        list2.append(i)
# 或者用列表推导式
# [list2.append(i) for i in list1 if not i in list2]  # append别忘记添加参数
# print(list2)

with open('zbj.txt',mode='w') as f:
    for i in list2:
        i=','.join(i)
        f.write(i+'\n')


