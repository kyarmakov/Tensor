import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.BasePage import BasePage
from pages.TensorPage import TensorPage


class ContactsPage(BasePage):
    CHANGED_REGION_RU: str = "Камчатский край"
    CHANGED_REGION_EN: str = "kamchatskij-kraj"

    def __init__(self, driver):
        self._driver = driver
        self._banner = "(//a[@href='https://tensor.ru/']/img)[1]"
        self._region = "(//span[contains(@class, 'sbis_ru-Region-Chooser__text')])[1]"
        self._first_partner = "((//div[@name='itemsContainer'])[1]/div[@item-parent-key])[1]"
        self._all_partners = "(//div[@name='itemsContainer'])[1]/div[@item-parent-key]//div[@title and contains(@class, 'sbisru-Contacts-List__name')]"
        self._new_region = "//li//span[text()='41 Камчатский край']"

    @allure.step("Переходим на https://tensor.ru/")
    def click_banner(self):
        BasePage._click(self._driver, By.XPATH, self._banner)
        BasePage._switch_to_new_window(self._driver)
        return TensorPage(self._driver)

    @allure.step("Получаем регион")
    def get_region(self):
        region: WebElement = BasePage._find(self._driver, By.XPATH, self._region)
        return region

    @allure.step("Проверяем, что регион изменился")
    def check_text_changed(self):
        changed: bool = BasePage._check_if_text_changed(self._driver, By.XPATH, self._region, ContactsPage.CHANGED_REGION_RU)
        return changed

    @allure.step("Получаем список партнеров")
    def get_partners(self):
        partner: WebElement = BasePage._find(self._driver, By.XPATH, self._first_partner)

        if partner:
            partners: list[WebElement] = BasePage._find_elements(self._driver, By.XPATH, self._all_partners)
            return partners
        else:
            return None

    @allure.step("Кликаем по региону")
    def click_regions(self):
        BasePage._click(self._driver, By.XPATH, self._region)
        return self

    @allure.step("Выбираем новый регион")
    def click_region(self):
        BasePage._click(self._driver, By.XPATH, self._new_region)

    @allure.step("Получаем URL")
    def get_url(self):
        url: str = BasePage._get_url(self._driver)
        return url

    @allure.step("Получаем title")
    def get_title(self):
        title: str = BasePage._get_title(self._driver)
        return title
