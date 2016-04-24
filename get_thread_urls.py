# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:46:35 2016

@author: nicenick
"""
from bs4 import BeautifulSoup
import re
# import urllib2

if __name__ == "__main__":
  count = 0
  file = 'D:\GitProject\web_crawler\sample_thlist.html'
  f = open(file,'r')
  # below is an alternative
  # with open(file,'r') as f:
    # thread_list = BeautifulSoup(unicode(f.read(),"utf-8"))
  # somehow if open url of this hipda page and create a bs4 object
  # everything will be read to the obj, but if copy paste to sublime and save it
  # then glitches due to inconsisitency between unicode and utf-8 will show up
  # if write back the transfered data(unicode()) to the file, ascii encoder will 
  # report failure on ecoding such data, so the only dirty choice here is unicode()
  # each time read from a file like this
  content = unicode(f.read(),"utf-8")
  thread_list = BeautifulSoup(content)
  pattern = r'viewthread\.php\?tid=[0-9]*&extra=page%3D[0-9]'
  string = 'viewthread.php?tid=1851214&extra=page%3D2'
  target_len = len(string)
  all_urls = thread_list.find_all('a', href=True)
  thread_urls_str = []
  for url in all_urls:
    url_str = url['href']
    if re.search(pattern, url_str) != None:
      if len(url_str) == target_len:
        if count % 2 == 0:
          thread_urls_str.append(url_str)
        count += 1


  print len(thread_urls_str)