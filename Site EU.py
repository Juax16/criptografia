import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

############### DATOS ################
mail = ""
pw = ""   #Minimo 9 caracteres
new_pw = ""
name = ""
lastname = ""
#######################################


def login_AH():
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://adrianahidalgo.es/")

    time.sleep(3)

    try:
        btn = driver.find_element_by_xpath('//*[@id="cn-accept-cookie"]')
        btn.click()
    finally:
        pass

    my_account_btn = driver.find_element_by_xpath('/html/body/header/div/div[3]/div/div[1]/ul/li[6]/a')
    my_account_btn.click()
    my_account_btn.click()

    mail_field = driver.find_element_by_xpath('//*[@id="username"]')
    mail_field.send_keys(mail)

    pw_field = driver.find_element_by_xpath('//*[@id="password"]')
    pw_field.send_keys(pw)

    time.sleep(1)

    login_btn = driver.find_element_by_xpath('/html/body/section/div/article/div/div/div/div[2]/div[1]/form/p[3]/button')
    login_btn.click()

    return

def signin_AH():
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://adrianahidalgo.es/")

    time.sleep(3)

    my_account_btn = driver.find_element_by_xpath('/html/body/header/div/div[3]/div/div[1]/ul/li[6]/a')
    my_account_btn.click()
    my_account_btn.click()

    mail_field = driver.find_element_by_xpath('//*[@id="reg_email"]')
    mail_field.send_keys(mail)

    pw_field = driver.find_element_by_xpath('//*[@id="reg_password"]')
    pw_field.send_keys(pw)

    time.sleep(1)

    try:
        btn = driver.find_element_by_xpath('//*[@id="cn-accept-cookie"]')
        btn.click()
    finally:
        pass

    time.sleep(1)

    register_btn = driver.find_element_by_xpath('/html/body/section/div/article/div/div/div/div[2]/div[2]/form/p[3]/button')
    register_btn.click()

    return

def change_password_AH():
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://adrianahidalgo.es/")

    time.sleep(3)

    try:
        btn = driver.find_element_by_xpath('//*[@id="cn-accept-cookie"]')
        btn.click()
    finally:
        pass

    my_account_btn = driver.find_element_by_xpath('/html/body/header/div/div[3]/div/div[1]/ul/li[6]/a')
    my_account_btn.click()
    my_account_btn.click()

    mail_field = driver.find_element_by_xpath('//*[@id="username"]')
    mail_field.send_keys(mail)

    pw_field = driver.find_element_by_xpath('//*[@id="password"]')
    pw_field.send_keys(pw)

    time.sleep(1)

    login_btn = driver.find_element_by_xpath('/html/body/section/div/article/div/div/div/div[2]/div[1]/form/p[3]/button')
    login_btn.click()

    account_details_btn = driver.find_element_by_xpath('/html/body/section/div/article/div/div/div/nav/ul/li[5]/a')
    account_details_btn.click()

    if driver.find_element_by_xpath('//*[@id="account_first_name"]').get_attribute('value') == '' or driver.find_element_by_xpath('//*[@id="account_last_name"]').get_attribute('value') == '':
        
        name_field = driver.find_element_by_xpath('//*[@id="account_first_name"]')
        name_field.send_keys(name)

        lastname_field = driver.find_element_by_xpath('//*[@id="account_last_name"]')
        lastname_field.send_keys(lastname)

    current_pw_field = driver.find_element_by_xpath('//*[@id="password_current"]')
    current_pw_field.send_keys(pw)

    new_pw_field = driver.find_element_by_xpath('//*[@id="password_1"]')
    new_pw_field.send_keys(new_pw)

    new_pw_field2 = driver.find_element_by_xpath('//*[@id="password_2"]')
    new_pw_field2.send_keys(new_pw)

    save_btn = driver.find_element_by_xpath('/html/body/section/div/article/div/div/div/div/form/p[5]/button')
    save_btn.click()

    return

def password_recovery_AH():
    #No terminado
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://adrianahidalgo.es/")

    time.sleep(3)

    try:
        btn = driver.find_element_by_xpath('//*[@id="cn-accept-cookie"]')
        btn.click()
    finally:
        pass

    my_account_btn = driver.find_element_by_xpath('/html/body/header/div/div[3]/div/div[1]/ul/li[6]/a')
    my_account_btn.click()
    my_account_btn.click()

    pw_recovery_btn = driver.find_element_by_xpath('/html/body/section/div/article/div/div/div/div[2]/div[1]/form/p[4]/a')
    pw_recovery_btn.click()

    #captcha
    return

#login_AH()
#signin_AH()
#change_password_AH()
#password_recovery_AH()#No funciona (CAPTCHA) 

