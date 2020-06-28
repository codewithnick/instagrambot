from selenium import webdriver
import time
import random
import os
dailylimit=50
commentarray=['https://www.instagram.com/explore/tags/comment4comment/',
              'https://www.instagram.com/explore/tags/comments/',
              'https://www.instagram.com/explore/tags/like4like/',
              'https://www.instagram.com/explore/tags/followme/',
              'https://www.instagram.com/explore/tags/follow/',
              ]
var='#love#instagood#photooftheday#fashion#Beautiful#like4like#picoftheday#art#happy#photography#instagram#followme#style#follow#instadaily#travel#life#cute#fitness#nature#beauty#girl#fun#photo#amazing#likeforlike#instalike#Selfie#smile#me#lifestyle#model#follow4follow#music#friends#motivation#like#food#inspiration#Repost#summer#design#makeup#TBT#followforfollow#ootd#Family#l4l#cool#igers#TagsForLikes#hair#instamood#sun#vsco#fit#beach#photographer#gym#artist#girls#vscocam#autumn#pretty#luxury#instapic#black#sunset#funny#sky#blogger#hot#healthy#work#bestoftheday#workout#f4f#nofilter#london#goals#blackandwhite#blue#swag#health#party#night#landscape#nyc#happiness#pink#lol#foodporn#newyork#fitfam#awesome#fashionblogger#Halloween#Home#fall#paris'
var=var.split('#')
for i in range(1,len(var)):
    var[i]='https://www.instagram.com/explore/tags/'+var[i]+'/'
    commentarray.append(var[i])
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.instagram.com/')
time.sleep(0.5)
f = open("username.txt", "r")
a=f.read()
f = open("password.txt", "r")
b=f.read()
f = open("comment.txt", "r")
message=f.read()
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

        
while dailylimit>0:
    try:
        linkvar=random.choice(commentarray)
        print(linkvar)
        driver.get(linkvar)
        time.sleep(random.randint(5,9))
        postlink = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a').get_attribute('href')
        driver.get(postlink)
        time.sleep(random.randint(5,9))
        postbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[2]/button')
        postbutton.click()
        commentbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
        commentbutton.send_keys(message)
        postbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div[1]/form/button')
        postbutton.click()
        dailylimit-=1
        time.sleep(random.randint(5,9))
        print('commented on '+postlink)
    except:
        print('could not comment trying next post')
print('daily commenting limit reached')
