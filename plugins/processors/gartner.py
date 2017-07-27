from plugins.outputs.ca_apm_rest import metricBatch
import logging

logger = logging.getLogger('parsible')

def process_line(line):
    if 'step-name' in line:
        logger.debug(line)

        line['step-number']=line['step-number'].zfill(2)
    
        metricBasePath = 'LogMetrics|%(file)s|%(step-number)s-%(step-name)s:Average Response Time(ms)' % line
    
        mb = metricBatch() 

        mb.addMetric('IntCounter', metricBasePath ,line['time'])
        mb.addMetric('StringEvent', "LogMetrics|running:running","running")
        mb.sendMetrics()
