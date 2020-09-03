# from selenium import webdriver
# import time

# driver=webdriver.Chrome()
# driver.get("https://www.gmail.com/")
# def login():#username,password
#     # driver.find_element
#     driver.find_element_by_id("identifierId").send_keys("surenderpal134@gmail.com")
#     driver.find_element_by_xpath("//span[@jsname='V67aGc']").click()
#     pass


# login()
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
class Google:

 def __init__(self):
  self.driver=webdriver.Chrome()
  self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
  sleep(3)
  self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
  self.driver.find_element_by_xpath('//input[@type="email"]').send_keys('surenderpal134@gmail.com')
  self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
  sleep(3)
  self.driver.find_element_by_xpath('//input[@type="password"]').send_keys('SUR@2000')
  self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
  sleep(2)
  self.driver.get('https://drive.google.com/drive/folders/1GdsRlvo2T-DUzP-RDtBYRkAyhSZi2jPH')
  sleep(5)
  self.driver.find_element_by_xpath("//button[@guidedhelpid='new_menu_button']").click()
  fileupload=self.driver.find_element_by_xpath("//div[contains(text(),'File upload')]")
  actions=ActionChains(self.driver)
  sleep(2)
  actions.move_to_element(fileupload).click().perform().send_keys('/Users/surenderpal/Downloads/sukhoi.jpg')

mylike= Google()