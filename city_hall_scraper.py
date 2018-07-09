import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from collections import namedtuple

_dataset = namedtuple('Dataset', ['name', 'xpath'])

# project_or_activity_expenses -- Despesas por Projeto/Atividade
datasets = [_dataset('project_or_activity_expenses',
                     '//*[@id="lnkDespesasPor_ProjetoAtividade"]')]


def download_dataset(dataset_name, download_path):
    for ds in datasets:
        if dataset_name == ds.name:
            options = webdriver.ChromeOptions()

            # set the default download path
            options.add_experimental_option('prefs', {
                'download.default_directory': download_path,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True})

            # Does not close the browser after script get finished
            options.add_experimental_option('detach', True)

            # Create the driver with the options and the
            # chromedriver path
            driver = webdriver.Chrome('.data/chromedriver',
                                      chrome_options=options)

            # go to the url
            driver.get('http://177.139.249.168:5656/Transparencia/')

            # Since the dataset button is hidden, we need to find the
            # dataset select menu first
            dataset_selector = driver.find_element_by_xpath(
                '//*[@id="LnkMenuDespesas"]')

            # Move the mouse to dataset selector
            actions = ActionChains(driver)
            actions.move_to_element(dataset_selector).click().perform()

            # Find and click on the dataset
            ds_button = driver.find_element_by_xpath(ds.xpath)
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

            break
    else:
        raise NotImplementedError()


def main():
    ds = 'project_or_activity_expenses'
    download_path = os.path.dirname(os.path.realpath(__file__)) + '/data'
    download_dataset(ds, download_path)

if __name__ == '__main__':
    main()
