from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

def wait(opening_time=3):
    time.sleep(opening_time)

def whatsapp_login():
    driver.get('https://web.whatsapp.com/')
    wait(10)

def send_message(text):
    web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
    web_obj.send_keys(text)
    web_obj.send_keys(Keys.RETURN)

def main():
    whatsapp_login()
    wait(5)
    for i in range(1, 1000):
        send_message("Hey bro?? Phone hi nhi kiya tune!!")
        wait(1)
        print('Message sent: ' + str(i))
    wait(2)
    print('Message sent successfully')
    driver.quit()

if __name__ == '__main__':
    main()
