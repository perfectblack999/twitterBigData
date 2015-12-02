__author__ = 'perfectblack999'
import csv
from time import strftime
import operator
import collections

def PercentChange(fileName):
    statsFile = open(fileName, "r")
    statsDict = list(csv.DictReader(statsFile))

    # Write the top row into the file
    outputFileName = "percentChangeStats_" + strftime("%Y%m%d%H%M%S") + ".csv"
    percentChangeStats = open(outputFileName, "wb")
    writer=csv.writer(percentChangeStats, delimiter=',')

    # Get all the dates in order
    i = 0
    for line in statsDict:
        if i > 0:
            break
        else:
            dates = line.keys()
    dates.remove('subject')
    dates.sort()
    percentChangeList = [['subject'] + dates]

    # Calculate the percentage change numbers and put it in a list
    for line in statsDict:
        subjectList = []
        subjectList.append(line['subject'])
        # Because you wouldn't have a percentage change for the first day
        subjectList.append(0)

        for i in range(0,len(dates) - 1):
            if float(line[dates[i]]) == 0:
                subjectList.append(0)
            else:
                subjectList.append(((float(line[dates[i+1]]) - float(line[dates[i]])) / float(line[dates[i]])) * 100)
        percentChangeList.append(subjectList)

    for percentChange in percentChangeList:
        writer.writerow(percentChange)
    percentChangeStats.close()

    return outputFileName

def greatestPercentageChange(fileName, numberOfDays):
    statsFile = open(fileName, "r")
    statsDict = csv.DictReader(statsFile)
    topPercentChangeList = []
    bottomPercentChangeList = []

    for line in statsDict:
        subject = line['subject']
        bottomPercentChangeList.append(subject)
        topPercentChangeList.append(subject)
        del line['subject']
        listSorted = sorted(line.items(), key=lambda t: float(t[1]))

        for keyPair in listSorted[0:numberOfDays]:
            bottomPercentChangeList.append(keyPair)

        for keyPair in listSorted[38:len(listSorted) - (numberOfDays + 1):-1]:
            topPercentChangeList.append(keyPair)

    return bottomPercentChangeList, topPercentChangeList



