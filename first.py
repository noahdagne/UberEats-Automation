#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint
from faker import Faker
import time 
import sys
import os

saved_url = None
def log(msg):
    print(msg) 

class DoorDash:

    
    
    def __init__(self):
        self.driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
        faker = Faker()
        self.first_name = faker.first_name_male()
        self.last_name = faker.last_name_male() 
        fakeEmail = self.first_name + self.last_name + '471937'
        self.email = fakeEmail + '@yahoo.com'
        self.phone = self.new_phone()
        self.password = "password"
            
    def close_browser(self):
        self.browser.close()  
    def new_phone(self):
        driver = self.driver

        driver.set_page_load_timeout(30)
        log("About to get your new finessed number")
        driver.get("https://freephonenum.com/us")
        containers = driver.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[1]/div")
        time.sleep(5)
        assert "Free Disposable Number" in driver.title
 
        phone_links = containers.find_elements_by_tag_name('a')
        phone_hrefs = [elem.get_attribute('href') for elem in phone_links] 
        constant = "https://freephonenum.com/us/receive-sms/"
        phone_numbers = [elem[len(constant):] for elem in phone_hrefs]
        #print(phone_numbers)
       # log(phone_numbers[0])  
        file_numbers = open("number_use.txt","r")
        lines = file_numbers.readlines()
        last_line = lines[-1]
        last_line_int = int(last_line)
        #ADD + 1 BELOW ####################
        to_update = last_line_int + 1
        log("Failed: " + last_line)
        current_number = phone_numbers[last_line_int]
        #print("last line is "+ last_line)
        #print("phone number in array is: ")
        #print(phone_numbers[last_line_int])
        to_update = last_line_int + 1
        to_update_str = str(to_update)
        file_update = open("number_use.txt", "w")
        file_update.write(to_update_str + "\n")
        log("UPDATED NUMBER")

        #Save new URL for future verification
        saved_url = constant + str(current_number)
        log("Saved url: " + saved_url)
        self.saved_url_pass = saved_url
        return current_number

    def sign_up(self):
        driver = self.driver
        log("Your new name is " + self.first_name + " " + self.last_name)

        driver.set_page_load_timeout(30)
        driver.get("https://www.doordash.com/")
        assert "DoorDash" in driver.title
        log("This shit has begun...")
        time.sleep(5)
        signup_button = driver.find_element_by_xpath("//a[@href='/consumer/signup/']")
        signup_button.click()
        time.sleep(5)
        assert "Restaurant Delivery" in driver.title
        log("On the sign up page") 

        first_name_input = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/span/div/div/div/div[2]/form/label[1]/input")
        first_name_input.clear()
        first_name_input.send_keys(self.first_name)
        #time.sleep(.25)

        last_name_input = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/span/div/div/div/div[2]/form/label[2]/input")
        last_name_input.clear()
        last_name_input.send_keys(self.last_name)
        #time.sleep(.25)

        email_input = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/span/div/div/div/div[2]/form/label[3]/input")
        email_input.clear()
        email_input.send_keys(self.email)
        #time.sleep(.25)

        phone_input = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/span/div/div/div/div[2]/form/label[4]/input")
        phone_input.clear()
        phone_input.send_keys(self.phone)
        #time.sleep(.25)

        password_input = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/span/div/div/div/div[2]/form/span/div/label/div[3]/input")
        password_input.clear()
        password_input.send_keys(self.password)
        #time.sleep(.25)
        log("Finished filling in all yo stuff")
        """registered = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/span/div/div/div/div[2]/form/button")
        registered.click()"""
        #time.sleep(9)
        
        main_window = driver.current_window_handle

        #VERIFY NUMBER
        pass_url = self.saved_url_pass
        
        log("For new tab " + pass_url)
        driver.execute_script("window.open('');")
        driver.get(pass_url)
        time.sleep(5)

        #CURRENTLY IN NEW TAB TO VERIFY TEXT
        try:
            verification_box = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/text()")
            verification_aux = verification_box.text
            verification_code = verification_aux[:4]
            log(verification_box.text)
        except:
            log("Verification code not found")

        log("About to verify the text code...")

        driver.switch_to.window([-1])


        









os.system('clear')
first = DoorDash()
first.sign_up()







