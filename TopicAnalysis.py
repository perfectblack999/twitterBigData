__author__ = 'perfectblack999'
import tweet_stats
import CalculatePercentageChange
# import twitter_practice
import getTopTweets
import getTopTweeters
import BingSearch
import csv

def calculateAverageSentimentTrends():
    tweetStatsFileName = tweet_stats()

def findPercentageChange():
    percentChangeFileName = CalculatePercentageChange.PercentChange('rawsentimentstats.csv')

def getGreatestPercentageChange():
    CalculatePercentageChange.greatestPercentageChange('percentChangeStats_20151127130559.csv', 3)

# def gatherTweets():
#     twitter_practice()

def getImpactfulTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange):
    tweetFileName = getTopTweets.getTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    return tweetFileName

def getImpactfulHandles(fileName, shelf):
    handles, handleFileName = getTopTweeters.getTopTweeters(fileName, shelf)
    return handles, handleFileName

def getHandleInfo(query, searchType):
    BingSearch.bing_search(query, searchType)

# Todo: need to create foreign key to link tweets with handles with search results
def analyzeAPeriod(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange):
    retweetTweetFileName = getImpactfulTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    followerTweetFileName = getImpactfulTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    favoriteTweetFileName = getImpactfulTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    positiveRetweetHandles, positiveRetweetHandleFileName = getImpactfulHandles(retweetTweetFileName, '91To100')
    positiveFollowerHandles, positiveFollowerHandleFileName = getImpactfulHandles(followerTweetFileName, '91To100')
    positiveFavoriteHandles, positiveFavoriteHandleFileName = getImpactfulHandles(favoriteTweetFileName, '91To100')
    negativeRetweetHandles, negativeRetweetHandleFileName = getImpactfulHandles(retweetTweetFileName, '0To10')
    negativeFollowerHandles, negativeFollowerHandleFileName = getImpactfulHandles(followerTweetFileName, '0To10')
    negativeFavoriteHandles, negativeFavoriteHandleFileName = getImpactfulHandles(favoriteTweetFileName, '0To10')

    retweetTweetFile = open(retweetTweetFileName, 'r')
    tweetReader = list(csv.DictReader(retweetTweetFile))

    for handles in positiveRetweetHandles:
        for tweet in tweetReader:
            if tweet['tweet_request_id'] == handles[0]:
                print tweet['raw_tweet']
                print handles[1:]
                justHandles = handles[1:]

                for handle in justHandles:
                    print BingSearch.bing_search(handle, 'Web')

analyzeAPeriod('carson', 25, 'rt_normalized', '2015-11-00 00:00:00', '2015-11-10 00:00:00')