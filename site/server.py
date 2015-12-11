__author__ = 'perfectblack999'
from flask import Flask, render_template, request, jsonify, url_for
import sys
sys.path.insert(0, '/Users/perfectblack999/Documents/Developer/Nkem_Big_Data_Projects')
import TopicAnalysis
app = Flask(__name__)

@app.route('/tweethandleinfo', methods=['POST', 'GET'])
def tweetHandleInfo():
    if request.method == 'POST':
        # return jsonify(filter=request.form['filter'], num_of_tweets=request.form['num_of_tweets'],
        #                rank_criteria=request.form['rank_criteria'], begin_date_range=request.form['begin_date_range'],
        #                end_date_range=request.form['end_date_range'])

        return jsonify(result=TopicAnalysis.analyzeAPeriod(request.form['filter'], request.form['num_of_tweets'],
                                                           request.form['rank_criteria'], request.form['shelf'],
                                                            request.form['begin_date_range'], request.form['end_date_range']))

    return render_template('template.html')

@app.route('/static/Chart.js')
@app.route('/tweetstats')
def tweetStats():
    tweetStatsFileName, dates, subjectsAndSentiments, subjects = TopicAnalysis.main("tweetStats")
    subjects.insert(0,"-")
    return render_template('tweetstats.html', dates=dates, subjectsAndSentiments=subjectsAndSentiments[0:2], subjects=subjects)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
