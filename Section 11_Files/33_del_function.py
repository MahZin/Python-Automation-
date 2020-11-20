# make a function as a precaution
import os

os.chdir('C:\\Users\\Mason\\Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)
