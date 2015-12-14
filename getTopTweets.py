__author__ = 'perfectblack999'
import csv
import sqlite3 as sql
from time import strftime

def main(filter, numberOfTweets, rankCriteria, beginDateRange, endDateRange):
    outputFileName = None

    if filter and numberOfTweets and rankCriteria and beginDateRange and endDateRange:
        connection = sql.connect('/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects/tweets.sqlite')
        connection.text_factory = str

        with connection:
            cursor = connection.cursor()
            # cursor.execute("SELECT * FROM tweet_text WHERE filter = 'carson' AND screen_name NOT LIKE '%' || 'carson' || '%' AND date BETWEEN '2015-10-00 00:00:00' AND '2015-11-08 00:00:00' ORDER BY rt_weighted_sentiment DESC LIMIT 100")
            cursor.execute("SELECT * FROM tweet_text WHERE filter = ? AND screen_name NOT LIKE '%' || ? || '%' AND date BETWEEN ? AND ? ORDER BY " + rankCriteria + " DESC LIMIT ?", (filter, filter, beginDateRange, endDateRange, numberOfTweets))
            tweets = cursor.fetchall()

        tweets0To10 = []
        tweets11To20 = []
        tweets21To30 = []
        tweets31To40 = []
        tweets41To50 = []
        tweets51To60 = []
        tweets61To70 = []
        tweets71To80 = []
        tweets81To90 = []
        tweets91To100 = []

        for tweet in tweets:
            if tweet[3] > .9:
                tweets91To100.append(tweet)
            elif tweet[3] > .8:
                tweets81To90.append(tweet)
            elif tweet[3] > .7:
                tweets71To80.append(tweet)
            elif tweet[3] > .6:
                tweets61To70.append(tweet)
            elif tweet[3] > .5:
                tweets51To60.append(tweet)
            elif tweet[3] > .4:
                tweets41To50.append(tweet)
            elif tweet[3] > .3:
                tweets31To40.append(tweet)
            elif tweet[3] > .2:
                tweets21To30.append(tweet)
            elif tweet[3] > .1:
                tweets11To20.append(tweet)
            else:
                tweets0To10.append(tweet)

        outputFileName = "topTweetOutput_" + strftime("%Y%m%d%H%M%S") + ".csv"
        topTweetOutputFile = open(outputFileName, "wb")
        writer = csv.writer(topTweetOutputFile, delimiter=',')
        writer.writerow(('date', 'raw_tweet', 'clean_tweet', 'sentiment', 'filter', 'screen_name', 'followers', 'retweet_count',
                        'favorite_count', 'rt_weighted_sentiment', 'favorite_weighted_sentiment', 'follower_weighted_sentiment',
                         'rt_normalized_sentiment', 'fav_normalized_sentiment', 'follower_normalized_sentiment', 'rt_normalized',
                         'followers_normalized', 'fav_normalized', 'shelf', 'tweet_request_id'))

        tweetRequestID = 0

        for tweet in tweets91To100:
            writer.writerow(tweet + ('91To100', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets81To90:
            writer.writerow(tweet + ('81To90', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets71To80:
            writer.writerow(tweet + ('71To80', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets61To70:
            writer.writerow(tweet + ('61To70', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets51To60:
            writer.writerow(tweet + ('51To60', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets41To50:
            writer.writerow(tweet + ('41To50', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets31To40:
            writer.writerow(tweet + ('31To40', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets21To30:
            writer.writerow(tweet + ('21To30', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets11To20:
            writer.writerow(tweet + ('11To20', tweetRequestID,))
            tweetRequestID += 1
        for tweet in tweets0To10:
            writer.writerow(tweet + ('0To10', tweetRequestID,))
            tweetRequestID += 1

        topTweetOutputFile.close()

    return outputFileName;

if __name__ == "__main__":
   main()

# getTweets('carson', 25, 'rt_normalized', '2015-11-00 00:00:00', '2015-11-10 00:00:00')