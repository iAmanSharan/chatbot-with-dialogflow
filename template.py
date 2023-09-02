import os 
import logging
rom pathlib import Path

logging.basicConig(level = logging.INO , ormat = "[%(asctime)s] : %(message)s:")

project_name = 'textSummarizer'
list_o_iles =  [
  ".github/worklows/.gitkeep",
  "src/textSummarizer/__init__.py",
  "src/textSummarizer/components/__init__.py",
  "src/textSummarizer/utils/__init__.py",
  "src/textSummarizer/utils/common.py",
  "src/textSummarizer/logging/__init__.py",
  "src/textSummarizer/conig/coniguration.py",
  "src/textSummarizer/pipeline/__init__.py",
  "src/textSummarizer/entity/__init__.py",
  "src/textSummarizer/constants/__init__.py",
  "Dockerile",
  "setup.py",
  "requirements.txt",
  "app.py",
  "main.py",
  "research/trails.ipynb",
  "params.yaml",
  "conig/conig.yaml"

]

or ilepath in list_o_iles:
  ilepath = Path(ilepath)
  iledir , ilename = os.path.split(ilepath)

  i iledir !="":
    os.makedirs(iledir , exist_ok = True)
    logging.ino("{iledir} created  or {ilename}")

  i (not os.path.exists(iledir)) or (os.path.getsize == 0):
    with open(ilepath ,"w") as :
      pass
      logging.ino("Creating empty ile or {ilepath}")

  else : 
    logging.ino("ile already exists ")