# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import csv
'''
collect  patent_information
FMZL: Invention patent
SYXX: utility model
WGZL: Exterior design
FMSQ: Invention authorization
'''

name = '尹宏鹏'
FMZL = 'Y'
SYXX = 'Y'
WGZL = 'Y'
FMSQ = 'Y'
PatentIndex = ''

patent_url = 'http://www.soopat.com/Home/Result?SearchWord='+str(name)+'&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
Referer = 'http://www.zhihu.com/articles' 
headers = { 'User-Agent' : user_agent, 'Referer' :Referer}

try:
    patent_request = urllib2.Request(patent_url,headers = headers)
    patent_response = urllib2.urlopen(patent_request)
    print patent_response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

patent_content = patent_response.read().decode('utf-8')

# varify_code = '验证码'
# varify_code = varify_code.decode('utf-8')
# chinese_pattern = re.compile(varify_code)
# varify = chinese_pattern.findall(patent_content)
# print repr(patent_content)
# print patent_content
# print repr(varify_code)

patent_patern = re.compile("MC.*?='(.*?)'", re.S)
patent_items = re.findall(patent_patern, patent_content)
print patent_items
'''
collect  paper_information
'''







'''
build  csv file
'''