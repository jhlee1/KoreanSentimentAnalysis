from selenium import webdriver


class Browser:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('—incognito')

        self.webDriver = webdriver.Chrome(executable_path='resources/chromedriver.exe', chrome_options=option)
        self.webDriver.maximize_window()
        self.webDriver.implicitly_wait(1)

    def get_page(self, url):
        self.webDriver.get(url)

    def get_element_by_xpath(self, xpath):
        return self.webDriver.find_element_by_xpath(xpath)

    def get_elements_by_xpath(self, xpath):
        return self.webDriver.find_elements_by_xpath(xpath)

    def click_element(self, element):
        return element.click()

    def click_element_by_xpath(self, xpath):
        return self.webDriver.find_element_by_xpath(xpath).click()

    def scroll_to_element(self, element):
        self.webDriver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.webDriver.current_url
