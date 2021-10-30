#登陆用户名之后才能爬取数据，此时就要用session
# 登陆17K小说网后，爬取书架上的数据，https://passport.17k.com/ck/user/login

#1.登陆  得到cookie
#2.带着cookie请求书架的url ->书架上的内容

#必须得把上面两步的操作连起来
# 我们可以使用session进行请求  session可以认为是一连串的请求，在这个过程中的cookie不会丢失，session 适用于上面的需求
#session 称为会话
# A->B
# B->A
# A->B
import requests

session=requests.session()
data={
    "loginName": "18790518707",
    "password": "1011320sr"
}

# 1 登陆
url='https://passport.17k.com/ck/user/login'
resp=session.post(url,data=data)  #post方法需要带上数据
# print(resp) #看响应状态
# print(resp.text) #判断登陆是否成功
# print(resp.cookies)  #看响应的cookie  response headers 里面查看

# 2 书架上的数据
# requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919') #不能用request.get()因为这是一个新的请求，并不知道cookie
resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919') #session中是有cookie的
# print(resp.text)
# print(resp.json()) #查看json
resp.encoding='utf-8'
dic=resp.json()
# print(dic)
print(dic['data'][1]['introduction']) #对字典的操作，对于字典的层次结构，可以看开发者工具中的network->Fetch/XHR->字典

#方法二
#错误的演示
# resp=requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919') #书架网页
# print(resp.text) #如果直接请求书架网页用户登陆错误
#正确的演示
resp=requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919',headers={
    "Cookie": "GUID=7e7d6415-da0b-48f8-b3fd-2495d39df2e3; Hm_lvt_9793f42b498361373512340937deb2a0=1635565495; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F02%252F42%252F39%252F84553942.jpg-88x88%253Fv%253D1635558855000%26id%3D84553942%26nickname%3D%25E9%25BA%25BB%25E8%25BE%25A3%25E6%2599%258B%25E7%25BA%25A7%26e%3D1651118034%26s%3Deae6f7ba62abb909; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2284553942%22%2C%22%24device_id%22%3A%2217ccf4ce2f76e9-0d5317bf83b008-1c306851-1296000-17ccf4ce2f8495%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%227e7d6415-da0b-48f8-b3fd-2495d39df2e3%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1635567665"
}) #书架网页
# print(resp.json())
#实际上方法一的内部也是使用了包含cookie的请求头

