import requests
from bs4 import BeautifulSoup
import json
import re
import urllib

x = 0


def getDouBanImg(page=1):
    global x
    url = requests.get('https://www.dbmeinv.com/index.htm?cid=4&pager_offset={}'.format(page))
    # 获取网站数据
    html = url.text
    # 解析网页
    soup = BeautifulSoup(html, 'html.parser')
    # 获取所有img标签
    girl = soup.find_all('img')
    # print(girl)

    for j in girl:
        # i img标签
        # 获取src路径
        img_src = j.get('src')
        # print(img_src)
        # 下载
        urllib.request.urlretrieve(img_src, '/data/pic/%s.jpg' % x)
        x += 1
        print('正在下载第%s张' % x)


for i in range(1, 10):
    print('正在下载第%s页图片' % i)
    getDouBanImg(i)
