import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #取消全局验证,然后使用urllib.urlopen('url')
from bs4 import BeautifulSoup
import re

def main():
    baseurl="https://movie.douban.com/top250?start="
    print('爬虫中...')
    datalist=getDate(baseurl)
    savefile="allchakan.txt"
    saveData(datalist,savefile)
    print('爬虫完毕')

def askURL(url):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'} ##模拟浏览器访问
    ret=urllib.request.Request(url, headers=headers)
    res=urllib.request.urlopen(ret) # 返回服务器响应的类文件对象
    html=res.read().decode('utf-8')
    return html

# print(soup.meta)  #找到第一个meta标签的内容
# print(soup.find_all("meta")) #找到所有的meta标签内容
#正则表达式 和soup混合使用
# result=soup.find_all("span")
# print(result)
# r=re.findall(r'.*推荐.*',str(result))
# print(r)

findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，标售规则影片详情链接的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"') #, re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
findEm = re.compile(r'<em class="">(.*)</em')

def getDate(baseurl):
    datalist=[]
    for i in range(0,10):  #10
        url=baseurl+str(i*25)
        html=askURL(url)
        soup=BeautifulSoup(html,'html.parser')
        items=soup.find_all('div', class_="item")
        for item in items:
            data=[]
            item=str(item)
            em=findEm.findall(item)[0]
            data.append(em)  #8
            link=findLink.findall(item)[0]  #print(link)
            data.append(link)  #1
            imgSrc=findImgSrc.findall(item)[0]
            data.append(imgSrc) #2
            title= findTitle.findall(item)
            ctitle=title[0] 
            data.append(ctitle) #3
            rating=findRating.findall(item)[0]
            data.append(rating) #4
            judgeNum=findJudge.findall(item)[0]
            data.append(judgeNum) #5
            inq=findInq.findall(item)
            if len(inq) != 0:
                inq=inq[0].replace("。","")
            else:
                inq=" "
            data.append(inq) #6
            findRI=re.compile(r'<br/>\s*(.*?)\s*</p>',re.S)
            # findRI=re.compile(r'<p class="">(.*?)</p>', re.S)
            ri=findRI.findall(item)[0]
            data.append(ri)  #7
            datalist.append(data)
    return datalist

def saveData(datalist,savefile):
    with open(savefile,'w+') as f:
        for i in range(0,len(datalist)): #25 len(datalist)
            # print(datalist[i])
            data=datalist[i]
            # a=data[5]+'\t'+data[6];f.write(a)
            for j in range(0,len(data)): #8
                print(data[j],end='\t',file=f)
            print(end='\n',file=f)

if __name__ == "__main__":
    main()
