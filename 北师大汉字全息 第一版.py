# coding=utf-8
import os
import random
import re
import requests
from lxml import etree
import openpyxl
from bs4 import BeautifulSoup
import time
from DrissionPage import ChromiumPage, web_page, ChromiumOptions
import pandas as pd


import execjs
import json
from urllib.request import urlretrieve
from DownloadKit import DownloadKit

d = DownloadKit()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://qxk.bnu.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://qxk.bnu.edu.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
data_1 = {
  'ziFuJiId': 'lwYREKSkK1DgPWHo60hoBuKiDg+lZgYevvCqudnwaX2RuoomI/yRRbz5f4bI4iqG',
  'jstjId': 'WagkdUR2Niv2c+IxZAl5V2sIf1yADd9a+TvoJFx0sd1dWfwAszERW4dywPjrLMOF',
  'content': ''
}

keyword='龙'
try:
    os.mkdir(keyword)
except FileExistsError :
    pass
path=f'{keyword}/{keyword}.txt'
d.goal_path = f'{keyword}'
# d.retry=10
d.file_exists='overwrite'

# jiami_keyword=execjs.compile(open('d1.js','r',encoding='utf-8').read()).call('jbbbbbb',keyword)
data_1['content']=keyword
response = requests.post('https://qxk.bnu.edu.cn/qxkapi/gjqxk/hanzi/search', headers=headers, data=data_1)
res1=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jiemi',response.text)
json_data1=json.loads(res1)['data']

fantizi=json_data1['fantizi'][0]
fantizi=fantizi['hanzi']+'-'+fantizi['jhfs']

print(fantizi)
buShou=json_data1['hanzi']['buShou']
print(buShou)
zBiHua=json_data1['hanzi']['zBiHua']
print(zBiHua)
biShun=json_data1['hanzi']['biShun']
print(biShun)
jieGouLeiXing=json_data1['hanzi']['jieGouLeiXing']
print(jieGouLeiXing)
jieGouTuShi=json_data1['hanzi']['jieGouTuShi']
print(jieGouTuShi)
ziJi=json_data1['hanzi']['ziJi']
print(ziJi)
pinyin=json_data1['hanzi']['pinyin']
zhuYinZiMu=json_data1['hanzi']['zhuYinZiMu']
xiandai=f'拼音：{pinyin} 注音：{zhuYinZiMu}'
print(xiandai)
jiami_keyword=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jbbbbbb',keyword)

jiami_keyword2=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jbbbbbb',fantizi.split('-')[0])

data2 = {
  'hanzi': jiami_keyword,
  'listhanzi': jiami_keyword2,
  'ziFuJiId': 'lwYREKSkK1DgPWHo60hoBuKiDg+lZgYevvCqudnwaX2RuoomI/yRRbz5f4bI4iqG'
}

response = requests.post('https://qxk.bnu.edu.cn/qxkapi/gjqxk/result/yin', headers=headers, data=data2)

res2=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jiemi',response.text)
time.sleep(0.4)
json_data2=json.loads(res2)['data'][0]
yin=json_data2['yin']

xitongname1=yin['shang'][0]['xitongname']
xitongname2=yin['shang'][1]['xitongname']
value_xitongname1=yin['shang'][0]['list']
value_xitongname1=''.join(value_xitongname1)
value_xitongname2=yin['shang'][1]['list']
value_xitongname2=''.join(value_xitongname2)
yin_shang=f'{xitongname1}:{value_xitongname1} | {xitongname2}:{value_xitongname2}'
print(yin_shang)
yin_zhong=''.join(yin['zhong'])
print(yin_zhong)
yin_jin=''.join(yin['jin'])
print(yin_jin)

data3 = {
  'hanzi': jiami_keyword,
  'listhanzi': jiami_keyword2,
  'ziFuJiId': 'lwYREKSkK1DgPWHo60hoBuKiDg+lZgYevvCqudnwaX2RuoomI/yRRbz5f4bI4iqG'
}

response = requests.post('https://qxk.bnu.edu.cn/qxkapi/gjqxk/result/yi2', headers=headers, data=data3)


res3=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jiemi',response.text)
time.sleep(0.4)
json_data3=json.loads(res3)['data']['cishushiyimulu']
dict_in={}
for i in json_data3:
    dict_in[i['id']]=i['header']

data4 = {
  'hanzi': jiami_keyword,
  'listhanzi': jiami_keyword2,
  'id': ''
}
dict_out={}
dict_out_img={}
for i in dict_in:
    data4['id']=i
    response = requests.post('https://qxk.bnu.edu.cn/qxkapi/gjqxk/result/cishushiyi', headers=headers, data=data4)
    res4=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jiemi',response.text)
    json_data4 = json.loads(res4)['data']
    for j in json_data4:

        if j['shiyi']!=[]:
            img='https://qxk.bnu.edu.cn/pic_server/'+j['pics'][0]
            txt=j['shiyi'][0]
            pattern = re.compile(r'<[^>]+>', re.S)
            result = pattern.sub('', txt)
            dict_out[dict_in[i]]=result
            dict_out_img[dict_in[i]]=img
    time.sleep(0.55)
print(dict_out)
print(dict_out_img)
data5 = {
  'hanzi': jiami_keyword,
  'listhanzi': jiami_keyword2,
  'ziFuJiId': 'lwYREKSkK1DgPWHo60hoBuKiDg+lZgYevvCqudnwaX2RuoomI/yRRbz5f4bI4iqG'
}

response = requests.post('https://qxk.bnu.edu.cn/qxkapi/gjqxk/result/yi2', headers=headers, data=data5)
res4=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jiemi',response.text)

time.sleep(0.4)
json_data4=json.loads(res4)['data']
changyongyixiang=''.join(json_data4['changyongyixiang'])
print(changyongyixiang)

data6 = {
  'hanzi': jiami_keyword,
  'listhanzi': jiami_keyword2,
  'dynasty': 'KsMU7pWW+HG/QhAEABLXyPRHtT6Fk7VA4Gf8+QGgF+2ZXJboZfrJXt51OmMGvFNQ',
  'pageSize': '8gx63SOoZWoVlySCj8O1Rw==',
  'index': '8gx63SOoZWoVlySCj8O1Rw=='
}
dict_dy={
'jgw':'甲骨文',
'jw':'金文',
    'qjd':'秦简牍',
'cwz':'楚文字',
    'qlwz':'齐鲁文字',
'kaishu':'楷书',
    'ls':'隶书',
'qxz':'秦小篆',
    'xingshu':'行书',
    'caoshu':'草书'
}
'http://qxk.bnu.edu.cn/pic_server//images/chinesedatabase/bookCrop/402881945f4ce10f015f4d27b5a30056/6ad767385862476e8f6bf9e0baba4194.jpg!70!10000000'
response = requests.post('https://qxk.bnu.edu.cn/qxkapi/gjqxk/result/pic_page', headers=headers, data=data6)
res6=execjs.compile(open('decode1.js','r',encoding='utf-8').read()).call('jiemi',response.text)
json_data6=json.loads(res6)['data'][0]
dict_out_img2={}
lst_6=json_data6['pic_page']
for i in lst_6:
    img='http://qxk.bnu.edu.cn/pic_server/'+i['records'][0]['simplePhoto']
    if i['dynasty'] in dict_dy:
        dict_out_img2[dict_dy[i['dynasty']]]=img
print(dict_out_img2)
write_lst=['繁体字\n',fantizi+'\n','部首\n',buShou+'\n','笔画数\n',zBiHua+'\n','笔顺\n',biShun,'造字方法\n',jieGouLeiXing+'\n','结构类型\n',jieGouTuShi+'\n','规范字级\n',jieGouTuShi+'\n',
           '现代音\n',xiandai+'\n','近代音\n',yin_jin+'\n','中古音\n',yin_zhong+'\n','上古音\n',yin_shang+'\n','现代义项\n',changyongyixiang+'\n']
for i,j in dict_out.items():
    write_lst.append(i+'\n')
    write_lst.append(j+'\n')
print(write_lst)
with open(path,'w',encoding='utf-8') as f:


    f.writelines(write_lst)
for i,j in dict_out_img.items():
    print(j)
    d.add(j,rename=f'{keyword}-{i}.jpg')
    # urlretrieve(j,f'{keyword}/{keyword}-{i}.jpg')

for i,j in dict_out_img2.items():
    print(j)
    d.add(j,rename=f'{keyword}-{i}.jpg')
    # urlretrieve(j,f'{keyword}/{keyword}-{i}.jpg')
d.wait()