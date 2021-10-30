# 抓取网易云音乐的精彩评论

#--爬虫的通用逻辑
# 1. 逻辑都是一样的，首先要确认要抓取的东西是否在源代码中  网址：https://music.163.com/#/song?id=1325905146
# 2. 如果再页面源代码中，通过re xpath beautifulsoup 等解析获取数据，\
# 如果不在，需要通过抓包工具(开发者工具)，获取信息所在的页面 network -> XHR ->刷新页面获取抓包

#----------------
#网易云音乐的网站是嵌套的，评论在嵌套的网页里面 "iframe" 所以会出现，页面源代码，和框架源代码，但需要抓取的评论都不在里面
# 在from Data中有加密的数据

# 2.1 找到未加密的参数
# 2.2 想办法把参数进行加密，加密过程必须参考网页的逻辑 params，encSecKey 这两个参数
# 2.3 请求到网易拿到信息

#48，49，50 以后重新再看： https://www.bilibili.com/video/BV1ZT4y1d7JM?p=49&spm_id_from=pageDriver
import requests
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="  #通过抓包工具获得的评论所在的网页
#请求方式是POST  #开发者工具中查看

# print()

