import random
from selenium import webdriver
import time
import os
driver = webdriver.Chrome('chromedriver')

time.sleep(0.5)
f = open("username.txt", "r")
a=f.read()
f = open("password.txt", "r")
b=f.read()
f.close()
def updatefile(followers):
    f=open('followedtoday.txt','w')
    for i in followers:
        f.write(i)
        f.write('\n')
    f.close()
while True:
    try:
        driver.get('https://www.instagram.com/')
        time.sleep(random.randint(5,9))
        print('trying to login')
        username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        username.send_keys(a)
        password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password.send_keys(b)
        sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        sign_in_button.click()
        time.sleep(random.randint(5,9))
        break
    except:
        print('some error occured tring again')
    finally:
        print('logged in sucessfully')
while True:
    try:
        print('reading')
        f= open("message.txt", "r")
        message=f.read()
        f = open("followedtoday.txt", "r")
        followers=f.readlines()
        f.close()
        break
    except:
        print('nothing to do status code 0')
        exit()
copiedarray=followers
print(copiedarray)
while True:
        driver.get('https://www.instagram.com/direct/new/')
        time.sleep(random.randint(5,9))
        try:
            notnowbutton = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            notnowbutton.click()
            break
        except:
            print('trying again not now is disturbing')
        time.sleep(3)
followers=copiedarray
for i in followers:
    try:

        driver.get('https://www.instagram.com/direct/new/')
        time.sleep(random.randint(5,9))
        newmessage = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
        time.sleep(1)
        newmessage = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input')               
        newmessage.send_keys(i)
        time.sleep(random.randint(5,9))
        newmessage = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/button')                                        
        newmessage.click()
        nextbutton = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/button')                                        
        nextbutton.click()
        time.sleep(random.randint(5,9))
        newmessage = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')                                        
        newmessage.send_keys(message)
        newmessage.send_keys('\n')
        print('sent message to ',i)
        copiedarray.pop(0)
        print(copiedarray)
        updatefile(copiedarray)
    except:
        print('couldnt send message to ',i)
        continue
os.remove('followedtoday.txt')
driver.quit()
