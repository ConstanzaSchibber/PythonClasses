## -*- coding: utf-8 -*- 

# For non ASCII characters
'''
Created on Nov 8, 2014

@author: connieschibber

Testing how strings work
'''

# Bytes


# Bytes 

a = "αά".encode('utf-8') # bytes
print 'This is a'
print a
print len(a)

b = 'αά' #bytes
print 'This is b'
print b
print len(b)

c = '\xce\xb1\xce\xac'
print 'This is c'
print c
print len(c)

#Unicode

d = a.decode('utf-8') # unicode
print 'This is e'
print d
print len(d)

e = u'αά' #unicode
print 'This is c'
print e

print a[1] == e[1]
print a[1]
print c[1]
print e[1]
