#_*_coding:utf-8_*_
# 引入模块
import requests
from lxml import etree
import re
import time
import datetime

res=requests.get('http://www.zhaojianzhu.com/toutiao')
html=res.text
sel=etree.HTML(html)
page_last=sel.xpath('//div[@class="pgnew"]/a[@class="last"]/text()')
re_com=re.compile('...(\d+)')
page_all=re_com.findall(page_last[0])
page_max=int(page_all[0])
i=0
begin = datetime.datetime.now()
with open("zhaojianzhu.txt","a+",encoding="utf-8") as f:
    for n in range(1,page_max+1):
        print("开始获取第%s页信息" % n)
        start_url="http://www.zhaojianzhu.com/toutiao/s4&sortid=4&filter=sortid&sortid=4&searchsort=1?page={}".format(n)
        res2=requests.get(start_url)
        html2=res2.text
        sel2=etree.HTML(html2)
        href_list=sel2.xpath('//a[@class="list_title"]/@href')
        for href in href_list:
            url="http://www.zhaojianzhu.com/"+href
            # print(url)
            res3 = requests.get(url)
            html3 = res3.text
            sel3 = etree.HTML(html3)
            text=sel3.xpath('//div[@id="img-content"]/h2[@id="activity-name"]/text()')
            if text:
               text=text[0].strip()
               f.write(text)
               f.write("\n")
            # print(text)
            text2 = sel3.xpath('//div[@id="js_content"]/p/text()')
            text4="".join(text2)
            f.write(text4)
            f.write("\n")
            text3 = sel3.xpath('//div[@id="js_content"]/p/span/text()')
            for text5 in text3:
                f.write(text5)
                f.write("\n")
            i = i + 1
            if i % 10 == 0:
                print('已获取%s篇文章' % i)
        end = datetime.datetime.now()
        usetime=end-begin
        print("获取%s页信息，共用时：" % n)
        print(usetime)
        time.sleep(2)





