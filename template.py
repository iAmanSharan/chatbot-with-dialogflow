import os 
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO , format = "[%(asctime)s] : %(message)s:")

project_name = 'textSummarizer'
list_of_files =  [
  ".github/workflows/.gitkeep",
  f"scr/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/utils/__init__.py",
  f"src/{project_name}/utils/common.py",
  f"src/{project_name}/logging/__init__.py",
  f"src/{project_name}/config/configuration.py",
  f"src/{project_name}/pipeline/__init__.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/constants/__init__.py",
  "DockerFile",
  "setup.py",
  "requirements.txt",
  "app.py",
  "main.py",
  "research/trails.ipynb",
  "params.yaml",
  "config/config.yaml"

]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir , filename = os.path.split(filepath)

  if filedir !="":
    os.makedirs(filedir , exist_ok = True)
    logging.info(f"{filedir} created  for {filename}")

  if (not os.path.exists(filedir)) or (os.path.getsize == 0):
    with open(filepath ,"w") as f:
      pass
      logging.info(f"Creating empty file for {filepath}")

  else : 
    logging.info("file already exists ")