import requests

def readGist(apiLink):
  r = requests.get(apiLink)
  content = r.json()
  secondIndex = list(r.json()["files"].keys())[0]
  content = r.json()["files"][secondIndex]["content"]

  contentAsList = content.split(", ")
  return contentAsList