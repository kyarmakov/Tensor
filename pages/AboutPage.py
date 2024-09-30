import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.BasePage import BasePage


class AboutPage(BasePage):
    URL: str = "https://tensor.ru/about"

    def __init__(self, driver):
        self._driver = driver
        self._first_image = "(//h2[text()='Работаем']/parent::div/following-sibling::div//img)[1]"
        self._all_images = "//h2[text()='Работаем']/parent::div/following-sibling::div//img"

    @allure.step("Получаем URL")
    def get_url(self):
        return BasePage._get_url(self._driver)

    @allure.step("Получаем все изображения в блоке 'Работаем'")
    def get_images(self):
        image: WebElement = BasePage._find(self._driver, By.XPATH, self._first_image)

        if image:
            images: list[WebElement] = BasePage._find_elements(self._driver, By.XPATH, self._all_images)
            return images
        else:
            return None


