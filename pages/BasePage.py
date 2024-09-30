from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from constants.framework_constants import EXPLICIT_WAIT_TIME


class BasePage:
    @staticmethod
    def _find(driver, by: By, value: str):
        element: WebElement = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
            EC.visibility_of_element_located((by, value)))

        return element

    @staticmethod
    def _check_if_text_changed(driver, by: By, value: str, expected_value: str):
        changed: bool = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
            EC.text_to_be_present_in_element((by, value), expected_value))

        return changed

    @staticmethod
    def _click(driver, by: By, value: str):
        element: WebElement = BasePage._find(driver, by, value)
        element.click()

    @staticmethod
    def _click_js(driver, by: By, value: str):
        element: WebElement = BasePage._find(driver, by, value)
        driver.execute_script("arguments[0].click();", element)

    @staticmethod
    def _find_elements(driver, by: By, value: str):
        elements: list[WebElement] = driver.find_elements(by, value)
        return elements

    @staticmethod
    def _get_url(driver):
        return driver.current_url

    @staticmethod
    def _switch_to_new_window(driver):
        windows_num: int = len(driver.window_handles)
        new_window = driver.window_handles[windows_num - 1]
        driver.switch_to.window(new_window)

    @staticmethod
    def _get_title(driver):
        return driver.title
