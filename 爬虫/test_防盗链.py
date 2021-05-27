# 1.拿到contID
# 2.拿到videoStatus返回 的json. --> srcURL
# 3.srcURL里面的内容进行修整
# 4.下载视频
import requests

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1728960"
contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.09719452204894763"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0",
    # 防盗链:溯源：当前本次请求的上一级是谁
    "Referer": url

}
resp = requests.get(videoStatusUrl, headers=headers)
dict = resp.json()
srcUrl = dict["videoInfo"]['videos']['srcUrl']
systemTime = dict['systemTime']

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)

# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
