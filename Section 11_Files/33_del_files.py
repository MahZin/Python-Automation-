import os

# check which file we are deleting
os.getcwd()
# 'C:\\Users\\Mason\\AppData\\Local\\Programs\\Python\\Python37'
os.rmdir('c:\\delicious')
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     os.rmdir('c:\\delicious')
# OSError: [WinError 145] The directory is not empty: 'c:\\delicious'
# to safeguard against removing important files

# to permanently remove files (will skip recycle bin!):
import shutil
shutil.rmtree('c:\\delicious') # remove tree

# to send files to recycle bin
import send2trash
send2trash.send2trash('c:\\users\\Mason\desktop\\dummyfile.txt')
