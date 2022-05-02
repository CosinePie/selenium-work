from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# PATH = r"C:\Program Files (x86)\geckodriver.exe"

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# driver = webdriver.Firefox()
# driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')
driver.get("https://translate.google.co.in/?sl=en&tl=es&op=translate")

search = driver.find_element_by_class_name("er8xn")
search.send_keys("selenium plugin")
search.send_keys(Keys.RETURN)
time.sleep(3)

# link = driver.find_element_by_link_text("TRANSLATE")
# link.clear()
# link.click


# time.sleep(5)
driver.quit()