# fileparse.py
#
# Exercise 3.3
import urllib.request
u = urllib.request.urlopen('https://flexiple.com/python/print-object-attributes-python')
data = u.read()
print(data)