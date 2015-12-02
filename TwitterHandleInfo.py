__author__ = 'perfectblack999'
#!/usr/bin/python
import json
import urllib
import csv
import requests
from pybing.query import WebQuery
from py_bing_search import PyBingSearch
import BingSearch

def googleSearch(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  print results
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

def bingSearch(acctKey, searchQuery, searchLimit, resultsFormat):
  bing = PyBingSearch(acctKey)
  return bing.search(searchQuery, limit=searchLimit, format=resultsFormat)

# results, nextUri = bingSearch('fiI+4C9i7o/nsII7jd5pFNroxPMfrdFYfdJJ+ezMxeg=','nkem', 50, 'json')

handlesFile = open('topTweeters.csv', 'r')
handleReader = csv.reader(handlesFile)
handlesList = list(handleReader)

for handle in handlesList[0]:
  print "handle: " + handle
  results = BingSearch.bing_search(handle, 'Web')
  for result in results:
    print "Description: " + result['Description']
    print "Title: " + result['Title']
    print "URL: " + result['Url']