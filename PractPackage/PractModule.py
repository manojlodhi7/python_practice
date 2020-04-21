'''
Created on Nov 12, 2019

@author: mlodhi
'''

from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path=r'C:\Practice_Python_Projects\geckodriver.exe')
driver.get("http://www.google.com")
print(driver.title)
print("Google" in driver.title)
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("testproject.io")
elem.send_keys(Keys.RETURN)
driver.close()