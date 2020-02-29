import sqlite3

#this creates db and table
conn = sqlite3.connect('textfiles.db')

with conn:
   cur = conn.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS tbl_filenames( \
      ID INTEGER PRIMARY KEY AUTOINCREMENT, \
      col_name TEXT)")
   conn.commit()
conn.close()

import os
#this looks at the files on my pc
location = 'C:/repository/PYTHON_Projects/Python_drills'

conn = sqlite3.connect('textfiles.db')
#looks for txt files, adds file names to db, prints only file names
for file in os.listdir(location):
    if file.endswith(".txt"):
       conn = sqlite3.connect('textfiles.db')
       with conn:
         cur = conn.cursor()
         cur.execute("INSERT INTO tbl_filenames(col_name) values(?)", \
                     (file,))
         conn.commit()
       conn.close()
       print(file)
    

