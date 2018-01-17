#!usr/bin/python/
#-*-conding:utf-8-*-
import  pickle
import selenium
import selenium.webdriver

driver=selenium.webdriver.Firefox()
driver.get("http://www.baidu.com") #添加cookie,访问网页之后

cookies=[]
cookies=pickle.load(open("cookie.txt","rb"))
print(type(cookies))
print(cookies)
for cookie  in cookies:
    print(cookie)
    driver.add_cookie(cookie)



driver.close()