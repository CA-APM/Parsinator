from plugins.outputs.ca_apm_rest import metricBatch
import logging

logger = logging.getLogger('parsible')

def process_line(line):
    if 'process' in line:
    
        metricBasePath = 'LogMetrics|%(process)s|%(host)s|%(port)s|%(element_name)s' % line
    
        mb = metricBatch() 

        mb.addMetric('IntCounter', metricBasePath + ':LAST',line["LAST"])
        mb.addMetric('IntCounter', metricBasePath + ':LOW', line["LOW"])
        mb.addMetric('IntCounter', metricBasePath + ':HIGH',line["HIGH"])
        mb.addMetric('StringEvent', "LogMetrics|running:running","running")
        mb.sendMetrics()
