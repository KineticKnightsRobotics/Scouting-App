
def extractData (filepath):
  with open(filepath, 'r') as doc:
    return "".join(doc.readlines()).split("\n")
