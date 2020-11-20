# Selenium
from selenium import webdriver
broswer = webbrowser.Firefox()
browser.get('http://automatetheboringstuff.com')
elem browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child()')
                                          
elem
elem.click()
elems = browser.find_elements_by_css_selector('p')
lens(elems)
searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
