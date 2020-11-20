# Beautiful Soup Function, parsing HTML's

import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('Insert Element') # right-click > inspect element > highlight elements > Copy selector
    # select() method returns list of matching Element objects
    return elems[0].text.strip()


price = getAmazonPrice('Insert URL')
print('The price is' + price)

# Doesn't work for all URLs
