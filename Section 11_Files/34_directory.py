# Directory tree

# Finding all files in the folder: c:\\delicious
import os
for folderName, subfolders, filenames in os.walk('c:\\delicious'):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()

# The folder is c:\delicious
# The subfolders in c:\delicious are: ['walnut']
# The filenames in c:\delicious are: ['delicious.txt', 'spam.txt', 'spamspamspam.txt']

# The folder is c:\delicious\walnut
# The subfolders in c:\delicious\walnut are: ['waffle']
# The filenames in c:\delicious\walnut are: ['eggs.txt']

# The folder is c:\delicious\walnut\waffle
# The subfolders in c:\delicious\walnut\waffle are: []
# The filenames in c:\delicious\walnut\waffle are: ['bacon.txt']


# To delete certain parts of a folder: 
for folderName, subfolders, filenames in os.walk('c:\\delicious'):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()

	for subfolder in subfolders:
            if 'fish' in subfolder:
                #os.rmdir(subfolder)
                print('rmdir on' + subfolder) # for dry-run

        for file in filenames:
            if file.endswith('.py'):
                # shutil.copy(os.join(foldername, file), os.join(folderName, file + '.backup'))
