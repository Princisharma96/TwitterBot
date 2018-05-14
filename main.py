from twitter import Twitter, OAuth
import tweepy
import re
from termcolor import colored
from textblob import TextBlob
from paralleldots import set_api_key, get_api_key, sentiment
import nltk
from nltk.corpus import *
from nltk import Counter
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

print ("\033[35;40m********************************************************************************************************************************************************************************************")
print (colored("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t WELCOME TO TWITTERBOT " , color= 'blue', attrs=['bold']))

#-----------------------------------------------------------------------------------------------------------------------
# CREDENTIALS
API_KEY = 'tWlZPllDzXGvuRaPYBMu82WjE'
API_SECRET = 'cBWdZn91zmX7LtQI8UczNdFC66TdkPdDHfLS9lVkpEN4cwDJxL'
ACCESS_TOKEN = '410532691-IK0YkbvXH4A0SVrgHiuKHWVpB4Srq9fGhsj1zAmr'
ACCESS_TOKEN_SECRET = 'Ag3H99umpVoaaY51Tzf5p6DIKdugDQuKEfMzkDQoud41H'

#-----------------------------------------------------------------------------------------------------------------------

twitter_oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth = twitter_oauth)

oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(oauth)

#-----------------------------------------------------------------------------------------------------------------------

#FOR DISPLAYING MY ACCOUNT DETAILS
def details():
    myaccount = api.me()
    print (colored("\n Personal Details", color='blue', attrs=['underline']))
    print 'Name: '  + myaccount.name
    print 'Location: ' + myaccount.location
    print 'Friends: ' + str(myaccount.friends_count)
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='green'))
#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING QUERY

def get_tweets(query):
    tweets = twitter.search.tweets(q='#' +query, count=200)
    return tweets
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='green'))

#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING NUMBER OF FOLLOWERS

def get_num_followers(query):
    num_followers = 0
    tweets = get_tweets(query)
    #print type(tweets)
    for each_tweet in tweets['statuses']:
        print (colored("*****************************************************************************************"
               "********************************************************************************************", color= 'green'))
        print "Name: " + each_tweet['user']['screen_name']
        print "Followers: " + str(each_tweet['user']['followers_count'])
        # print each_tweet['user']['location']
        num_followers += each_tweet['user']['followers_count']
    return  num_followers
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='green'))
#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING SENTIMENTS

def get_sentiments(query):
    p = 0
    n=0
    ne = 0
    set_api_key('YjTdGL5qoPMia9yaiziaUjTL2uEvRWFBFu3Rp0sdbd0')
    get_api_key()
    public_tweets = api.search(query)
    for tweet in public_tweets:
        text = tweet.text
        print (colored("*****************************************************************************************"
                       "********************************************************************************************",
                       color='green'))
        print (colored(tweet.text, color='red'))
        r = sentiment(tweet.text)
        print(colored(r, color= 'red'))
        result = r['sentiment']
        if result == "positive":
            p = p+1
        elif  r['sentiment'] == "neutral":
            n = n+1
        else:
            ne = ne+1
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='blue'))
    print "Maximum positive comments: ", p
    print "Maximum neutral comments: ", n
    print "Maximum negative comments: ", ne
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='blue'))

#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING LOCATION, LANGUAGE AND TIME ZONE

def llt(query):

    public_tweets = get_tweets(query)
    lo = {}
    la = {}
    tz = {}
    for tweet in public_tweets ['statuses']:


        print (colored("Time Zone: ", color='red', attrs=['bold']) + tweet['user']['created_at'])
        print (colored("Language: ", color='red', attrs=['bold']) + tweet['user']['lang'])
        print (colored("Location: ", color='red', attrs=['bold']) + tweet['user']['location'])
        print (colored("*****************************************************************************************"
                       "********************************************************************************************",
                       color='green'))


#-----------------------------------------------------------------------------------------------------------------------

# FOR COMPARISION OF MODI AND TRUMP TWEETS

def Comparision():

    # FOR MODI
    count = 0
    new_tweets = api.user_timeline(screen_name = '@narendramodi', count = 200, tweet_mode='extended')
    for tweet in new_tweets:
        print(tweet.full_text)
        text = tweet.full_text
        temp = []
        temp.append(text)
        temp1 = temp
        words = re.sub(r"http\S+", "", str(temp1))
        word = words.split()
        for i in word:
            i = i.upper()
            if i == "USA" or i == "US" or i == "America" or i == "United States of America":
                count = count + 1
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='green'))
    print "Number of times Narendra Modi mentioned 'USA', 'US', 'United States Of America:' or 'America':" , count


    #FOR TRUMP
    count1 = 0
    new_tweets = api.user_timeline(screen_name='@realDonaldTrump', count=200, tweet_mode='extended')
    for tweet in new_tweets:
        print(tweet.full_text)
        text = tweet.full_text
        temp = []
        temp.append(text)
        temp1 = temp
        words = re.sub(r"http\S+"," ", str(temp1))
        word = words.split()
        for i in word:
            i = i.lower()
            if i == "India" or i == "INDIA":
                count1 = count1 + 1
    print "Number of times Donald Trump mentioned 'India': ", count1
    print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='green'))

#-----------------------------------------------------------------------------------------------------------------------

# FOR DETERMINING TOP USAGE STOPWORDS

def Topusage():
    new_tweets = api.user_timeline(screen_name='@narendramodi', count=200, tweet_mode='extended')
    for tweet in new_tweets:
        #print(tweet.full_text)
        temp = []
        temp.append(tweet.full_text)
        temp1 = temp
        import re
        words = re.sub(r"http\S+"," ", str(temp1))
        word = words.split()
        word1 = [w for w in word if w in stop_words]
        for w in word1:
            if w not in stop_words:
                word1.append(w)
        num = Counter(word1).most_common(10)
        #print word1
        print(num)

#-----------------------------------------------------------------------------------------------------------------------

# FOR UPDATING STATUS

def tweet_status():
    status = raw_input("Enter your new tweet: ")
    api.update_status(status)

#-----------------------------------------------------------------------------------------------------------------------

# MAIN FUNCTION

def main():
 print (colored("*****************************************************************************************"
                   "********************************************************************************************",
                   color='red'))
 while (True):

     user_choice = input("\nWhat would you like to do? Choose the option \n"
                   "1. Display my Twitter details.\n"
                   "2. Count the number of followers. \n"
                   "3. Determine the sentiments of people Tweeting using a certain hash tag. \n"
                   "4. Determining the location, timezone and language of people Tweeting using a certain hash tag. \n"
                   "5. Comparision of tweets by Narendera Modi and Donald Trump. \n"
                   "6. Determining Top Usage. \n"
                   "7. Tweet a message from your account. \n"
                   "8. Exit\n"
                   "User Choice: ")

     if user_choice == 1:
         details()

     elif user_choice == 2:
        print ("Chosen to count the number of followers.")
        user_input = raw_input("Enter the hash tag: ")
        print "\n Maximum number of people who might have seen this has tag are: %s " % (get_num_followers(user_input))

     elif user_choice == 3:
         user_input = raw_input("Enter the hash tag: ")
         get_sentiments(user_input)

     elif user_choice == 4:
        user_input = raw_input("Enter the hash tag: ")
        llt(user_input)

     elif user_choice == 5:
        Comparision()

     elif user_choice == 6:
          Topusage()

     elif user_choice == 7:

         tweet_status()

     elif user_choice == 8:
       break
     else:
        print("wrong choice try again.")
        exit()
main()