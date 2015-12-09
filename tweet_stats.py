import csv
import sqlite3 as sql
from time import strftime

def addTweetsToDB():
    connection = sql.connect('/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects/tweets.sqlite')
    connection.text_factory = str

    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT avg(sentiment), filter, strftime('%m-%d-%Y', date) as valDay FROM tweet_text GROUP BY filter, valDay")
        stats = cursor.fetchall()

    # print(stats)
    datesCollected = ['subject']

    # Get all the dates in the sqlite database
    for stat in stats:
        if stat[2] not in datesCollected:
            datesCollected.append(stat[2])

    # Write the top row into the file
    outputFileName = "rawSentimentStats_" + strftime("%Y%m%d%H%M%S") + ".csv"
    rawSentimentStats = open(outputFileName, "wb")
    writer=csv.writer(rawSentimentStats,delimiter=',')
    writer.writerow(datesCollected)

    subjectList = []
    for stat in stats:
        if stat[1] not in subjectList:
            subjectList.append(stat[1])

    found = 0
    subjectAndSentimentsRowList = []
    for subject in subjectList:
        subjectAndSentimentsRow = [subject]
        for date in datesCollected[1:]:
            for stat in stats:
                # If the subject and date match up then put the average in this spot, if not found, put a 0
                if stat[2] == date and stat[1] == subject:
                    found = 1
                    break;
            if found == 1:
                subjectAndSentimentsRow.append(stat[0])
                found = 0
            else:
                subjectAndSentimentsRow.append(0)
        subjectAndSentimentsRowList.append(subjectAndSentimentsRow)

    # Write the row into the output file
    for subjectAndSentimentsRowPrint in subjectAndSentimentsRowList:
        writer.writerow(subjectAndSentimentsRowPrint)
        # print subjectAndSentimentsRowPrint

    rawSentimentStats.close()

    return outputFileName