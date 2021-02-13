from selenium import webdriver
import time
from index import Main

class Test():
    def __init__(self):
        self.pd_cost = 'a-price-whole'
        self.pd_title = '//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"]'
        self.page_ = '//li[@class="a-last"]'

    def find_search_product(self):
        return self.search_product()

    def search_product(self):
        drive = webdriver.Chrome()
        drive.get('https://www.amazon.com/ref=nav_logo')
        search = Main(drive)
        search.search_products_go()
        drive.implicitly_wait(5)
        x = 0
        while x < 3:
            title = drive.find_elements_by_xpath(self.pd_title)
            print('Page', x)
            for ct in title:
                try:
                    cost = ct.find_element_by_class_name(self.pd_cost).text
                    if float(cost) > 10:
                        print(ct.find_element_by_tag_name('h2').text)
                except:
                    print('this have not cost')
            page = drive.find_element_by_xpath(self.page_)
            page.click()
            time.sleep(5)
            x = x+1

def main():
    test = Test()
    test.find_search_product()

if __name__ == "__main__":
    main()