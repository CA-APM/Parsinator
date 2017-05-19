import requests
import json
import logging
import sys

logger = logging.getLogger('parsible')
# configure URL and header for RESTful submission
#url = "http://{0}:{1}/apm/metricFeed".format(options.hostname, options.port)
url = "http://localhost:8083/apm/metricFeed"
headers = {'content-type': 'application/json'}

class metricBatch(object):

    def __init__(self):
        self.metricDict = {'metrics' : []}
        logging.getLogger("requests").setLevel(logging.WARNING)

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
    def sendMetrics(self):
        try:
            logger.debug(json.dumps(self.metricDict, sort_keys=True, indent=4, separators=(',', ': ')))
            r = requests.post(url, data = json.dumps(self.metricDict),
                              headers = headers)
        except requests.ConnectionError as err:
            logger.error("Unable to connect to EPAgent via URL %s : %s\ncheck httpServerPort and that EPAgent is running!"%(url, err))
            sys.exit(1)

        if logging.getLogger('parsible').isEnabledFor(logging.DEBUG):

            logger.debug("Response:")
            response = json.loads(r.text)
            logger.debug(json.dumps(response, indent = 4))

            logger.debug("StatusCode: {0}".format(r.status_code))

