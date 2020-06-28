import random
import time
import os
followedtoday='#follow#followback#likes#f#followme#followforfollow#followbackteam#followforfollowback#followmeplease#followers'
followedtoday=followedtoday.split('#')[1:]
print(followedtoday)
try:
    f=open('followedtoday.txt')
    length=f.readlines()
    dailylimit=10-len(length)
except:
    dailylimit=10
print(dailylimit)
def writeinfollower(username):
    f = open("followedtoday.txt", "a")
    f.write(username)
    f.write('\n')
    f.close()
def follow(dailylimit):
    try:
        followlink=random.choice(followedtoday)
        followedtoday.remove(followlink)
        followlink='https://www.instagram.com/explore/tags/'+followlink+'/'
        print(followlink)
        driver.get(followlink)
        time.sleep(random.randint(5,9))
        post = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a').get_attribute('href')
        driver.get(post)
        followbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button')
        followbutton.click()
        username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/a').get_attribute('href')
        time.sleep(random.randint(5,9))
        print(username[26:-1])
        writeinfollower(username[26:-1])
        print('followed',10-dailylimit)
    except:
        print('some error occured while trying to follow')
        pass
        
    if dailylimit>0:
        dailylimit-=1
        follow(dailylimit)
    else:
        print('hourly limit reached')
        return
from selenium import webdriver
#we store this driver in the variable called driver
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.instagram.com/')
time.sleep(0.5)
f = open("username.txt", "r")
a=f.read()
f = open("password.txt", "r")
b=f.read()
f.close()

while True:
    try:
        username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        username.send_keys(a)
        password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password.send_keys(b)
        sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        sign_in_button.click()
        time.sleep(random.randint(5,9))
        break
    except:
        print('some error occurred try again')
        continue
    finally:
        print('logged in sucessfully')
follow(dailylimit)
driver.quit()
