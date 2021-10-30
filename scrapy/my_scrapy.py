'''
scrapy 的用法
'''

# pip install scrapy
#可能需要先安装以下插件
# pip install --upgrade incremental
# pip install Twisted  #是scrapy低层的框架

import scrapy
#--beatifulsoup 是库
#scrapy 是框架

# html=scrapy.Request("http://stockpage.10jqka.com.cn/600004/")  #同花顺子网
html=scrapy.Request('http://stockpage.10jqka.com.cn/600004/company/')
print(html)
