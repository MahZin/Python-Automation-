# filenames, filepaths

# basic file recognition
'c:\\spam\\eggs.png'
# 'c:\\spam\\eggs.png'
print('\\')
# \
r'c\spam\eggs.png'
# 'c\\spam\\eggs.png'
print(r'c:\spam\eggs.png')
# c:\spam\eggs.png

# Combining folders
'\\'.join(['folder1', 'folder2', 'folder3', 'file.png'])
# 'folder1\\folder2\\folder3\\file.png'
import os
os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# 'folder1\\folder2\\folder3\\file.png'
os.sep
# '\\'

# To return current working directory
os.getcwd() 
# 'C:\\Users\\Mason\\AppData\\Local\\Programs\\Python\\Python37'

# To change working directory
os.chdir('c:\\') 
os.getcwd()
# 'c:\\'

# Absolute and relative file paths
'c:\\folder1\\\folder2\\spam.png' # absolute
'folder1\\\folder2\\spam.png' # relative

# . and .. folders
# ..\ refers to relative path of C:\
# .\ is optional. Refers to relative path

os.chdir('C:\\Users\\Mason\\AppData\\Local\\Programs\\Python\\Python37')

# Returns an absolute path form of the path passed to it
os.path.abspath('spam.png')
# 'C:\\Users\\Mason\\AppData\\Local\\Programs\\Python\\Python37\\spam.png'
os.path.abspath('..\\..\\spam.png')
# 'C:\\Users\\Mason\\AppData\\Local\\Programs\\spam.png'

# To check if path is absolute
os.path.isabs('..\\..\\spam.png')
# False
os.path.isabs('c:\\folder\\folder')
# True

# Returns the relative path b/w two paths passed to it
os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
# 'folder2\\spam.png'

# pull out directories
os.path.dirname('c:\\folder1\\folder2\\spam.png') 
# 'c:\\folder1\\folder2'

# pull out last part after last \\
os.path.basename('c:\\folder1\\folder2\\spam.png')
# 'spam.png'

# to check if a file is on your hard drive
os.path.dirname('c:\\folder1\\folder2\\spam.png')
# False
os.path.exists('c:\\windows\\system32\\calc.exe')
# True
os.path.isfile('c:\\windows\\system32\\calc.exe')
# True
os.path.isfile('c:\\windows\\system32')
# False # because this is just a folder
os.path.isdir('c:\\windows\\system32\\calc.exe')
# False # testing for if a file path is for a directory or a folder
os.path.isdir('c:\\windows\\system32')
# True

# To get size of file in bytes
os.path.getsize('c:\\windows\\system32\\calc.exe')
27648

# function to return total size of all folders specified
totalSize = 0
for filename in os.listdir('c:\\automatebook'):
    if os.path.isfile(os.path.join('c:\\automatebook', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\automatebook', filename)):
totalSize

# to make a file in hard drive
os.makedirs('c:\\delicious\\walnut\\waffles')
