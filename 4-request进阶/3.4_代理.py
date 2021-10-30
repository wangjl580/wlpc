# 原理：通过第三方机器发送请求

import requests
# 免费代理网站：https://www.zdaye.com/Free/
# 60.216.20.213	8001	透明	山东省 BGP大带宽业务机柜段
# 223.240.98.231	8000	普匿	安徽省合肥市 电信
# 47.111.94.201	7777	高匿	浙江省杭州市 阿里云
# 47.100.255.35	80	普匿	上海市 阿里云
# 218.244.147.59	3128	透明	北京市 鹏博士中关村IDC(万网租用)
# proxies={
#     # "http":"",
#     # "https":"",  #看访问的网站是什么开头的，比如百度就是htttps
#     # "https": "60.216.20.213:8001", #之前这么写就ok
#     # "https": "https://60.216.20.213:8001", # 看当前的版本是否需要加
#     # "https": "https://223.240.98.231:8000",
    # "https": "https://47.111.94.201:7777",
# }

# 以下两条命令用于测试代理是否可以用
# import os
# pro='47.111.94.201:7777'
# os.system(f"curl --connect-timeout 2 -x {pro} https://www.baidu.com/")

proxies={
    "https": "https://47.111.94.201:7777",
}

#---根据上面的测试，代理ip应该是可以用的，但我用以下命令未成功，不知道原因
url='https://www.baidu.com'
resp=requests.get(url, proxies=proxies)  #这样就加入了代理
# resp=requests.get(url)
resp.close()
resp.encoding='utf-8'
# print(resp.text)