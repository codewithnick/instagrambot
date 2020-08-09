#imports and variables
import time
import traceback
import random


followlimit=10
commentlimit=10
dmlimit=3
#connectiong to mongo client
import pymongo
from pymongo import MongoClient
client = MongoClient("")
db = client["bot"]
collection=db["user"]
hashtag=db["hashtag"]
hashtag=hashtag.find({"_id":0})
commentarray=hashtag[0]["comments"]
followedarray=hashtag[0]["follows"]
users=collection.find({})
#####################################################################################################################################
#####################################################################################################################################
####################################################################################################################################


# connecting selenium window 
from selenium import webdriver





#####################################################  loop for all users ####################################################
for user in users:
    #reset vars
    followlimit=10
    commentlimit=10
    dmlimit=3
    links=[]
    user_name_array=[]
    a=user["username"]
    b=user["password"]
    #create driver
    driver =webdriver.Chrome('chromedriver')
    driver.get('https://www.instagram.com/')
    #login now
    while True:
        try:
            #9 seconds to load page
            time.sleep(random.randint(5,9))
            username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
            username.send_keys(a)
            password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
            password.send_keys(b)
            sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
            sign_in_button.click()            
        except:
            traceback.print_exc()
            print('some error occurred trying again')
            continue
        else:
            print('logged in sucessfully')
            #wait for page load
            time.sleep(random.randint(5,9))
            break
        finally:
            time.sleep(1)
            
    #comment 10 posts
    while commentlimit>0:
        try:
            linkvar=random.choice(commentarray)
            print(linkvar)
            #get the hastag search
            driver.get(linkvar)
            #wait for page 9 seconds
            time.sleep(random.randint(5,9))
            #get the link for the post
            postlink = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a').get_attribute('href')
            #if already commented
            if postlink in links:
                continue
            commentarray.remove(linkvar)
            links.append(linkvar)        
            driver.get(postlink)
            time.sleep(random.randint(5,9))
            #now comment
            postbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button')
                                                      #/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[2]/button
            postbutton.click()
            #writing comment wait for 9 seconds
            time.sleep(random.randint(5,9))
            commentbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
                                                         #/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea
            commenttext=user["comments"]
            commentbutton.send_keys(random.choice(commenttext))
            postbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/button[2]')
                                                      #/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div[1]/form/button
            postbutton.click()
            #comment posted
            commentlimit-=1
            time.sleep(random.randint(5,9))
            print('commented on '+postlink)
            print(commentlimit+'left to be commented')
        except:
            traceback.print_exc()
            print('could not comment trying next post')
    print('daily commenting limit reached')
    #follow 10 people
    while followlimit>0:
        try:
            #choose hashtag
            followlink=random.choice(followedarray)
            followedarray.remove(followlink)
            driver.get(followlink)
            time.sleep(random.randint(5,9))
            #getpost
            post = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a').get_attribute('href')        
            driver.get(post)
            #followbutton
            followbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button')                                
            followbutton.click()                                        
            time.sleep(1)
        except:
            traceback.print_exc()
            print('could not follow trying next')
            pass
        followlimit-=1
    #find 3 people
    while dmlimit>0:
        try:
            followlink=random.choice(followedarray)
            followedarray.remove(followlink)
            driver.get(followlink)
            time.sleep(random.randint(5,9))
            #getpost
            post = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a').get_attribute('href')        
            driver.get(post)
            #getusername
            user_name = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a').get_attribute('href')
            user_name=user_name[26:-1]
            user_name_array.append(user_name)
            pass
        except:
            traceback.print_exc()
            print('could not message trying next')
            pass
        dmlimit-=1
    
    #now dm them
    while True:
        driver.get('https://www.instagram.com/direct/new/')
        time.sleep(random.randint(5,9))
        try:
            notnowbutton = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            notnowbutton.click()
            break
        except:
            traceback.print_exc()
            print('trying again not now is disturbing')
        time.sleep(3)
    for user_name in user_name_array:
        driver.get('https://www.instagram.com/direct/new/')
        time.sleep(random.randint(5,9))
        try:
            #search bar
            newmessage = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
            time.sleep(1)
            newmessage = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input')               
            newmessage.send_keys(user_name)
            time.sleep(random.randint(5,9))
            #searched for user now send new message
            newmessage = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/button')                                        
            newmessage.click()
            nextbutton = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/button')                                        
            nextbutton.click()
            time.sleep(random.randint(5,9))
            #typing message
            message=random.choice(user["dm"])
            time.sleep(random.randint(5,9))
            newmessage = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')                                        
            newmessage.send_keys(message)
            time.sleep(10)
            newmessage.send_keys('\n')
            pass
        except:
            traceback.print_exc()
            print('could not message trying next')
            pass        
    driver.quit()
    #now wait 45 minutes before starting another process 40-50 minutes
    print('process ended now wasting time')
    time.sleep(random.randint( 40*60 , 50*60 ))
