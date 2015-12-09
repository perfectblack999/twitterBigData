__author__ = 'perfectblack999'
import tweet_stats
import CalculatePercentageChange
import twitter_practice
import getTopTweets
import getTopTweeters
import BingSearch
import csv

def main(function, filter, numOfTweets, rankCriteria, shelf, beginDateRange, endDateRange):

    # need to put an if statement for functions in
    if function == "tweetStats":
        tweetStatsFileName = tweet_stats()
    elif function == "percentChange":
        percentChangeFileName = CalculatePercentageChange.PercentChange('rawsentimentstats.csv')
    elif function == "greatestPercentChange":
        CalculatePercentageChange.greatestPercentageChange('percentChangeStats_20151127130559.csv', 3)
    elif function == "gatherTweets":
        twitter_practice()
    elif function == "getImpactfulTweets":
        tweetFileName = getTopTweets.getTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)


def getImpactfulHandles(fileName, shelf):
    handles, handleFileName = getTopTweeters.main(fileName, shelf)
    return handles, handleFileName

def getHandleInfo(query, searchType):
    BingSearch.bing_search(query, searchType)

# Todo: need to create foreign key to link tweets with handles with search results
def analyzeAPeriod(filter, numOfTweets, rankCriteria, shelf, beginDateRange, endDateRange):
    tweetFileName = getImpactfulTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    impactfulHandles, handleFileName = getImpactfulHandles(tweetFileName, shelf)

    retweetTweetFile = open(tweetFileName, 'r')
    tweetReader = list(csv.DictReader(retweetTweetFile))

    positiveRetweetList = []

    for handles in impactfulHandles:
        for tweet in tweetReader:
            if tweet['tweet_request_id'] == handles[0]:
                # print tweet['raw_tweet']
                # print handles[1:]
                positiveRetweetList.append(tweet['raw_tweet'])
                positiveRetweetList.append(handles[1:])
                justHandles = handles[1:]

                for handle in justHandles:
                    searchResult = BingSearch.bing_search(handle, 'Web')
                    # print searchResult
                    positiveRetweetList.append(handle)
                    positiveRetweetList.append(BingSearch.bing_search(handle, 'Web'))

    return positiveRetweetList

if __name__ == "__main__":
   main()