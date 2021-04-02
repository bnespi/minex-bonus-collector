from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass


def btn_click(btn):
    btn.click()


def open_site(driver, url):
    driver.get(url)


def click_enter(txtbox):
    txtbox.send_keys(Keys.ENTER)


def main(uname, pword):
    driver = webdriver.Chrome()

    login_site = 'https://minex.world/login'
    open_site(driver, login_site)

    username = driver.find_element_by_xpath('//*[@id="InputEmail"]')
    username.send_keys(uname)

    password = driver.find_element_by_xpath('//*[@id="InputPass"]')
    password.send_keys(pword)

    sleep(2)
    click_enter(password)

    bonuses = 'https://minex.world/cabinet/bonuses'
    open_site(driver, bonuses)

    get_bonus = driver.find_element_by_xpath('//*[@id="get-bonus"]')
    btn_click(get_bonus)
    sleep(2)
    driver.close()


user = input('Username:')
password = getpass.getpass('Password: ')
while True:
    if __name__ == '__main__':
        main(user, password)
    sleep(3600)