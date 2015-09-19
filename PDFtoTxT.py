'''
Created on Jan 27, 2014

@author: connieschibber

Program to turn a number of PDFs into txt files
'''
import urllib2
import os
import csv
import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFSyntaxError
#from pdfminer.converter import TextConverter
import nltk
import codecs


def link_to_pdf(url):
    try:
        page = urllib2.urlopen(url)
        page_object = StringIO.StringIO(page.read())
        page.close()        
        return page_object
    except urllib2.URLError, e: 
        print row[1]
        print e.args
        pass
    except urllib2.HTTPError, e: 
        print e.code
        print row[1]
        pass

def pdf_to_text(page_object):
    parser = PDFParser(page_object)
    # Create a PDF document object that stores the document structure
    doc = PDFDocument(parser)
    # Connect the parser and document objects.
    parser.set_document(doc)
    doc.initialize('')
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF page aggregator object
    device = PDFPageAggregator(rsrcmgr, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    text_content = []
    # i = page number #without this it doesn't work
    # page are items in page
    for i, page in enumerate(PDFPage.create_pages(doc)):
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        for object in layout:
            if isinstance(object, LTTextBox) or isinstance(object, LTTextLine):
                trial = []
                trial.append(object.get_text())
                for word in trial:
                    text_content.append(word)                    
    return text_content

def write_file (folder, filename, filedata, flags='w'):
    """Write the file data to the folder and filename combination
    (flags: 'w' for write text, 'wb' for write binary, use 'a' instead of 'w' for append)"""
    result = False
    if os.path.isdir(folder):
        try:
            file_obj = codecs.open(os.path.join(folder, filename), encoding='utf-16', mode='w', errors='ignore')
            for item in filedata:
                file_obj.write("%s\n" % item)
            file_obj.close()
            result = True
        except IOError:
            print "ERROR WRITE FILE"
            pass
    return result

path = #Here fill in the path to the folder where you saved PDFs
path_save = #Here fill in the path to the folder where the txt files will be saved

for file in os.listdir(path):
    if file.endswith(".csv"): 
        with open(os.path.join(path, file), 'rb') as f:  
            reader = csv.reader(f)
            next(reader) #1st row is header
            for row in reader:
                bill = row[1]
                bill = bill.split("/")
                filename = bill[1] + '-' + bill[0] + '.txt'
                print filename
                try: 
                    page = link_to_pdf(row[3])
                    page_pdf = pdf_to_text(page)
                    write_file(folder=path_save, filename=filename, filedata=page_pdf)
                    print "ready"
                    print '------'
                except PDFSyntaxError:
                    print "Error - NOT A PDF" 
                    print row[1]     
                    print "------"
                    pass           
                

print '----- The End -----'
