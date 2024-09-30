import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.ContactsPage import ContactsPage
from pages.DownloadPage import DownloadPage


class HomePage(BasePage):
    def __init__(self, driver):
        self._driver = driver
        self._contacts_btn = "//div[text()='Контакты']"
        self._contacts_link = "//a[@href='/contacts']/span"
        self._region = "//div[contains(@class, 'sbisru-Header-ContactsMenu__items')]//span[contains(@class, 'sbis_ru-Region-Chooser__text')]"
        self._download_link = "//a[@href='/download']"

    @allure.step("Открываем подменю Контакты на главной странице")
    def click_contacts_btn(self):
        BasePage._click(self._driver, By.XPATH, self._contacts_btn)
        return self

    @allure.step("Переходим на страницу /contacts")
    def click_contacts_link(self):
        BasePage._click(self._driver, By.XPATH, self._contacts_link)
        return ContactsPage(self._driver)

    @allure.step("Получаем регион")
    def get_region(self):
        return BasePage._find(self._driver, By.XPATH, self._region)

    @allure.step("Переходим на страницу /download")
    def click_download_link(self):
        BasePage._click(self._driver, By.XPATH, self._download_link)
        return DownloadPage(self._driver)
