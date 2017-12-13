from bs4 import BeautifulSoup
import urllib.request
import xlrd
import time
import requests
import json

#import easyExcel       
def parser(cont,key):
    soup = BeautifulSoup(cont,'html.parser',from_encoding='utf-8')
    print(soup.title.string.strip())
    print(soup.find(text=key).string)
    print(soup.find(text=key).parent.next_sibling.next_sibling.next_sibling.next_sibling.string)
    print(soup.find(text=key).parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.string)
    #print (time.strftime("%m月%d日"))
    if time.strftime("%m月%d日") == soup.find(text=key).parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.string:
        #Out_excel("D:\zn.xls",1,time.strftime("%m月%d日"))
        if key =='SMM 0#锌锭':
            Out_excel("D:\zn.xls",7,soup.find(text=key).parent.next_sibling.next_sibling.next_sibling.next_sibling.string.strip())
        if key =='SMM 1#铅锭':
            Out_excel("D:\zn.xls",16,soup.find(text=key).parent.next_sibling.next_sibling.next_sibling.next_sibling.string.strip())
        
def parser_hn(cont,key1,key2):
    soup = BeautifulSoup(cont,'html.parser',from_encoding='utf-8')
    print(soup.title.string.strip())
    hn = soup.find('div',class_="dis",id="sub1").tbody.tbody#.tr.td
    #print(hn.string)
    for td in hn.findAll('td'):
        if td.string.strip() == key1 and td.next_sibling.next_sibling.string.strip()== key2:
            print(td.string.strip())
            print(td.next_sibling.next_sibling.string.strip())
            print(td.next_sibling.next_sibling.next_sibling.next_sibling.string.strip().split('-')[1])
            print(td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string.strip())
            if time.strftime("%m-%d") == td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string.strip():
                Out_excel("D:\zn.xls",8,td.next_sibling.next_sibling.next_sibling.next_sibling.string.strip().split('-')[1])
            
            
def parser_ht(cont,key):
    soup = BeautifulSoup(cont,'html.parser',from_encoding='utf-8')
    print(soup.title.string.strip())
    print(soup.find(text=key).string)
    print(soup.find(text=key).parent.next_sibling.next_sibling.string)            
    print(soup.find(text=key).parent.parent.next_sibling.next_sibling.td.string)
    print(soup.find(text=key).parent.parent.next_sibling.next_sibling.td.next_sibling.next_sibling.string)

def parser_ht2(cont,key):
    soup = BeautifulSoup(cont,'html.parser',from_encoding='utf-8')
    print(soup.title.string.strip())
    print(key)
    print(soup.find(text=key).parent.parent.parent.parent.next_sibling.next_sibling.td.string)
    print(soup.find(text=key).parent.parent.parent.parent.next_sibling.next_sibling.td.next_sibling.next_sibling.string)
    print(soup.find(text=key).parent.parent.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.td.string)
    print(soup.find(text=key).parent.parent.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.td.next_sibling.next_sibling.string)

def parser_hx(code,Symbol,t):
    ts = str(round(time.time()*1000))#时间戳
    start = time.strftime("%Y%m%d")+str(t)
    #print(start)
    #code = 3
    print('')
    url='http://webftcn.hermes.hexun.com/shf/minute?code=SHFE'+code+Symbol+'&start='+start+'&number=1&t='+ts
    r = requests.get(url)
    d = str(r.content,'utf-8')
    dj = d[1:-2]
    jj = json.loads(dj)
    print(Symbol)
    print('时间:%s'%jj['Data'][0][0][0])
    print('价格:%s'%jj['Data'][0][0][1])
    print('成交额:%s'%jj['Data'][0][0][2])
    print('成交量:%s'%jj['Data'][0][0][3])
    print('持仓量:%s'%jj['Data'][0][0][5])
    
def download(url):
    if url is None:
        return None
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    #User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53
    rep = urllib.request.Request(url=url, headers=headers)  
    respons = urllib.request.urlopen(rep)#.read()  
    #respons = urllib.request.urlopen(url)
    if respons.getcode()!=200:
        print (respons.getcode())
        return None
    print(respons.getcode())
    print('页面访问成功')
    print("")
    return respons.read()

from xlrd import open_workbook
from xlutils.copy import copy
def Out_excel(fn,l,s):
    data = xlrd.open_workbook(fn)
    table = data.sheet_by_name(u'Sheet1')
    row = table.nrows-1
    print('第%r行'%row)
    #print(table.cell(row,0).value) #单元格的值'
    if table.cell(row,0).value == time.strftime("%m月%d日"):
        # 打开文件
        rb = open_workbook(fn)
        # 复制
        wb = copy(rb)
        # 选取表单
        sheet = wb.get_sheet('Sheet1')
        # 写入数据
        sheet.write(row,l-1,s)
        # 保存
        wb.save(fn)
    else:
        # 打开文件
        rb = open_workbook(fn)
        # 复制
        wb = copy(rb)
        # 选取表单
        sheet = wb.get_sheet('Sheet1')
        # 写入数据
        sheet.write(row+1,0,time.strftime("%m月%d日"))
        # 保存
        wb.save(fn)

if __name__=='__main__':
    
    url1 = "https://hq.smm.cn/qian"
    p1 = download(url1)
    parser(p1,'SMM 1#铅锭')
    
    url2 = "https://hq.smm.cn/xin"
    p2 = download(url2)
    parser(p2,'SMM 0#锌锭')
    
    url = 'http://www.enanchu.com/'
    p = download(url)
    parser_hn(p,'锌锭','Zn99.995')
    '''
    url3 = 'http://www.ex-silver.com/'
    p3 = download(url3)
    parser_ht(p3,'定盘价')
    '''
    url3 = 'http://www.ex-silver.com/'
    p3 = download(url3)
    parser_ht2(p3,'上海华通现货白银报价')

    parser_hx('3','ZN1801','103000')
    parser_hx('3','ZN1802','103000')
    parser_hx('3','ZN1803','103000')
    parser_hx('3','Pb1802','103000')
    parser_hx('3','Pb1803','103000')
    parser_hx('2','AG1801','103000')
    parser_hx('2','AU1801','103000')
    
