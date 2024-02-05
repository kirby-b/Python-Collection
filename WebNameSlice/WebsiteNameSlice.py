import re

def main():
  website1 = ("https://google.com")
  website2 = ("https://w3schools.com")
  
  print("This program takes a sample website like this:")
  print(website1)
  print(website2)
  print("And turns them into this")
  print(extract_name(website1))
  print(extract_name(website2))

def extract_name(website):
  start = website.find("://", beg=0, end=len(website))
  end = ""
  dot_what = re.search("\..+.*" , website).span()
  end = dot_what[-1]
  s = slice(start, end)
  return website[s]
