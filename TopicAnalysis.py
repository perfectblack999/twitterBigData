__author__ = 'perfectblack999'
import tweet_stats
import CalculatePercentageChange
import twitter_practice
import getTopTweets
import getTopTweeters
import BingSearch
import csv

def main(function):

    # need to put an if statement for functions in
    if function == "tweetStats":
        tweetStatsFileName, dates, subjectsAndSentiments, subjectList = tweet_stats.main()
        return tweetStatsFileName, dates, subjectsAndSentiments, subjectList
    elif function == "percentChange":
        percentChangeFileName = CalculatePercentageChange.PercentChange('rawsentimentstats.csv')
    elif function == "greatestPercentChange":
        CalculatePercentageChange.greatestPercentageChange('percentChangeStats_20151127130559.csv', 3)
    elif function == "gatherTweets":
        twitter_practice()

def getImpactfulTweets(filter=None, numOfTweets=None, rankCriteria=None, beginDateRange=None, endDateRange=None):
    tweetFileName = getTopTweets.main(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    return tweetFileName

def getImpactfulHandles(fileName=None, shelf=None):
    handles, handleFileName = getTopTweeters.main(fileName, shelf)
    return handles, handleFileName

def getHandleInfo(query=None, searchType=None):
    BingSearch.bing_search(query, searchType)

# Todo: need to create foreign key to link tweets with handles with search results
def analyzeAPeriod(filter=None, numOfTweets=None, rankCriteria=None, shelf=None, beginDateRange=None, endDateRange=None):
    tweetFileName = getImpactfulTweets(filter, numOfTweets, rankCriteria, beginDateRange, endDateRange)
    if tweetFileName:
        impactfulHandles, handleFileName = getImpactfulHandles(tweetFileName, shelf)

        retweetTweetFile = open(tweetFileName, 'r')
        tweetReader = list(csv.DictReader(retweetTweetFile))

        tweetDict = {}
        tweetHandlesDict = {}

        tweetDict['shelf'] = shelf
        for handles in impactfulHandles:
            for tweet in tweetReader:
                if tweet['tweet_request_id'] == handles[0]:
                    tweetHandlesDict["tweet"] = tweet['raw_tweet']
                    tweetHandlesDict["handles"] = handles[1:]
                    justHandles = handles[1:]

                    for handle in justHandles:
                        searchResult = BingSearch.bing_search(handle, 'Web')

                        tweetHandlesDict[handle] = searchResult
                    tweetDict[tweet['tweet_request_id']] = tweetHandlesDict
                    tweetHandlesDict = {}


        return tweetDict

if __name__ == "__main__":
   main("tweetStats")