

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://automationpractice.com/index.php')

FirstSearch = "Lets go to places where we have never been before"
first = web.find_element_by_xpath('//*[@id="search_query_top"]')
first.send_keys(FirstSearch)

Submit = web.find_element_by_xpath('//*[@id="searchbox"]/button')
Submit.click()

img = web.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div/[1]/div/a[1]/img')
img.click()
