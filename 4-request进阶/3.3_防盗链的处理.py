#---下载梨视频网页里面的一个视频 ：https://www.pearvideo.com/
# 1 拿到contId
# 2 拿到vedioStatus返回的json -> 拿到json里面的srcURL
# 3 srcURL里面的内容进行修改
# 4 下载视频
import requests

#拉取视频的网址
# 1 拿到contId
url='https://www.pearvideo.com/video_1735409'
contId=url.split("_")[1]
# print(contId)

# 2 拿到vedioStatus返回的json -> 拿到json里面的srcURL
# vedioStatusURL= "https://www.pearvideo.com/videoStatus.jsp?contId=1735409&mrd=0.12371440604577133"
vedioStatusURL = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.12371440604577133" #mrd就是个随机数，想换就换

# print(vedioStatusURL)
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    #防盗链：溯源->当前请求的上一级是什么
    # "Referer": "https://www.pearvideo.com/video_1735409"
    "Referer": url
}

resp=requests.get(vedioStatusURL,headers=headers)
resp.close()
# print(resp.text)
# print(resp.json())
dic=resp.json()
srcUrl=dic["videoInfo"]['videos']['srcUrl']
systemTime=dic['systemTime']
# 3 srcURL里面的内容进行修改
srcUrl=str(srcUrl).replace(systemTime,f"cont-{contId}") 
# https://video.pearvideo.com/mp4/third/20210716/cont-1735409-10097838-163135-hd.mp4
# print(srcUrl) 

# 4 下载视频
print('开始下载...')
resp=requests.get(srcUrl)
resp.close()
with open('1.mp4',mode='wb') as f: #记住需要wb
    f.write(resp.content)

print('over')



