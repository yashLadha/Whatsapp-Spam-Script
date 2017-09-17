from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Launches chrome in a automated mode
# need to have chrome preinstalled in the system
driver = webdriver.Chrome(executable_path='./chromedriver')
thoughts = []


def random_thought():
    id = random.randint(0, len(thoughts)-1)
    return thoughts[id]


def open_thought():
    file_descriptor = open("encouraging.txt", 'r')
    for line in file_descriptor:
        if len(line) > 1:
            thoughts.append(line)


def wait(opening_time=3):
    """ wait function """
    time.sleep(opening_time)


def whatsapp_login():
    """ Whatsapp login wait instance """
    driver.get('https://web.whatsapp.com/')
    wait(10)


def send_message(text):
    """ Message sending function """
    web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
    web_obj.send_keys(unicode(text, errors='ignore'))
    web_obj.send_keys(Keys.RETURN)


def main():
    """ Driver function """
    open_thought()
    whatsapp_login()
    wait(10)
    for i in range(1, 2000):
        send_message(random_thought())
        print('Message sent: ' + str(i))
    wait(2)
    print('Message sent successfully')
    driver.quit()


if __name__ == '__main__':
    main()
