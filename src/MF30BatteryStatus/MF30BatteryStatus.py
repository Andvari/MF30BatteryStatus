'''
Created on 11.01.2012

@author: Nemo
'''

import urllib, urllib2, re, time


params = urllib.urlencode({'systemDate' : 0113131112, 'user' : 'admin', 'psw' : 'admin', 'languageSelect' : 'ru', 'save_login' : 1, 'save_login_enablebox' : 1})

response = urllib.urlopen('http://192.168.0.1/goform/login', params) 
page = response.read()
"""
response = urllib.urlopen('http://192.168.0.1/index.asp', params) 
page = response.read()

response = urllib.urlopen('http://192.168.0.1/statistic.asp', params)
page = response.read()

print page

"""
response = urllib.urlopen('http://192.168.0.1/index.asp', params) 
page = response.read()
response = urllib.urlopen('http://192.168.0.1/logo.asp', params) 
page = response.read()

battery = page[page.find('battery_status') + 18 : ]
battery = battery[: battery.find("'")]
print 'Battery status: ' + battery + '%'

time.sleep(1)
