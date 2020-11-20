# The results are the new location of the moved file/folder

import shutil

# copying a file into a folder
shutil.copy('c:\\spam.txt', 'c:\\delicious')
# 'c:\\delicious\\spam.txt'

# copying a file and renaming it to a new location
shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')
# 'c:\\delicious\\spamspamspam.txt'

# copying a folder and all of its content, then renaming it 
shutil.copytree('c:\\delicious', 'c:\\delicious_backup')
# 'c:\\delicious_backup'

# moving a file into a folder
shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut')
# 'c:\\delicious\\walnut\\spam.txt'

# to move and rename:
shutil.move('c:\\delicious\\walnut\\spam.txt', 'c:\\delicious\\walnut\\eggs.txt')
# I moved it to the same location, but with a different name
