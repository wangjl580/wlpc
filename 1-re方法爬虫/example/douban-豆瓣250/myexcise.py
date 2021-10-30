from os import truncate
import re
import requests
import csv
import time

print('正在抓取数据...')
# 1.解析url
url='https://xinxiang.zbj.com/search/f/?kw=saas'
resp=requests.get(url)
resp.close()
page_content=resp.text
# print(page_content)

# 2.确定搜索模式
patten=re.compile(r'item-wrap service-new j-sp-item-wrap.*?<p class=\'text-overflow\'>.*?</span>(?P<com_name>.*?)</p>'
                  r'.*?service-icons clearfix.*?<span title=.*?>(?P<com_loc>.*?)</span>'
                  r'.*?>\¥(?P<price>.*?)</span>'
                  r".*?<p class=\'title\'>(?P<com_inf>.*?)</p>",re.S)


result=patten.finditer(page_content)
# print(result)
with open('test.csv',mode='w') as f:
    csvWriter=csv.writer(f)
    for it in result:
        # 通过列表数据写入
        com_name=it.group('com_name').strip()
        com_loc=it.group('com_loc')
        price=it.group('price')
        com_inf=it.group('com_inf').replace('<hl>','').replace('</hl>','')
        # csvWriter.writerow([com_name,com_loc,price,com_inf])
        print(com_name,com_loc,price,com_inf,sep=',',file=f,flush=True)
        # 通过字典数据写入
        dic=it.groupdict()
        dic['com_name']=dic['com_name'].strip()
        dic['com_inf']=dic['com_inf'].replace('<hl>','').replace('</hl>','')
        # csvWriter.writerow(dic.values())

print('over')

