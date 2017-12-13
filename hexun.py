# -*- coding:utf-8 -*-
import requests
import time
page_count = 20
page_index = 1
hy = 'RB1805'#3:RB ZN PB 2:AG AU 合约代码
tm = '20171208093000'#时间
n ='1'#'记录条数'
ts = str(round(time.time()*1000)) #'1412652968269' 时间戳？
url_template = 'http://webftcn.hermes.hexun.com/shf/minute?code=SHFE3'+hy+'&start='+tm+'&number='+n+'&t='+ts#'http://webftcn.hermes.hexun.com/shf/historyminute?code=SHFE3ZN1805&date=20171206'
                #http://webftcn.hermes.hexun.com/shf/minute?code=SHFE2AG1806&start=20171207212200&number=570&t=1512652968279


def get_json_from_url(url):
    r = requests.get(url)
    t = str(r.content,'utf-8')
    print(t)


def init_url_by_parms(page_count=40, page_index=1):
    if not page_count or not page_index:
        return ''
    return url_template.replace('{page_index}', str((page_index - 1) * page_count)).replace('{page_count}',
                                                                                            str(page_count))


if __name__ == '__main__':
    #url = init_url_by_parms(page_count=page_count, page_index=page_index)
    url = url_template
    print (url)
    print (int(round(time.time()*1000)))
    objs = get_json_from_url(url)
    #print (objs)
    '''
    if objs:
        for obj in objs:
            print ('####################################')
            for k, v in obj.items():
                print (k, ':', v)
    '''
