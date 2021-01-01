import os
import time

file_path = ".\images"
file_names = os.listdir(file_path)

i=1
tmp = "tmp"
for name in file_names:
    print(name)
    src = os.path.join(file_path, name)
    dst = tmp+str(i) + '.jpg'

    i += 1
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)


file_names = os.listdir(file_path)
i=1
for name in file_names:
    print(name)
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'

    i += 1
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)