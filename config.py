# this reads in configurations 
# the main one right now is YAML, though others could be supported
# the target of this routine is to produce a dict (see sample.py)

import yaml

def read_yaml(file):
    stream = open(file, "r")
    config = yaml.load(stream)
    # if there's something there return it
    if config:
        return config
    else: 
        error("not a valid configuraiton in file " + file)
              
              