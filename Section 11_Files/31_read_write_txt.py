# Plaintext files

# open() returns a file object you can read and write on
helloFile = open('c:\\users\\Mason\\hello.txt')
helloFile.read()
# 'Hello world!\nHow are you?'
helloFile.close()

helloFile = open('c:\\users\\Mason\\hello.txt')
content = helloFile.read()
print(content)
# Hello world!
# How are you?

helloFile = open('c:\\users\\Mason\\hello.txt')
helloFile.readlines()
# ['Hello world!\n', 'How are you?']
helloFile.close()

# To open in write mode ('r' = nothing) ('a' = append mode)
helloFile = open('c:\\users\\Mason\\hello.txt', 'w')
helloFile.write('Hello!!!!!!!')
# 12 # bytes
helloFile.write('Hello!!!!!!!')
# 12
helloFile.write('Hello!!!!!!!')
# 12
helloFile.close()

# Editing a file called 'Bacon'
baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable')
# 24
baconFile.close()
import os
os.getcwd()
# 'C:\\Users\\Mason\\AppData\\Local\\Programs\\Python\\Python37'
print(os.getcwd())
# C:\Users\Mason\AppData\Local\Programs\Python\Python37
baconFile = open('bacon.txt', 'a') # append mode
baconFile = write('\n\nBacon is delicious.')
baconFile.write('\n\nBacon is delicious.')
# 21
baconFile.close()

# Shelve module can store Python values in a binary file
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()
shelfFile = shelve.open('mydata')
shelfFile['cats']
# ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

# shelve.open returns a dictionary-like shelf value
shelfFile = shelve.open('mydata')
shelfFile.keys()
# KeysView(<shelve.DbfilenameShelf object at 0x000001763663C7B8>)
list(shelfFile.keys())
# ['cats']
list(shelfFile.values())
# [['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']]
