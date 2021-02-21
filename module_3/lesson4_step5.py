from math import log, sin
from time import sleep

from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element_by_id('input_value').text
    print(x)
    answer = log(abs(12 * sin(int(x))))
    browser.find_element_by_id('answer').send_keys(str(answer))
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_class_name('btn-primary').click()


except:
    sleep(10)
    browser.quit()
