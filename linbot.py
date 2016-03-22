# linbot
# by daniel sngiem

# polls @lin_manuel's account for his location every minute
# if it changes, it posts to @linmanuelishere

import tweepy
import time

consumerKey = "8yfryf5JvvjeBOG4mUs42fWWg"
consumerSecret = "yHGOeK1iLgq8IpW0pz7SYXi2W2oXGHORrqEMkGgKtjfiHw1Klk"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)

accessToken = "712089131778703360-MxbfGqF9oSHTvnBvVknWmTiHc1Y3ojl"
accessTokenSecret = "xX1pFsMga44heuogml8snp8zPFW0PTDAy3jPLWQ7XePax"

auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

def updateStatus():

    #get lin location
    linUser = api.get_user("lin_manuel")
    linLocation = linUser.location.strip()

    #get my last tweet
    myTimeline = api.user_timeline("whereslinmanuel", count=1)
    
    if len(myTimeline) > 0:
        myLastLocation = myTimeline[0].text.strip()
    else:
        myLastLocation = u""


    if linLocation != myLastLocation:
        api.update_status(linLocation)
        return "update my status. current location: " + linLocation

    else:
        return "location has not changed from: " + myLastLocation



if __name__ == '__main__':
    while True:
		updateStatus()
		time.sleep(60)