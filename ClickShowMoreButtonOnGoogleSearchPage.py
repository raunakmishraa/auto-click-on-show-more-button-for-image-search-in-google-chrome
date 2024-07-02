from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(r'C:\Users\DELL\chromedriver\chromedriver.exe')
driver.get('https://images.google.com/?gws_rd=ssl')

box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box.send_keys("giraffe")
box.send_keys(Keys.ENTER)
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[2]/div[2]/input').click()
        except:
            print("The show more button is not available now. You've reached to the end of the page.")
            break
    last_height = new_height
