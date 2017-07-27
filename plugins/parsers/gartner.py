import re
import logging

logger = logging.getLogger('parsible')

def parse_parser(line):
    result_set = {}
    cs = line.split(";")
    for pair in cs:
        the_pair = pair.split("=")
        if len(the_pair) == 2:
          result_set[the_pair[0].strip()] = the_pair[1]
    return result_set
   

def getValue(pair): 
   nv = pair.split("=")
   if len(nv) == 2:
        return nv[1]
   else:
       logger.debug(pair)
  
