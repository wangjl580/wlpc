import sys, os, time
import urllib.request, urllib.error, urllib.request, urllib.parse
import pprint as pp
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #取消全局验证,然后使用urllib.urlopen('url')

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

def download_img(url, dst_path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': userAgent})
        res = urllib.request.urlopen(req)
        img_data = res.read()
        with open(dst_path, mode="wb") as f:
            f.write(img_data)
    except urllib.error.URLError as ex:
        print(ex)

# if (len(sys.argv) < 2):
#     print("\n", "usage: py main.py [url]")
#     exit(0)

# 命令行url取得
# url = sys.argv[1]
url="https://blog.csdn.net/bookssea/article/details/107309591"

# url请求
req = urllib.request.Request(url, headers={'User-Agent': userAgent})
html = urllib.request.urlopen(req)

# 解析获取的html
soup = BeautifulSoup(html, "html.parser")
# print(soup.html)
# print(soup.text)

# 取出所有的图片标记
img_list = soup.find_all('img')

# 整理图片的url，生成新的数组
url_list = []
for img in img_list:
    if img.get('src') == None:
        continue

    tmp = img['src'].strip()
    if tmp.startswith("https://") or tmp.startswith("http://"):
        # url_list.append(tmp)
        pass
    else:
        # url_list.append(urllib.parse.urljoin(url, tmp))
        tmp = urllib.parse.urljoin(url, tmp)
    
    if not tmp in url_list:
        url_list.append(tmp)
# pp.pprint(url_list, indent=4)

# 建立下载文件夹
download_dir = './out'
if not os.path.exists(download_dir):
    os.mkdir(download_dir)

# 下载处理
digits_width = len(str(len(url_list)))
count = 0
for url in url_list:
    count = count + 1

    # 文件名整理：01->
    fmt_url = url
    if fmt_url.find("?") > -1:
        fmt_url = fmt_url[0:fmt_url.find("?")]
    file, ext = os.path.splitext(fmt_url)
    filename = str(count).zfill(digits_width) + ext
    if len(ext) == 0:
        filename = filename + ".png"

    dst_path = os.path.join(download_dir, filename)
    print(url)
    print("", "->", dst_path)

    time.sleep(0.1) # 下载延迟，减少服务器负荷
    download_img(url, dst_path)

