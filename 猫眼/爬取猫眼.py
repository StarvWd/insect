import requests
import re
import json

def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0(Macintosh; Inter Mac OS X 10_13_3)AppleWebKit/537.36 (KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    res = requests.get(url, headers = headers)
    return res.text

def parse_one_page(html):
    print(html)
    pattern = re.compile('<dd>.*?board-index-.*?>(.*?)<.*?title="(.*?)".*?star">(.*?)<.*?releasetime">上映时间：(.*?)<.*?integer">(.*?)<.*?fraction">(.*?)<.*?', re.S)
    items = re.findall(pattern, html)
    #print(items)
    for item in items:
        yield({'index':item[0], 'title':item[1], 'actor':item[2].strip()[3:], 'time': item[3], 'score':item[4]+item[5]})

def write_file(tem):
    with open('result.txt', 'a', encoding = 'utf-8') as f:#设置编码为utf-8，以保存中文
        f.write(json.dumps(tem, ensure_ascii = False) + '\n')
        #json.dumps用于将python类型转换成json字符串类型，以便存入文件
        # encoding_ascii = False保障输出结果是中文而不是unicode编码

def main():
    url = "http://maoyan.com/board/4"

    html = get_one_page(url)
    parse_one_page(html)
    for i in parse_one_page(html):
        print(i)
        write_file(i)

if __name__ == '__main__':
    main()
