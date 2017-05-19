import requests
import json
import logging

logger = logging.getLogger('parsible')
# configure URL and header for RESTful submission
#url = "http://{0}:{1}/apm/metricFeed".format(options.hostname, options.port)
url = "http://localhost:8083/apm/metricFeed"
headers = {'content-type': 'application/json'}

class metricBatch(object):

    def __init__(self):
        self.metricDict = {'metrics' : []}

    # add a metric to the dictionary
    # param metricDict: container for sending metrics to EPAgent
    # param metricType: metric data type, e.g. IntCounter, StringEvent, https://communities.ca.com/docs/DOC-231154867
    # param metricName: the full metric name
    # param metricValue: the metric value
    def addMetric(self, metricType, metricName, metricValue):
        m = {}
        m['type'] = metricType
        m['name'] = metricName
        m['value']= "%s" % metricValue
        self.metricDict['metrics'].append(m)

     # json package.  Post resulting message to EPAgent RESTful
     # interface.
    def sendMetrics(self, verbose):
        try:
            logger.debug(json.dumps(self.metricDict, sort_keys=True, indent=4, separators=(',', ': ')))
            r = requests.post(url, data = json.dumps(self.metricDict),
                              headers = headers)
        except requests.ConnectionError as err:
            print("Unable to connect to EPAgent via URL \"{}\": {}\ncheck httpServerPort and that EPAgent is running!".format(url, err))
            sys.exit(1)

        if verbose == True:
            #print("jsonDump:")
            #print(json.dumps(metricDict, indent = 4))

            print("Response:")
            response = json.loads(r.text)
            print(json.dumps(response, indent = 4))

            print("StatusCode: {0}".format(r.status_code))

