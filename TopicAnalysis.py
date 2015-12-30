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
        originalTweetList = []
        originalIdList = []
        originalHandlesList = []

        for tweet in tweetReader:
            if tweet['raw_tweet'] not in originalTweetList:
                originalTweetList.append(tweet['raw_tweet'])
                originalIdList.append(tweet['tweet_request_id'])
                for handles in impactfulHandles:
                    if handles[0] == tweet['tweet_request_id']:
                        originalHandlesList.append(handles[1:])
            else:
                # Add new handles to the original tweet
                tweetIndex = originalTweetList.index(tweet['raw_tweet'])
                for handles in impactfulHandles:
                    if handles[0] == tweet['tweet_request_id']:
                        for handle in handles[1:]:
                            if handle not in originalHandlesList[tweetIndex]:
                                originalHandlesList[tweetIndex].append(handle)


        tweetDict['shelf'] = shelf
        for i in range(0,len(originalTweetList) - 1):
            tweetHandlesDict['tweet'] = originalTweetList[i]
            tweetHandlesDict['handles'] = originalHandlesList[i]

            for handle in originalHandlesList[i]:
                searchResult = BingSearch.bing_search(handle, 'Web')
                tweetHandlesDict[handle] = searchResult

            tweetDict[originalIdList[i]] = tweetHandlesDict
            tweetHandlesDict = {}

        return tweetDict

if __name__ == "__main__":
   main("tweetStats")