
class Main:
    def __init__(self, driver):
        self.drive = driver
        self.url_home = 'https://www.amazon.com/ref=nav_logo'
        self.search = '//*[@id="twotabsearchtextbox"]'
        self.button_search = '//*[@id="nav-search-submit-button"]'

    def search_products_go(self):
        return self.search_products()

    def search_products(self):
        search = self.drive.find_element_by_xpath(self.search)
        search.click()
        search.send_keys('notebooks for work')
        button = self.drive.find_element_by_xpath(self.button_search)
        button.click()



