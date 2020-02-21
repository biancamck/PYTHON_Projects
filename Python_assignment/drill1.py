
import os
import time

location = 'C:/repository/PYTHON_Projects/Python_assignment'

for file in os.listdir(location):
    if file.endswith(".txt"):
       modtime = os.path.getmtime(file)
       modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modtime))
       joinfile = os.path.join(location, file)
       print(file, "Last Modified Time : ", modificationTime)
