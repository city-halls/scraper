import os
from selenium import webdriver


class Scraper(object):

    def __init__(self):
        self.options = webdriver.ChromeOptions()

        self.download_path = os.path.dirname(
            os.path.realpath('./scraper')
        ) + '/data'

        # set the default download path
        self.options.add_experimental_option(
            'prefs', {
                'download.default_directory': self.download_path,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True
            }
        )

        # Does not close the browser after script get finished
        self.options.add_experimental_option('detach', True)

        # Create the driver with the options and the chromedriver path
        self.driver = webdriver.Chrome(
            '.data/chromedriver',
            chrome_options=self.options
        )

    def get_csv_file(self, city_hall):
        return city_hall.get_csv_file(self.driver)
