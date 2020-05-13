from selenium import webdriver


def crawling(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_driver_path = './chromedriver'
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    return html
    driver.close()


if __name__ == '__main__':
    print('연결 테스트 입니다.')
    print(crawling('https://hihd.imweb.me/'))

