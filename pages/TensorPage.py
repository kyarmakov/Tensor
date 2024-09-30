import allure
from selenium.webdriver.common.by import By

from pages.AboutPage import AboutPage
from pages.BasePage import BasePage


class TensorPage(BasePage):
    BLOCK_HEADER: str = "Сила в людях"

    def __init__(self, driver):
        self._driver = driver
        self._block = "//p[text()='Сила в людях']"
        self._about_link = "//p[text()='Сила в людях']/parent::div//child::a[@href='/about']"

    @allure.step("Получаем блок 'Сила в людях'")
    def get_block(self):
        return BasePage._find(self._driver, By.XPATH, self._block)

    @allure.step("Переходим на страницу /about")
    def click_about_link(self):
        BasePage._click_js(self._driver, By.XPATH, self._about_link)
        return AboutPage(self._driver)
