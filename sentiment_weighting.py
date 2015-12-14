__author__ = 'perfectblack999'

import csv
import sqlite3 as sql

connection = sql.connect('/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects/tweets.sqlite')
connection.text_factory = str
weighted_data = []
data_maxes = []
normalized_data_list = []

# Get the twitter data
with connection:
    cursor = connection.cursor()

    cursor.execute("SELECT rowid, sentiment, followers, retweet_count, favorite_count FROM tweet_text")
    tweet_data = cursor.fetchall()

    cursor.execute("select MAX(followers), MAX(retweet_count), MAX(favorite_count) FROM tweet_text")
    data_maxes = cursor.fetchone()

# Calculate the weighted values
for row in tweet_data:
    if row[0] is not None:
        rowID = float(row[0])
    else:
        rowID = float(0)

    if row[1] is not None:
        sentiment = float(row[1])
    else:
        sentiment = float(0)

    if row[2] is not None:
        followers = float(row[2])
    else:
        followers = float(0)

    if row[3] is not None:
        retweets = float(row[3])
    else:
        retweets = float(0)

    if row[4] is not None:
        favorites = float(row[4])
    else:
        favorites = float(0)

    weighted_data.append((rowID, (sentiment * followers) / data_maxes[0], (sentiment * retweets) / data_maxes[1],
                          (sentiment * favorites) / data_maxes[2], retweets / data_maxes[1], followers / data_maxes[0],
                          favorites / data_maxes[2]))
    # print "followers/max_followers: " + str(followers) + "/" + str(data_maxes[0]) + " retweets/max_retweets: " + str(retweets) + "/" + str(data_maxes[1]) + " favorites/max_favorites: " + str(favorites) + "/" + str(data_maxes[2])
    # print (rowID, (sentiment * followers) / data_maxes[0], (sentiment * retweets) / data_maxes[1],
    #                       (sentiment * favorites) / data_maxes[2], float(retweets / data_maxes[1]), float(followers / data_maxes[0]),
    #        float(favorites / data_maxes[2]))

print "data maxes: followers, rt, favorites"
print data_maxes

# Put weighted values back in
with connection:
    cursor = connection.cursor()

    for row in weighted_data:
        cursor.execute("UPDATE tweet_text SET followers_weighted_sentiment = (?), rt_weighted_sentiment = (?), "
                       "fav_weighted_sentiment = (?), rt_normalized = (?), followers_normalized = (?), fav_normalized = (?) WHERE rowid = (?) ",
                       (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))

# get the weighted values
    cursor.execute("SELECT MAX(followers_weighted_sentiment), MAX(rt_weighted_sentiment), MAX(fav_weighted_sentiment) FROM tweet_text")
    data_maxes = cursor.fetchone()
    # print data_maxes

    cursor.execute("SELECT rowid, followers_weighted_sentiment, rt_weighted_sentiment, fav_weighted_sentiment FROM tweet_text")
    normalized_data = cursor.fetchall()

# Calculate the normalized weighted values
    for row in normalized_data:
        if row[0] is not None:
            rowID = row[0]
        else:
            rowID = 0

        if row[1] is not None:
            followersWeightedSentiment = row[1]
        else:
            followersWeightedSentiment = 0

        if row[2] is not None:
            rtWeightedSentiment = row[2]
        else:
            rtWeightedSentiment = 0

        if row[3] is not None:
            favWeightedSentiment = row[3]
        else:
            favWeightedSentiment = 0

        normalized_data_list.append((rowID, (followersWeightedSentiment) / data_maxes[0], (rtWeightedSentiment) / data_maxes[1], (favWeightedSentiment) / data_maxes[2]))
        # print (rowID, (followersWeightedSentiment) / data_maxes[0], (rtWeightedSentiment) / data_maxes[1], (favWeightedSentiment) / data_maxes[2])

with connection:
    cursor = connection.cursor()
    for row in normalized_data_list:
        cursor.execute("UPDATE tweet_text SET followers_normalized_sentiment = (?), rt_normalized_sentiment = (?), fav_normalized_sentiment = (?)  WHERE rowid = (?)", (row[1], row[2], row[3], row[0]))