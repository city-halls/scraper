from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Tabatinga(object):

    def __init__(self):
        self.url = 'http://189.20.141.242:5656/Transparencia/'

    def get_csv_file(self, driver):
        try:
            driver.get(self.url)

            # Since the dataset button is hidden, we need to find the
            # dataset select menu first
            dataset_selector = driver.find_element_by_xpath(
                '//*[@id="LnkMenuDespesas"]')

            # Move the mouse to dataset selector
            actions = ActionChains(driver)
            actions.move_to_element(dataset_selector).click().perform()

            # Find and click on the dataset
            ds_button = driver.find_element_by_xpath(
                '//*[@id="lnkDespesasPor_ProjetoAtividade"]'
            )
            ds_button.click()

            # The page is a frame, so we must tell the driver
            # to switch to the frame
            frame = driver.find_element_by_xpath('//*[@id="frmPaginaAspx"]')
            driver.switch_to.frame(frame)

            # While there is no CVS button, wait for it
            download_as_csv_button = WebDriverWait(driver, 80).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="btnExportarCSV"]'))

            # Download
            download_as_csv_button.click()

            return True
        except Exception as ex:
            print(ex)
            return False
