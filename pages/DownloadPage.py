import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants.framework_constants import EXPLICIT_WAIT_TIME
from pages.BasePage import BasePage


class DownloadPage(BasePage):
    PLUGIN: str = "sbisplugin-setup-web.exe"
    PLUGIN_SIZE: float = 11.47

    def __init__(self, driver):
        self._driver = driver
        self._plugin_to_download = "//a[contains(@href, 'sbisplugin-setup-web.exe')]"

    @allure.step("Скачиваем плагин")
    def click_download_plugin(self, download_path: str):
        BasePage._click(self._driver, By.XPATH, self._plugin_to_download)

        WebDriverWait(self._driver, EXPLICIT_WAIT_TIME).until(
            lambda driver: any(filename == DownloadPage.PLUGIN for filename in os.listdir(download_path)))

    @allure.step("Получаем путь к скаченному файлу")
    def get_downloaded_file_path(self, download_path: str):
        return os.path.join(download_path, DownloadPage.PLUGIN)

    @allure.step("Получаем фактический размер скаченного файла")
    def get_actual_size_mb(self, downloaded_file_path: str):
        return round(os.path.getsize(downloaded_file_path) / (1024 * 1024), 2)

    @allure.step("Проверяем, скачался ли файл")
    def check_if_file_downloaded(self, download_path: str):
        return DownloadPage.PLUGIN in os.listdir(download_path)
