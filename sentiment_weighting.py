__author__ = 'perfectblack999'

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

    weighted_data.append((rowID, retweets / data_maxes[1], followers / data_maxes[0], favorites / data_maxes[2]))

print "data maxes: followers, rt, favorites"
print data_maxes

# Put normalized values back in
with connection:
    cursor = connection.cursor()

    for row in weighted_data:
        cursor.execute("UPDATE tweet_text SET rt_normalized = (?), followers_normalized = (?), fav_normalized = (?) WHERE rowid = (?) ",
                       (row[1], row[2], row[3], row[0]))