__author__ = 'perfectblack999'
from flask import Flask, render_template, request, jsonify, url_for
from time import strftime
import json
import sys
import jsonConversion
sys.path.insert(0, '/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects')
import TopicAnalysis
app = Flask(__name__)

@app.route('/tweethandleinfo', methods=['POST', 'GET'])
def tweetHandleInfo():
    if request.method == 'POST':
        # return jsonify(filter=request.form['filter'], num_of_tweets=request.form['num_of_tweets'],
        #                rank_criteria=request.form['rank_criteria'], begin_date_range=request.form['begin_date_range'],
        #                end_date_range=request.form['end_date_range'])

        # jsonData = json.dump(result=TopicAnalysis.analyzeAPeriod(request.form['filter'], request.form['num_of_tweets'],
        #                                                    request.form['rank_criteria'], request.form['shelf'],
        #                                                     request.form['begin_date_range'], request.form['end_date_range']))

        fileName = "practice_" + request.form['filter'] + "_" + request.form['rank_criteria'] + "_" + request.form['shelf'] + "_" + strftime("%Y%m%d%H%M%S") + ".txt"
        with open(fileName, 'wb') as outfile:
            json.dump(TopicAnalysis.analyzeAPeriod(request.form['filter'], request.form['num_of_tweets'],
                                                           request.form['rank_criteria'], request.form['shelf'],
                                                            request.form['begin_date_range'], request.form['end_date_range']), outfile)
        outfile.close()

        jsonConversion.main(fileName)


        # return jsonify(result=TopicAnalysis.analyzeAPeriod(request.form['filter'], request.form['num_of_tweets'],
        #                                                    request.form['rank_criteria'], request.form['shelf'],
        #                                                     request.form['begin_date_range'], request.form['end_date_range']))

    return render_template('template.html')

@app.route('/static/Chart.js')
@app.route('/tweetstats')
def tweetStats():
    tweetStatsFileName, dates, subjectsAndSentiments, subjects = TopicAnalysis.main("tweetStats")
    subjects.insert(0,"-")
    return render_template('tweetstats.html', dates=dates[0:4], subjectsAndSentiments=subjectsAndSentiments[0:4], subjects=subjects)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
