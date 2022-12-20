from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

file = open("info.txt","r")

userName = file.readline()
password = file.readline()

file.close()

driver = webdriver.Chrome()
url = "https://github.com/login"
driver.get(url)
driver.maximize_window()

# get elements with locators

userInput = driver.find_element(By.ID,"login_field")
passwordInput = driver.find_element(By.ID,"password")
logBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]")

# action of Test

def incorrectLogin(userArg):
    actions0 = ActionChains(driver)
    actions0.send_keys_to_element(userInput,userArg)
    actions0.click(logBtn)
    actions0.perform()
    sleep(2)

    incorrectFlash = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[2]/div/div/div")
    message = incorrectFlash.text

    if "Incorrect username or password." in message:
        print("Test Başarılı ✔")
    else:
        print("Test başarısız ❌")


incorrectLogin("test")









