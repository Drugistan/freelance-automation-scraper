from selenium import webdriver
from time import sleep

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
import pandas as pd


class BuilderOnline:

    def __init__(self):
        self.builderOnline_url = "https://www.builderonline.com/data-analysis/?offset=320/"
        self.webDriverPath = "/home/darkside/PycharmProjects/upwork_task/webDriver"
        self.driverController = webdriver.Chrome(executable_path=self.webDriverPath)
        self.title_link = []

    def buliderOnline_Bot(self):
        self.driverController.get(self.builderOnline_url)
        sleep(20)
        box = self.driverController.find_elements(By.XPATH, '//div[@class="result type-article split"]')
        titles_list = []
        image_list = []
        links_list = []
        end_page_limit = self.driverController.find_element(By.XPATH, "//ul[@class='numbered-pagination pager']/li[5]/a[@class='page-count']")
        count = 0
        count_ = []
        for paginate_link in range(int(float(end_page_limit.text)) + 1):
            count = count + 1
            if count != 5:
                try:
                    for products in box:
                        links_list.append(products.find_element(By.CLASS_NAME, 'headline2').get_attribute('href'))
                        self.page(links_list)
                    next_pager = self.driverController.find_element(By.CLASS_NAME, 'next')
                    self.driverController.execute_script("arguments[0].scrollIntoView(true);", next_pager)
                    next_pager.click()

                    print("first")
                    sleep(5)
                except StaleElementReferenceException:
                    pass



                print(self.title_link)

    def page(self, x):
        print("x", x)


if __name__ == "__main__":
    callingObject = BuilderOnline()
    callingObject.buliderOnline_Bot()

# for pagination


#
# def buliderOnline_Bot(self):
#      self.driverController.get(self.builderOnline_url)
#      sleep(50)
#      count = 0
#      page = 1
#      pageIncrement = 10
#      maxRet = 50
#
#      end_page = self.driverController.find_element(By.XPATH, "//ul[@class='numbered-pagination pager']/li[5]/a[@class='page-count']")
#
#      print(int(end_page.text))
#      for x in range(int(float(end_page.text))+1):
#          try:
#              print(x)
#              print("Sd")
#              element = self.driverController.find_element(By.CLASS_NAME, 'next')
#              self.driverController.execute_script("arguments[0].scrollIntoView(true);", element)
#              element.click()
#              sleep(4)
#          except Exception as e:
#              print(f"Error occurred on page {x}: {e}")
