from bs4 import BeautifulSoup
import requests
from re import sub


def get_ted_transcript(url=None):
  """
  Crawl into TED talks and scrap title, body, author and link
  
  Parameters
  -----------
  url: str
    Target url for scrapping
  """

  if "ted" not in str(url):
    raise Exception("URL not in TED")

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')
  transcript = soup("div", {"class":"Grid Grid--with-gutter d:f@md p-b:4"})
  
  texts = []
  for div in transcript:
    text = div("p")[0].text
    text = text.strip()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace('"', "")
    text = text.replace("\\", '')
    text = sub(" +", " ", text)
    texts.append(text)

  header = soup.title.text
  author = header.split(":")[0].strip()
  title = header.split(":")[1].split("|")[0].strip()

  return {
    "author": author,
    "body": " ".join(texts),
    "title": title,
    "type": "video",
    "url": url
  }


def get_olhardigital_article(url=None):
  """
  Crawl into Olhar Digital and scrap title, body, author and link
  
  Parameters
  -----------
  url: str
    Target url for scrapping
  """

  if "olhardigital" not in str(url):
    raise Exception("URL not in OLHAR DIGITAL")

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')
  transcript = soup("article", {"class":"mat-container"})[0]("div", {"class":"mat-txt"})
  texts = []

  for div in transcript:
    paragraphs = div("p")
    for p in paragraphs:
      text = p.text
      text = text.strip()
      text = text.replace("\n", " ")
      text = text.replace("\t", " ")
      text = text.replace("\\", '')
      text = sub(' +', ' ', text)
      texts.append(text)
  
  try:
    author = soup("h1", {"class":"cln-nom"})[0].text
  except IndexError:
    author = soup("span",{"class":"meta-item meta-aut"})[0].text
    if "," in author:
      author = author.split(",")[0]
  except:
    raise Exception("Verifique o codigo")
    
  title = soup("h1", {"class":"mat-tit"})[0].text
  return {
    "author": author,
    "body": " ".join(texts),
    "title": title,
    "type": "article",
    "url": url
  }


def get_startse_article(url=None):
  """
  Crawl into Start SE and scrap title, body, author and link
  
  Parameters
  -----------
  url: str
    Target url for scrapping
  """

  if "startse" not in str(url):
    raise Exception("URL not in STARTSE")

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')
  transcript = soup("span", {"style":"font-weight: 400;"})
  texts = []
  for span in transcript:
    text = span.text
    text = text.strip()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("\\", '')
    text = sub(' +', ' ', text)
    texts.append(text)
  
  author = soup("div", {"class":"title-single__info"})[0]("h4")[0]("a")[0].text
  title = soup("div", {"class":"title-single__title"})[0]("h2")[0].text
  return {
    "author": author,
    "body": " ".join(texts),
    "title": title,
    "type": "article",
    "url": url
  }
