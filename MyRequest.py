import requests
import time
import re
import json
name = '爱学派FF'
pwd = '1111'
localtime = time.time().as_integer_ratio()
print(localtime)
dataload =(('name', name),('pwd',pwd),('time', localtime),('method','login.do'))
r = requests.post('http://school.etiantian.com/aixuepadtios/test/_manager/GenderCourseRecordSign.jsp', data=dataload)
s = r.status_code
print(s)
t = r.text
print(t.rstrip())
print("------------------------------")
dataloadlogin =(('name', name),('pwd',pwd),('time', localtime),('sign',t.rstrip()))
loginRequest = requests.post('http://school.etiantian.com/aixuepadtios/login.do', data=dataloadlogin)
print(loginRequest.json())
data1 = loginRequest.json()
str =loginRequest.text
#re.search(pattern, string, flags=0)
str1 =re.search("schoolId\":(.*),\"jid", str, flags=0)
print("--------")
print(str1)
