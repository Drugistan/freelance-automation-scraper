from selenium import webdriver
from time import sleep

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd


class BuilderOnline:

    def __init__(self):
        self.builderOnline_url = "https://www.builderonline.com/data-analysis/?offset=320/"
        self.webDriverPath = "/home/darkside/PycharmProjects/upwork_task/webDriver"
        self.driverController = webdriver.Chrome(executable_path=self.webDriverPath)
        self.title_link = []

    def buliderOnline_Bot(self):
        box = self.driverController.find_elements(By.XPATH, '//div[@class="result type-article split"]')
        count = 0
        list_of_links = [
            "https://www.builderonline.com/data-analysis/private-equity-and-home-builders-align-to-accelerate-and-transform-the-industry_o",
            "https://www.builderonline.com/data-analysis/new-home-lot-inventory-drops-24-2-yoy-to-new-lows_o",
            "https://www.builderonline.com/data-analysis/ninety-nine-percent-of-u-s-metros-recorded-rising-home-prices-in-q1_o",
            "https://www.builderonline.com/data-analysis/nonfarm-payroll-employment-rises-266-000-in-april-marking-a-slowdown-in-growth_o",
            "https://www.builderonline.com/data-analysis/zonda-unveils-the-nations-most-lucrative-remodeling-projects-in-2021-cost-vs-value-report_o",
            "https://www.builderonline.com/data-analysis/breaking-down-the-first-quarter-results-for-publicly-traded-home-builders_o",
            "https://www.builderonline.com/data-analysis/the-metro-phoenix-area-has-lowest-level-of-finished-lots-in-over-15-years_o",
            "https://www.builderonline.com/data-analysis/the-arguments-for-and-against-higher-government-debt-levels_o",
            "https://www.builderonline.com/data-analysis/covid-19-update-expecting-economic-growth_o",
            "https://www.builderonline.com/data-analysis/baby-boomers-migrating-to-las-vegas-tampa-and-phoenix-metros_c",
            "https://www.builderonline.com/data-analysis/pending-home-sales-rebound-1-9-in-march_o",
            "https://www.builderonline.com/data-analysis/builders-look-to-expand-beyond-north-carolinas-major-markets_o",
            "https://www.builderonline.com/data-analysis/high-lumber-costs-add-more-than-35k-to-new-home-prices_c",
            "https://www.builderonline.com/data-analysis/case-shiller-home-price-index-reports-12-annual-gain-for-february_o",
            "https://www.builderonline.com/data-analysis/new-single-family-home-sales-surge-in-march_o",
            "https://www.builderonline.com/data-analysis/new-home-pending-sales-index-drops-6-1-month-over-month-on-tight-inventory_o",
            "https://www.builderonline.com/data-analysis/does-the-austin-housing-market-have-too-much-of-a-good-thing_o",
            "https://www.builderonline.com/data-analysis/housing-starts-completions-and-permits-leap-forward-in-march_o",
            "https://www.builderonline.com/data-analysis/nahb-wells-fargo-hmi-rises-one-point-to-83-in-april_o",
            "https://www.builderonline.com/data-analysis/are-we-in-a-goldilocks-economy_o",
            "https://www.builderonline.com/data-analysis/zonda-acquires-urban-analytics-expanding-footprint-into-canada_o",
            "https://www.builderonline.com/data-analysis/america-at-home-consumers-place-more-importance-on-well-being_o",
            "https://www.builderonline.com/data-analysis/median-age-of-owner-occupied-homes-is-39-years-varies-widely-by-state_c",
            "https://www.builderonline.com/data-analysis/nonfarm-payrolls-rose-by-916-000-in-march-unemployment-drops-to-6_o",
            "https://www.builderonline.com/data-analysis/rolling-the-dice-on-recovery_o",
            "https://www.builderonline.com/data-analysis/pending-home-sales-fall-10-6-in-february_o",
            "https://www.builderonline.com/data-analysis/home-prices-continue-to-rise-across-the-u-s_o",
            "https://www.builderonline.com/data-analysis/the-motivations-and-risks-behind-todays-seven-main-home-buyers_o",
            "https://www.builderonline.com/data-analysis/houstons-new-home-market-riding-the-tailwinds-despite-the-headwinds_o",
            "https://www.builderonline.com/data-analysis/can-dallas-fort-worth-remain-no-1-in-home-building_o",
            "https://www.builderonline.com/data-analysis/new-residential-sales-decline-sharply-in-february_o",
            "https://www.builderonline.com/data-analysis/existing-home-sales-drop-6-6-in-february_o",
            "https://www.builderonline.com/data-analysis/new-home-psi-rises-35-yoy-sales-decline-2-4-from-january_o",
            "https://www.builderonline.com/data-analysis/a-little-spring-in-orlandos-step_o",
            "https://www.builderonline.com/data-analysis/housing-starts-and-permits-fall-in-february_o",
            "https://www.builderonline.com/data-analysis/rising-costs-interest-rates-and-supply-shortages-depress-builder-sentiment_o",
            "https://www.builderonline.com/data-analysis/nearly-90-of-builders-report-issues-getting-appliances_c",
            "https://www.builderonline.com/data-analysis/mortgage-outlook-what-2021-holds-for-buyers-builders-and-lenders_o",
            "https://www.builderonline.com/data-analysis/nonfarm-payrolls-rose-by-379-000-in-february-unemployment-steady-at-6-2_o",
            "https://www.builderonline.com/data-analysis/builders-crack-the-affordability-code-in-san-antonio_o",
            "https://www.builderonline.com/data-analysis/how-the-covid-vaccine-could-help-spur-the-upcoming-home-shopping-season_c",
            "https://www.builderonline.com/data-analysis/economic-growth-and-recreation-access-draw-home-buyers-to-salt-lake-city_o",
            "https://www.builderonline.com/data-analysis/covid-19-update-economy-back-in-growth-mode_o",
            "https://www.builderonline.com/data-analysis/pending-home-sales-drop-2-8-month-over-month-in-january_o",
            "https://www.builderonline.com/data-analysis/new-home-sales-inch-higher-in-january_o",
            "https://www.builderonline.com/data-analysis/case-shiller-home-price-index-reports-10-4-annual-gain-to-end-2020_o",
            "https://www.builderonline.com/data-analysis/the-challenges-millennials-face-to-attaining-homeownership_o",
            "https://www.builderonline.com/data-analysis/pending-home-sales-rose-28-1-yoy-in-january_o",
            "https://www.builderonline.com/data-analysis/nar-existing-home-sales-rose-0-6-in-january_o",
            "https://www.builderonline.com/data-analysis/single-family-starts-dip-in-january-while-permits-rise_o",
            "https://www.builderonline.com/data-analysis/new-home-lot-supply-index-drops-11-6-in-q4-2020_o",
            "https://www.builderonline.com/data-analysis/nahb-wells-fargo-index-inches-to-84-in-february_o",
            "https://www.builderonline.com/data-analysis/home-prices-up-in-all-metros-for-q4-2020_o",
            "https://www.builderonline.com/data-analysis/attached-to-reality-in-seattle_o",
            "https://www.builderonline.com/data-analysis/nonfarm-payroll-employment-rises-by-49-000-in-january-unemployment-falls-to-6-3_o",
            "https://www.builderonline.com/data-analysis/america-at-home-rising-new-home-demand-from-renters_o",
            "https://www.builderonline.com/data-analysis/housing-momentum-in-the-midwest_o",
            "https://www.builderonline.com/data-analysis/pending-home-sales-reach-december-highs-down-0-3-from-november_o",
            "https://www.builderonline.com/data-analysis/covid-19-update-well-feel-good-when_o",
            "https://www.builderonline.com/data-analysis/new-home-sales-increase-slightly-in-final-month-of-2020_o",

        ]


        for url in list_of_links:
            print(url)
            self.extract(url)

    def extract(self, links):
        self.driverController.get(links)
        sleep(5)
        list_of_title = []
        list_of_image = []
        list_of_decsription = []
        list_of_author = []
        list_of_links = []

        list_of_title.append(self.driverController.find_element(By.XPATH, "//h1[@class='o-article__headline']").text)
        list_of_decsription.append(self.driverController.find_element(By.XPATH,
                                                                      "//article[@class='o-article module -editorial']/div[@class='o-article__body article-body -editorial']//p").text)
        try:
            list_of_author.append(self.driverController.find_element(By.XPATH,
                                                                     "//div[@class='o-article__byline byline normal--hwcorp']/a").text)
            print('Element found with primary XPath!')
        except NoSuchElementException:
            # If the element is not found, try the fallback XPath expression
            try:
                element = "No Author name"
                list_of_author.append(element)
                print('Element found with fallback XPath!')
            except NoSuchElementException:
                print('Element not found')

        list_of_links.append(links)

        try:
            element = self.driverController.find_element(By.XPATH,
                                                         "//div[@class='enhancement-mod image ']/figure/img").get_attribute(
                'src')
            list_of_image.append(element)
            print('Element found with primary XPath!')
        except NoSuchElementException:
            # If the element is not found, try the fallback XPath expression
            try:
                element = self.driverController.find_element(By.XPATH,
                                                             "//div[@class='o-article__body article-body -editorial']/div[@class='enhancement-mod image left']/figure/img").get_attribute(
                    'src')
                list_of_image.append(element)
                print('Element found with fallback XPath!')
            except NoSuchElementException:
                try:
                    element = "None"
                    list_of_image.append(element)
                    print('Element found with fallback XPath!')
                except NoSuchElementException:
                    print('Element not found')
        data = {
            "Article Title": list_of_title,
            "Article Description": list_of_decsription,
            "Article Author": list_of_author,
            "Article Link": list_of_links,
            "Article Image": list_of_image,

        }
        print(data)
        df = pd.DataFrame(data)
        df.to_csv("builderOnline.csv", index=False, mode='a', header=False)
        print("done")


if __name__ == "__main__":
    callingObject = BuilderOnline()
    callingObject.buliderOnline_Bot()

