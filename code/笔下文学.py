# encoding: UTF-8
import urllib.request
import re

# 尚未完成
# 下载其它书籍只需改动 get_map() 中的 url
# 然后加上大量的调试？


def get_map():
    url = 'http://www.bxwx9.org/b/7/7779/'
    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')

    p = re.compile(r"(?<=<div id=\"title\">).+?(?=全集下载)")
    res = p.search(html).group(0)
    title = res.strip()
    print(title)

    p = re.compile(r"(?<=<div id=\"info\">).+?</a>")
    res = p.search(html).group(0)
    p = re.compile(r"(?<=>).+?(?=</a>)")
    res = p.search(res).group(0)
    author = res.strip()
    print(author)

    p = re.compile(r"(?<=<dd).+?(?=</dd>)")
    res = p.findall(html)
    # print(res[0])

    dic = {}
    for s in res:
        if s.find('</a>') == -1:
            continue
        p1 = re.compile(r"(?<=<a href=\").+(?=\">)")
        p2 = re.compile(r"(?<=\").+(?=</a>)")
        link = p1.search(s).group(0)
        name = p2.search(s).group(0)
        dic[name] = url + link
    return dic, title, author


def get_chapter(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('GBK')

    p = re.compile(r"(?<=<div id=\"adright\"></div>).+(?=</div>)")
    chp = p.search(html).group(0)

    chp = chp.replace('&nbsp;', '')
    chp = chp.replace('<br /><br />', '\n')

    return chp


def main():
    [dic, title, author] = get_map()
    fp = open(title + '.txt', 'w')
    fp.write(title + '\n' + '作者：' + author + '\n')

    debug = 0
    keys = sorted(dic)
    for key in keys:
        debug += 1
        if debug == 10:
            break
        chapter = key + '\n'
        print('debug:' + dic[key] + '\n')
        chapter += get_chapter(dic[key]) + '\n'
        fp.write(chapter)
        print(key)

    fp.close()

main()
