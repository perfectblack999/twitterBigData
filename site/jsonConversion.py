__author__ = 'perfectblack999'
import json

def main(fileName):
    file = open(fileName)
    rawJson = json.load(file)
    fileName = fileName.replace(".txt", "")
    print fileName
    outputFile = open(fileName + "_output.txt", "wb")
    outputFileList = []
    print rawJson
    print rawJson['shelf']
    outputFileList.append("Sentiment Range: " + rawJson['shelf'])
    for i in range(0,25):
        print i
        if rawJson.get(str(i)):
            print rawJson[str(i)]['tweet']
            outputFileList.append("Tweet: " + rawJson[str(i)]['tweet'].encode('utf-8'))
            print rawJson[str(i)]['handles']
            outputFileList.append("Handles: " + str(rawJson[str(i)]['handles']).encode('utf-8'))
            outputFileList.append("\n")
            for handle in rawJson[str(i)]['handles']:
                print handle
                handle = str(handle).encode('utf-8')
                outputFileList.append("Handle: " + handle)
                for entry in rawJson[str(i)][handle]:
                    print entry['Title']
                    print entry['Description']
                    print entry['Url']
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