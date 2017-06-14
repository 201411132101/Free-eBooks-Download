# encoding: UTF-8
import urllib.request
import re


def get_map():
    url = 'http://www.baquge.tw/files/article/html/0/24'
    response = urllib.request.urlopen(url)
    html = response.read().decode('GBK')

    p = re.compile(r"(?<=<dd>).+?(?=</dd>)")
    res = p.findall(html)
    print(res)

    dic = {}
    for s in res:
        p1 = re.compile(r"(?<=<a href=\").+(?=\">)")
        p2 = re.compile(r"(?<=>).+(?=<)")
        link = p1.search(s).group(0)
        name = p2.search(s).group(0)
        dic[name] = 'http://www.baquge.tw' + link
    return dic


def get_chapter(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('GBK')

    p = re.compile(r"(?<=<div id=\"content\">).+(?=</div>)")
    chp = p.search(html).group(0)

    chp = chp.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '')
    chp = chp.replace('<br /><br />', '\n')

    return chp


fp = open('食人魔的美食盒.txt', 'w')
fp.write('食人魔的美食盒\n' + '作者：黑籍\n')

dic = get_map()
for key in dic:
    chapter = key + '\n'
    chapter += get_chapter(dic[key])
    fp.write(chapter)
    print(key)

fp.close()
