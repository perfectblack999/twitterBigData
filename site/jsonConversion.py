__author__ = 'perfectblack999'
import json

def main(fileName):
    tweetList = []
    file = open(fileName)
    rawJson = json.load(file)
    fileName = fileName.replace(".txt", "")
    outputFile = open(fileName + "_output.txt", "wb")
    outputFileList = []
    outputFileList.append("Sentiment Range: " + rawJson['shelf'])

    for i in range(0,25):
        if rawJson.get(str(i)):
            if rawJson[str(i)]['tweet'] not in tweetList:
                tweetList.append(rawJson[str(i)]['tweet'])
                outputFileList.append("Tweet: " + rawJson[str(i)]['tweet'].encode('utf-8'))
                outputFileList.append("Handles: " + str(rawJson[str(i)]['handles']).encode('utf-8'))
                outputFileList.append("\n")
                for handle in rawJson[str(i)]['handles']:
                    handle = str(handle).encode('utf-8')
                    outputFileList.append("Handle: " + handle)
                    for entry in rawJson[str(i)][handle]:
                        title = entry['Title'].encode('utf-8')
                        description = entry['Description'].encode('utf-8')
                        url = entry['Url'].encode('utf-8')
                        outputFileList.append("Title: " + title)
                        outputFileList.append("Description: " + description)
                        outputFileList.append("URL: " + url)
                        outputFileList.append("\n")
                    outputFileList.append("\n\n")

    for line in outputFileList:
        outputFile.write(line + "\n")

    outputFile.close()

if __name__ == "__main__":
   main("practice_dating app_rt_normalized_11To20_20151213233854.txt")