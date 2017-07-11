# encoding: UTF-8
import urllib.request
import re


def get_map():
    url = 'http://www.x23us.com/html/4/4958/'
    response = urllib.request.urlopen(url)
    html = response.read().decode('GBK')

    p = re.compile(r"(?<=<td class=\"L\">).+?(?=</td>)")
    res = p.findall(html)
    print(res)

    dic = {}
    for s in res:
        p1 = re.compile(r"(?<=<a href=\").+(?=\">)")
        p2 = re.compile(r"(?<=>).+(?=<)")
        link = p1.search(s).group(0)
        name = p2.search(s).group(0)
        dic[name] = url + link
    return dic


def get_chapter(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('GBK')

    p = re.compile(r"(?<=<dd id=\"contents\">).+(?=</dd>)")
    chp = p.search(html).group(0)

    chp = chp.replace('&nbsp;', '')
    chp = chp.replace('<br /><br />', '\n')

    return chp


fp = open('恶魔书.txt', 'w')
fp.write('恶魔书\n' + '作者：柳水心\n')

dic = get_map()
for key in dic:
    chapter = key + '\n'
    chapter += get_chapter(dic[key]) + '\n'
    fp.write(chapter)
    print(key)

fp.close()
