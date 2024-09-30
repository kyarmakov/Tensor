from selenium.webdriver.remote.webelement import WebElement
from pages import *


def test_second_scenario(setup_driver):
    home_page: HomePage = HomePage(setup_driver)
    region_home_page: str = home_page.click_contacts_btn().get_region().text

    contacts_page: ContactsPage = home_page.click_contacts_link()
    region_contacts_page: str = contacts_page.get_region().text
    # Проверка, что определился ваш регион
    assert region_home_page == region_contacts_page, "Регион не определился"

    partners: list[WebElement] = contacts_page.get_partners()
    partners_list: list[str] = [partner.text for partner in partners]
    # Проверка, что есть список партнеров
    assert len(partners_list) > 0, "Нет списка партнеров"

    contacts_page.click_regions().click_region()
    changed: bool = contacts_page.check_text_changed()
    # Проверка, что подставился выбранный регион
    if changed:
        new_region: str = contacts_page.get_region().text
        assert new_region == ContactsPage.CHANGED_REGION_RU, "Выбранный регион не подставился"

    new_partners: list[WebElement] = contacts_page.get_partners()
    new_partners_list: list[str] = [partner.text for partner in new_partners]

    # Проверка, что список партнеров изменился
    assert partners_list != new_partners_list, "Список партнеров не изменился"
    # Проверка, что url содержит информацию выбранного региона
    assert ContactsPage.CHANGED_REGION_EN in contacts_page.get_url(), "url не содержит информацию выбранного региона"
    # Проверка, что title содержит информацию выбранного региона
    assert ContactsPage.CHANGED_REGION_RU in contacts_page.get_title(), "title не содержит информацию выбранного региона"
