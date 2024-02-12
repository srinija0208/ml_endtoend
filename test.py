import os

path="notebooks/research.ipynb"

# print(os.path.split(path))
## creating dir and file

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(file,"w") as f:
    pass