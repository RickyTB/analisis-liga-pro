import json

def load_json(dir):
  with open(dir, encoding='utf8') as d:
    dictData = json.load(d)
    return dictData