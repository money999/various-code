# coding: utf-8
'''
从网站上爬下福利彩票双色球所有开奖结果
'''
from urllib import request
import re, collections

# 获取html页面
# 目前就只有110页的结果
def get_html():
    page_num=range(1,111)
    res = ''
    for page in page_num:
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html' % page
        response = request.urlopen(url)
        html = response.read()
        res += html.decode('utf-8')
    return res

# 解析页面获取每期开奖结果
def get_ballnum():
    html = get_html()
    reg = re.compile(r'<tr>[^<]*'
                     r'<td align="center">(.*?)</td>[^<]*'
                     r'<td align="center">(.*?)</td>[^<]*'
                     r'<td align="center" style="padding-left:10px;">[^<]*'
                     r'<em class="rr">(.*?)</em>[^<]*'
                     r'<em class="rr">(.*?)</em>[^<]*'
                     r'<em class="rr">(.*?)</em>[^<]*'
                     r'<em class="rr">(.*?)</em>[^<]*'
                     r'<em class="rr">(.*?)</em>[^<]*'
                     r'<em class="rr">(.*?)</em>[^<]*'
                     r'<em>(.*?)</em></td>', re.S)
    res = re.findall(reg, html)
    return res

# 返回中奖等级
# 开奖红球，开奖蓝球，预判红球，预判蓝球
def get_prize(pubball,pubspe, preball, prespe):
    ballnum = 6
    iz = len(collections.Counter(pubball + preball)) - ballnum
    if iz == 0 and pubspe == prespe:
        return 1
    elif iz == 0:
        return 2
    elif iz == 1 and pubspe == prespe:
        return 3
    elif iz == 1 or (iz==2 and pubspe ==prespe):
        return 4
    elif iz == 2 or (iz==3 and pubspe==prespe):
        return 5
    elif pubspe == prespe:
        return 6
    else:
        return 0

if __name__ == '__main__':

# 打算守的十组号
    preball = ([1,5,15,22,25,32,14],
               [6,8,16,21,30,32,4],
               [13,14,23,25,27,32,12],
               [18,22,25,26,30,31,4],
               [5,8,10,21,25,27,7],
               [13,16,17,27,28,32,7],
               [5,9,10,14,18,33,1],
               [5,7,11,12,24,33,10],
               [7,9,16,24,29,30,2],
               [4,11,13,25,29,33,9])
    index = 0
    ballres = get_ballnum()
    liss = [] #十组号每期中奖的结果
    allball = [] #所有开奖红球号码
    sprball = [] #所有开奖蓝球号码
    for issue in ballres:
        for index in range(10):
            res = get_prize(list(map(int, issue[2:8])), int(issue[8]), preball[index][:6], preball[index][6])
            allball.extend(list(map(int, issue[2:8])))
            sprball.append(int(issue[8]))
            if res > 0:
                print(issue, res)
                liss.append(res)

    print(collections.Counter(liss)) #中奖次数
    print(collections.Counter(allball)) #每个红球号码出现次数
    print(collections.Counter(sprball)) #每个蓝球号码出现次数
