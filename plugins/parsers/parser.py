import re

debugOn = False

def parse_parser(line):
    result_set = {}
    start_index = line.find("process")
    sliced_line = line[start_index:]
    cs = sliced_line.split(",")
    if len(cs) == 10:
        result_set["process"] = getValue(cs[0])
        result_set["host"] = getValue(cs[1])
        result_set["port"] = getValue(cs[2])
        result_set["element_name"] = getValue(cs[3])
        result_set["HIGH"] = getValue(cs[4])
        result_set["LOW"] = getValue(cs[5])
        result_set["LAST"] = getValue(cs[6])
        result_set["ELAPSE"] = getValue(cs[7])
        result_set["soeTimestamp"] = getValue(cs[8])
        result_set["time_stamp"] = getValue(cs[9])
    else:
        debug (line)
    return result_set

def getValue(pair): 
   nv = pair.split("=")
   if len(nv) == 2:
        return nv[1]
   else:
       debug(pair)
  
def debug(message):
   if debugOn:
     print(message)
