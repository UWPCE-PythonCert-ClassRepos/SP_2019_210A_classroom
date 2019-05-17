from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Grabbing login credentials from my text file
def git_hub():
    with open(r"C:\Users\roviram\Documents\Amazon\BIE\GH_Cred.txt", "r") as in_cred_file:
        cred_list = []
        for line in in_cred_file:
            cred = line.strip()
            cred_list.append(cred)

    try:
        user = cred_list[0]
        pwd = cred_list[1]
        # This is when the firefox web browser starts up. You need to put in the executable path of the web driver: geckodriver (for firefox)
        browser = webdriver.Firefox(executable_path=r'C:\Users\roviram\Documents\geckodriver-v0.24.0-win64\geckodriver.exe')
        # The get method is taking us to the web address
        browser.get("https://github.com/login")

        # Multiple ways to find the element of the textbox where you need to fill out your forms.
        login = browser.find_element_by_id("login_field")
        my_pwd = browser.find_element_by_id("password")

        # Clearing login and password if text already exist
        login.clear()
        # Sending login and password info
        login.send_keys(user)
        my_pwd.clear()
        my_pwd.send_keys(pwd)
        browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[3]/input[4]").click()
        print("Login to Github successful!")

    except Exception as error:
        print("There is an error with your code, please check credentials, element path or the xpath")
        print("This is what Python's error was complaining about:", error)

if __name__ == '__main__':
    git_hub()

