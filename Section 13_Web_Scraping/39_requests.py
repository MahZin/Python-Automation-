# requests

import requests

res = requests.get('insert URL here')
res.status_code # to check if request succeeded
len(res.text)
print(res.text[:500]) # first 500 characters

# If download failed, raise an exception
res.raise_for_status()
badRes = requests.get('http://automatetheboringstuff.com/skdksd')
badRes.raise_for_status()
# will raise error message

playFile = open('RomeoAndJuliet.txt', 'wb') # wb = write in binary mode
for chunk in res.iter_content(100000): # returns chunks of content for each iteration
    playFile.write(chunk)
# 100000
# 72493
playFile.close()
