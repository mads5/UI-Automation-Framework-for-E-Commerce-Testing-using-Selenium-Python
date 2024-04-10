import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import base_url
from utils import generate_random_email, wait_for_element_visible

class Login(object):
    def closeAllChromeInstances():
        try:
            os.system("taskkill /im chromedriver.exe")
            os.system("taskkill /im chrome.exe")
        except:
            pass
            
    def launchWebsite():
    
        global driver
        
        driver = webdriver.Chrome(r"/chromedriver.exe")
        browser.maximize_window()
        browser.get('https://practice.automationtesting.in/')
        
    def createAccount():
    
        driver.find_element(By.ID('menu-item-50'))
        driver.click()
        elmnt = WebdriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reg_email"]')))
        elmnt.click()
        elmnt.send_keys('demo@dmail.com')
        elmnt.send_keys(Keys.TAB)
        elmnt.send_keys('Gmail@007')
        elmnt.send_keys(Keys.RETURN)
        
        driver.implicitly_wait(2)
        
        if elmnt = driver.find_element(By.XPATH('//*[text()=(" An account is already registered with your email address. Please login.")]')):
            logger.info('Account exists')
        elif elmnt = driver.find_element(By.ID('//*[@href="https://practice.automationtesting.in/my-account/customer-logout/"])[1]')):
            logger.info('User logged in')
            assert driver.current_url == "https://practice.automationtesting.in/my-account/"

            
    def Login():
    
        driver.find_element(By.ID('username'))
        driver.click()
        elmnt.send_keys('demo@dmail.com')
        elmnt.send_keys(Keys.TAB)
        elmnt.send_keys('Gmail@007')
        elmnt.send_keys(Keys.RETURN)
        
        driver.implicitly_wait(2)
        
        if elmnt = driver.find_element(By.XPATH('//*[text()=(" A user could not be found with this email address.")]')):
            logger.info("User does not exists!")
        elif elmnt = driver.find_element(By.ID('//*[@href="https://practice.automationtesting.in/my-account/customer-logout/"])[1]')):
            logger.info('User logged in')
            assert driver.current_url == "https://practice.automationtesting.in/my-account/"

        
    
    def Shop():
        
        driver.find_element(By.XPATH('//*[@href="https://practice.automationtesting.in/shop/"]'))
        driver.click()
        driver.find_element(By.XPATH('//*[@id="content"]/ul/li[1]/a[2]'))
        driver.click()
        driver.find_element(By.XPATH('//*[@title="View your shopping cart"]'))
        driver.click()
        
        elmnt = WebdriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[3]')))
        
        if elmnt = True:
            driver.find_element(By.XPATH('//*[@title="Remove this item"]'))
            driver.click()
            driver.implicitly_wait(1)
            result = driver.find_element(By.XPATH('//*[text()="Android Quick Start Guide removed. "]'))
            if result = True:
                assert True
            else:
                assert False
        else:
            logger.info("Unable to find the Shopping Cart!")
            
    
    
    def Address():
        
        driver.find_element(By.ID('menu-item-50'))
        driver.click()
        driver.find_element(By.XPATH('//*[@href="https://practice.automationtesting.in/my-account/edit-address/"]'))
        driver.click()
        driver.find_element(By.XPATH('(//*[contains(text(),'Edit')])[2]'))
        driver.click()
        driver.implicitly_wait(2)
        
        driver.find_element(By.XPATH('//*[@name="shipping_first_name"]'))
        driver.send_keys("Veer")
        driver.find_element(By.XPATH('//*[@name="shipping_last_name"]'))
        driver.send_keys("Kalantri")
        driver.find_element(By.XPATH('//*[@name="shipping_company"]'))
        a = Centime
        driver.send_keys(a)
        driver.find_element(By.XPATH('//*[@name="shipping_address_1"]'))
        driver.send_keys("Badnera Road")
        driver.find_element(By.XPATH('//*[@name="shipping_city"]'))
        driver.send_keys("Amravati")
        driver.find_element(By.XPATH('//*[@name="shipping_postcode"]'))
        driver.send_keys("444605")
        dropdown = Select(driver.find_element(By.ID('select2-chosen-1'))
        dropdown.select_by_visible_text('India')
        dropdown = Select(driver.find_element(By.ID('select2-chosen-2'))
        dropdown.select_by_visible_text('Maharashtra')
        
        driver.find_element(By.XPATH('//*[@class="button"]'))
        driver.click()
        
        elmnt = WebdriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Address changed successfully.']")))
        driver.find_element(By.XPATH('//*[@href="https://practice.automationtesting.in/my-account/edit-address/"]'))
        driver.click()
        elmnt = driver.find_element(By.XPATH('//*[contains(text(),'Centime')]'))
        
    
if __name__ == "__main__":
    
    result = closeAllChromeInstances()
    result = launchWebsite()
    result = createAccount()
    result = Login()
    result = Shop()
    result = Address()
    
    