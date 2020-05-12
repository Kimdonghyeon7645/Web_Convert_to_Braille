from selenium import webdriver
import time


def crawling(url):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    chrome_driver_path = './chromedriver'
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    driver.close()
    return html

if
print(crawling('https://youtu.be/wQYHQ7Lme-g'))
