from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://groundtruth.greythr.com/")
time.sleep(2)

def GreyHr(): #username, password
    driver.find_element_by_id("username").send_keys("GTIND-078")
    driver.find_element_by_id("password").send_keys("Surenderpal@1991")
    driver.find_element_by_xpath("//button/h6[text()= 'Sign In']").click()
    time.sleep(5)

def Salslip():
    driver.find_element_by_partial_link_text("Salary").click()
    time.sleep(2)
    driver.find_element_by_partial_link_text("View Payslips").click()
    time.sleep(2)
    # driver.find_element_by_id("pdfButton").click()


def Leaves():
    driver.find_element_by_partial_link_text("Home").click()
    driver.find_element_by_partial_link_text("Leave").click()
    time.sleep(2)
    driver.find_element_by_partial_link_text("View Leave Summary").click()
    time.sleep(2)
    actions=ActionChains(driver)
    driver.find_element_by_xpath("//div[@id='myleave']//div[@class='controls']//input[contains(@class,'input-medium')]").send_keys("Leave")
    time.sleep(2)
    leaveopt=driver.find_element_by_xpath("//ul[@role='listbox']/li[1]/a")
    actions.move_to_element(leaveopt).click().perform()

def LeaveApplication():
    time.sleep(2)
    driver.find_element_by_xpath("")




def signOut():
    driver.find_element_by_link_text("Sign Out").click()

GreyHr()
Salslip()
Leaves()
