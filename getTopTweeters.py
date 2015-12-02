__author__ = 'perfectblack999'
import csv
import sqlite3 as sql
import pprint
from time import strftime

def getTopTweeters(fileName, shelf):
    tweetFile = open(fileName, 'r')
    tweetFileInput = csv.DictReader(tweetFile)
    line_handles = []
    twitter_handles = []

    for line in tweetFileInput:
        if line['shelf'] == shelf or shelf == 'all':
            handles = [word for word in str(line['raw_tweet']).split() if word.startswith('@')]
            for handle in handles:
                handle = handle.replace(":", "")
                if handle not in line_handles:
                    line_handles.append(handle)
            if "@" + line['screen_name'] not in line_handles:
                line_handles.append("@" + line['screen_name'])
            line_handles.insert(0, line['tweet_request_id'])
        if line_handles:
            twitter_handles.append(line_handles)
        line_handles = []

    print(twitter_handles)
    print(len(twitter_handles))

    outputFileName = "topTweeters_" + strftime("%Y%m%d%H%M%S") + ".csv"
    topTweetersFile = open(outputFileName, "wb")
    writer = csv.writer(topTweetersFile, delimiter = ",")
    for line in twitter_handles:
        writer.writerow(line)

    topTweetersFile.close()
    return twitter_handles, outputFileName

tweetFileName = 'topTweetOutput_20151201203108.csv'
topTweeters = getTopTweeters(tweetFileName, '91To100')