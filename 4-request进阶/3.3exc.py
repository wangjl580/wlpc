import requests

url="https://www.pearvideo.com/video_1694346"


vedioStatusUrl='https://www.pearvideo.com/videoStatus.jsp?contId=1694346&mrd=0.3471724873210409'
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Referer": "https://www.pearvideo.com/video_1694346",
}
resp=requests.get(vedioStatusUrl,headers=headers)
resp.close()
# print(resp.text)
dic=resp.json()

srcUrl=dic["videoInfo"]['videos']['srcUrl']
# print(srcUrl)
systemTime=dic['systemTime']
contId=url.split('_')[1]
# print(contId)
srcUrl=str(srcUrl).replace(systemTime,f'cont-{contId}')
# print(srcUrl)

print('开始下载...')
with open('2.mp4',mode='wb') as f:
    resp=requests.get(srcUrl)
    resp.close()
    f.write(resp.content)

print('over')






# https://video.pearvideo.com/mp4/third/20200829/1635576924289-10703582-100942-hd.mp4
# https://video.pearvideo.com/mp4/third/20200829/cont-1694346-10703582-100942-hd.mp4
