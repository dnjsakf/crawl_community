import os
import codecs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = os.path.join( os.path.dirname(os.path.abspath(__file__)), '../drivers/chromedriver_78' )
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument( "--headless" )
chrome_options.add_argument( f"--window-size={ WINDOW_SIZE }" )

driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
driver.get("https://www.google.com")
# driver.get_screenshot_as_file("capture.png")

print( driver )

with codecs.open('google.html', 'w', encoding='utf-8') as w:
    w.write( driver.page_source )

driver.close()