import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

############# DATOS #############
mail = "joaquinhockeylagos@gmail.com" 
pw = "Qwer.1234" #Contraseña actual, Al menos 5 caracteres 
new_pw = "Qwer.1234" #Nueva contraseña 
name = "" 
lastname = "" 
birthday = "" # dd/mm/aaaa
#######################################


def login_everlast():
    driver.get("https://www.everlast.cl/")

    time.sleep(3)

    log_in_button = driver.find_element_by_id("header-user-btn")
    log_in_button.click()

    mail_field = driver.find_element_by_name("email")
    mail_field.send_keys(mail)

    pw_field = driver.find_element_by_name("password")
    pw_field.send_keys(pw)

    login_btn = driver.find_element_by_id("submit-login")
    login_btn.click()

    return


def signin_everlast():

    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://www.everlast.cl/")


    time.sleep(3)

    log_in_button = driver.find_element_by_id("header-user-btn")
    log_in_button.click()

    register_btn = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/div/div/div/div/a')
    register_btn.click()

    name_field = driver.find_element_by_name("firstname")
    name_field.send_keys(name)

    lastname_field = driver.find_element_by_name("lastname")
    lastname_field.send_keys(lastname)

    mail_field = driver.find_element_by_name("email")
    mail_field.send_keys(mail)

    pw_field = driver.find_element_by_name("password")
    pw_field.send_keys(pw)

    bd_field = driver.find_element_by_name("birthday")
    bd_field.send_keys(birthday)

    register_btn = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/section/form/footer/button')
    register_btn.click()

    return


def change_password_everlast():
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://www.everlast.cl/")

    time.sleep(3)

    log_in_button = driver.find_element_by_id("header-user-btn")
    log_in_button.click()

    mail_field = driver.find_element_by_name("email")
    mail_field.send_keys(mail)

    pw_field = driver.find_element_by_name("password")
    pw_field.send_keys(pw)

    login_btn = driver.find_element_by_id("submit-login")
    login_btn.click()

    account_btn = driver.find_element_by_id("identity-link")
    account_btn.click()

    current_pw_field = driver.find_element_by_name("password")
    current_pw_field.send_keys(pw)

    new_pw_field = driver.find_element_by_name("new_password")
    new_pw_field.send_keys(new_pw)

    account_btn = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/div/div[2]/form/footer/button')
    account_btn.click()

    return


def password_recovery():
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
    driver.get("https://www.everlast.cl/")

    time.sleep(3)

    log_in_button = driver.find_element_by_id("header-user-btn")
    log_in_button.click()

    pw_recovery_btn = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/div/section/form/section/div[3]/a')
    pw_recovery_btn.click()

    mail_btn = driver.find_element_by_id("email")
    mail_btn.send_keys(mail)

    btn = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/section/form/button')
    btn.click()

    #Se envía enlace de recuperación al mail   
    return

#signin_everlast()
#login_everlast()
#password_recovery()
#change_password_everlast()




