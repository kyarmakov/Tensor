import os

import pytest
from selenium import webdriver
from constants.framework_constants import BASE_URL


@pytest.fixture(scope="function")
def setup_driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def setup_download_path():
    download_path = os.path.join(os.getcwd(), 'tests')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }

    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver, download_path
    driver.quit()
