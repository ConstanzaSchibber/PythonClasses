'''
Created on Nov 9, 2014

@author: connieschibber

HTML Encoding Problems 
'''

import nltk
import HTMLParser
import mechanize
import os
import codecs

def create_soup(url):
    br = mechanize.Browser()
    br.set_handle_robots(False) # ignore robots.txt
    br.addheaders = [('User-agent', 'Mozilla/5.0')] 
    page = br.open(url) #open browser
    html = page.read() #read page
    html_parser = HTMLParser.HTMLParser()  #MAGIC line for CHARACTERS
    unescaped = html_parser.unescape(html) #MAGIC line for CHARACTERS
    raw_text = nltk.clean_html(unescaped)
    return raw_text
    br.close()    #close browser
 
 
path_save = "/Users/connieschibber/"    
filename = '0004-PE-2005' + '.txt'
link = 'http://www3.hcdn.gov.ar/folio-cgi-bin/om_isapi.dll?advquery=0029-PE-05&infobase=tp.nfo&record=%7BA4F7%7D&recordswithhits=on&softpage=proyecto'
 
raw_text = create_soup(link)
print raw_text

# How to save this as a file -- need uft-16

file_obj = codecs.open(os.path.join(path_save, filename), 'w', 'utf-16')
file_obj.write(raw_text)
    
