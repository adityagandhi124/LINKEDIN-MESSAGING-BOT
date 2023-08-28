from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
import time 


def login_LINKEDIN(driver): 
    url = 'https://www.linkedin.com'
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(3)

    #Sign in 
    # email = driver.find_element(By.ID, "session_key")
    # password = driver.find_element(By.ID, "session_password")

    email = driver.find_element(by = By.XPATH, value = "//input[@name = 'session_key']")
    password = driver.find_element(by = By.XPATH, value = "//input[@name = 'session_password']")

    with open(r"/Users/adityagandhi/Desktop/python projects/Username.txt") as myUser: 
        username = myUser.read().replace('\n', '') #this replaces any newline characters ('\n') in the file contents with an empty string
    email.send_keys(username)

    with open(r"/Users/adityagandhi/Desktop/python projects/Password.txt") as myPass: 
        passcode = myPass.read().replace('\n', '')
    password.send_keys(passcode)

    time.sleep(3)
    driver.find_element(by=By.XPATH, value = "//button[@type = 'submit']").click()
    time.sleep(3)

def message_AUTOMATION(driver): 
    url = 'https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&sid=B2M'
    driver.get(url)
    time.sleep(2) 

    all_buttons = driver.find_elements(By.TAG_NAME, "button") # you cannot access a span element, so we have to attack all of the button elements with the message of "message"
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    message_buttons[0].click()

    paragraphs = driver.find_elements(By.TAG_NAME, "p")

    for p, q in enumerate(paragraphs): 
        print(p)
        print(q.text)

    time.sleep(2)

def main(): 

    driver = webdriver.Chrome()
    login_LINKEDIN(driver)
    message_AUTOMATION(driver)


    print("Automation Complete")

main()
