import os

ls = os.listdir()
for l in ls:
  if os.path.isfile(l):
    lsize = os.path.getsize(l)
    print(f"{l} is a file: size {lsize}")
  elif os.path.isdir(l):
    print(f"{l} is a directory")