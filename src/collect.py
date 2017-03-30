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

patent_url = 'http://www.soopat.com/Home/Result?SearchWord='+str(name)+'&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(patent_url,headers = headers)#urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

'''
collect  paper_information
'''







'''
build  csv file
'''