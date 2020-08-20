import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://dbuser:JZf111qVS2zqKVfs@addmie-ybdhy.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["bot"]
collection=db["hashtag"]
#follow hastags
followedtoday='#follow#followback#likes#f#followme#followforfollow#followbackteam#followforfollowback#followmeplease#followers'
followedtoday=followedtoday.split('#')[1:]
#comment hastags
comments='#follow#comments#comment4comment#love#instagood#photooftheday#fashion#Beautiful#like4like#picoftheday#art#happy#photography#instagram#followme#style#instadaily#travel#life#cute#fitness#nature#beauty#girl#fun#photo#amazing#likeforlike#instalike#Selfie#smile#me#lifestyle#model#follow4follow#music#friends#motivation#like#food#inspiration#Repost#summer#design#makeup#TBT#followforfollow#ootd#Family#l4l#cool#igers#TagsForLikes#hair#instamood#sun#vsco#fit#beach#photographer#gym#artist#girls#vscocam#autumn#pretty#luxury#instapic#black#sunset#funny#sky#blogger#hot#healthy#work#bestoftheday#workout#f4f#nofilter#london#goals#blackandwhite#blue#swag#health#party#night#landscape#nyc#happiness#pink#lol#foodporn#newyork#fitfam#awesome#fashionblogger#Halloween#Home#fall#paris'
comments=comments.split('#')[1:]
#messages hastags
messages='#india#love#instagood#photography#engineer'
messages=messages.split('#')[1:]

for i in range(len(followedtoday)):
    followedtoday[i]='https://www.instagram.com/explore/tags/'+followedtoday[i]+'/'
for i in range(len(comments)):
    comments[i]='https://www.instagram.com/explore/tags/'+comments[i]+'/'
for i in range(len(messages)):
    messages[i]='https://www.instagram.com/explore/tags/'+messages[i]+'/'

print(followedtoday,comments)
##inserting##
collection.insert_one({"_id":0,"comments":comments,"follows":followedtoday,"dm":messages})
