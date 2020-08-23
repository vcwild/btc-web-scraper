from routes import Routes
from os import path, makedirs
from json import dump
from crawlers import (
  get_ted_transcript, 
  get_olhardigital_article,
  get_startse_article
)


# Crawler objects
ted = Routes.ted
od = Routes.olhar_digital
ss = Routes.startse

# Routines

## Create dir
new_path: str = "./documents"

if not path.exists(new_path):
  makedirs(new_path)

## Crawler workers
for url in ted:
  data = get_ted_transcript(url)
  index = ted.index(url)
  name = str(f'ted_{index}')

  with open(f'./documents/{name}.json', 'w') as file:
    dump(data, file, ensure_ascii=False)

for url in od:
  data = get_olhardigital_article(url)
  index = od.index(url)
  name = str(f'odt_{index}')

  with open(f'./documents/{name}.json', 'w') as file:
    dump(data, file, ensure_ascii=False)

for url in ss:
  data = get_startse_article(url)
  index = ss.index(url)
  name = str(f'startse_{index}')

  with open(f'./documents/{name}.json', 'w') as file:
    dump(data, file, ensure_ascii=False)
