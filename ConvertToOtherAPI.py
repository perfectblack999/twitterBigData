__author__ = 'perfectblack999'

import requests, urllib, pprint
import sqlite3 as sql
import csv
import time
import unirest

connection = sql.connect('/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects/tweets.sqlite')
connection.text_factory = str
tweet_data = []
tweet_count = 0
tweet_list = []
mashape_key = 'gIUzJXTpYEmshon0ZKQJlivtJtGkp19XNxvjsnXODF47IvZo6o'

with connection:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tweet_text")
    tweet_data = cursor.fetchall()

tweetSentimentAPI = open("twinworddotcom.csv", "wb")
writer=csv.writer(tweetSentimentAPI,delimiter=',')

# for index in range(49001,49120):
#     print tweet_data[index][2]
#     text = urllib.quote_plus(tweet_data[index][2])
#     key = '268c4eac6fe109c7768b2d3a49ee00ce38ddc1a1'
#     url = "https://www.tweetsentimentapi.com/api/?key=%s&text=%s" % (key, text)
#     r = requests.get(url)
#     tweet_list.append((index, tweet_data[index][2], r.json()['sentiment'], r.json()['score']))
#     writer.writerow((index, tweet_data[index][2], r.json()['sentiment'], r.json()['score']))
#     time.sleep(60)

for index in range(49001,49120):
    print tweet_data[index][2]
    text = tweet_data[index][2]

    # These code snippets use an open-source library. http://unirest.io/python
    response = unirest.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
      headers={
        "X-Mashape-Key": "gIUzJXTpYEmshon0ZKQJlivtJtGkp19XNxvjsnXODF47IvZo6o",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      },
      params={
        "text": text
      }
    )
    print response.body

    tweet_list.append((index, tweet_data[index][2], response.body['type'], response.body['score'], response.body['ratio']))
    writer.writerow((index, tweet_data[index][2], response.body['type'], response.body['score'], response.body['ratio']))


tweetSentimentAPI.close()