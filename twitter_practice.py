##############################################################################
## To access Twitter ##
##############################################################################
import tweepy
import indicoio
import sqlite3 as sql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    indicoio.config.api_key = '568b95dbd872c89618448e76a809c715'
    auth = tweepy.OAuthHandler('I8WduwyyITtt61j61rxLGnE5T','Fesofuet7mzLhjdZYCLHkxHR2BbMainTjHv2Bk65FhFsFhrjLj')
    api = tweepy.API(auth)
    searchWords = open("/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects/search_words.txt", "r")

    tweetList = []
    searchWordList = searchWords.read().split(',')

    for searchWord in searchWordList:
        tweetList.append((tweepy.Cursor(api.search, q = searchWord, show_user = "true").items(25), searchWord))

    connection = sql.connect('/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects/tweets.sqlite')
    connection.text_factory = str

    with connection:
        cursor = connection.cursor()
        # iterate through the tweets and put them in database
        for searchWordTweet in tweetList:
            searchWord = searchWordTweet[1]
            searchWordTweetList = []

            for tweet in searchWordTweet[0]:
                # find all words that start with "@" or a link
                handles = [word for word in str(tweet.text.encode('utf8')).split() if word.startswith('@')]
                links = [word for word in str(tweet.text.encode('utf8')).split() if word.startswith('http')]
                clean_tweet = str(tweet.text.encode('utf8'))

                for handle in handles:
                    handle = handle + " "
                    clean_tweet = clean_tweet.replace(handle, "")
                for link in links:
                    link = link
                    clean_tweet = clean_tweet.replace(link, "")

                clean_tweet = clean_tweet.replace("#", "")
                clean_tweet = clean_tweet.replace("RT ", "")

                # Make sure there are no empty strings
                if(clean_tweet == ""):
                    clean_tweet = "empty"

                tweet_insert = (str(tweet.created_at), tweet.text.encode('utf8'), clean_tweet, indicoio.sentiment(clean_tweet), str(searchWord), str(tweet.user.screen_name), tweet.user.followers_count, tweet.retweet_count, tweet.favorite_count)
                cursor.execute("INSERT INTO tweet_text (date, raw_tweet, clean_tweet, sentiment, filter, screen_name, followers, retweet_count, favorite_count) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", tweet_insert)
                # pprint.pprint("tweet_insert: " + str(tweet_insert))

    # send confirmation email
    fromEmail = "nkembigdata@gmail.com"
    toEmail = "nkembigdata@gmail.com"
    pw = "IAmAnEngineer10."
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg["To"] = toEmail
    msg['Subject'] = "Nkem, Your Script Ran!"

    body = "Hey Nkem, your script ran successfully! Hope you're having a great day! :)"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromEmail, pw)
    text = msg.as_string()
    server.sendmail(fromEmail, toEmail, text)
    server.quit

if __name__ == "__main__":
   main()


