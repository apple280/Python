import time
import json
import requests
from lxml import etree
def getOnePage(n):
    url=f"https://maoyan.com/board/4?offset={n*10}"
    #伪装浏览器,迷惑服务器(headers=header)  //里面的值是从浏览器F12 network里面可以找到
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    r = requests.get(url,headers=header)
    return r.text
def parse(text):
    #标准化语法
    html = etree.HTML(text)
    #这里需要学习下xpath的语法  names得到的是列表xpath返回的一定是列表
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    #这里取上映时间..同上的方法
    releasetimes = html.xpath('//p[@class="releasetime"]/text()')
    #因为上面是成对出现,需要循环出来   zip是拉链函数..
    item = {}
    for name, releasetime in zip(names, releasetimes):
        item['name'] = name
        item['releaasetime'] = releasetime
        yield item
def save2File(data):
    with open('movie.json','a', encoding='utf-8') as f:
        data = json.dumps(data,ensure_ascii=False) + '\n'
        f.write(data)
def run():
    for n in range(0,10):
        text = getOnePage(n)
        items = parse(text)
        for item in items:
            print(item)   
            save2File(item)
        time.sleep(1)
if __name__=='__main__':
    run()
