from math import log, sin
from time import sleep

from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    answer = log(abs(12 * sin(int(x))))
    browser.find_element_by_id('answer').send_keys(str(answer))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_class_name('btn-default').click()


except:
    sleep(10)
    browser.quit()
