## -*- coding: utf-8 -*- 

'''
Created on Nov 9, 2014

@author: connieschibber

Saving text in multiple languages. Example with Wikipedia's Political Science page
'''

import urllib2
from BeautifulSoup import BeautifulSoup
import codecs
import os 

main_wiki = 'http://en.wikipedia.org/wiki/Political_science'

def create_soup(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=hdr)
    page = urllib2.urlopen(req)
    html = page.read()
    page.close()
    return  BeautifulSoup(html) 

soup = create_soup(main_wiki)

links = soup.findAll('a', lang=True)
#print links

for link in links:
    print link['lang'] + link['title']   
 
 
## Correct way of saving file
path_save = "/Users/connieschibber/"    
filename = 'wikipedia_languagues.txt'
    
the_file = codecs.open(os.path.join(path_save, filename), 'w', encoding='utf-8')
for item in links:
#    print link
    the_file.write("%s\n" % item)
the_file.close()

### Correct way of reading file
lines = codecs.open('/Users/connieschibber/wikipedia_languagues.txt', 'r', 'utf-8')
#for line in lines:
#    print line
    
# Incorrect way of saving # Not specifying encoding

#path_save = "/Users/connieschibber/"    
#filename = 'wikipedia_languagues.txt' 

#file_obj = open(os.path.join(path_save, filename), 'w')
#for link in links:
#    obj = link['lang'] + link['title']
#    file_obj.write(obj.encode('unicode_escape'))
#file_obj.close()
    
