import pytest
from selenium.webdriver.remote.webelement import WebElement
from pages import *


def test_first_scenario(setup_driver):
    home_page: HomePage = HomePage(setup_driver)
    contacts_page: ContactsPage = home_page.click_contacts_btn().click_contacts_link()

    tensor_page: TensorPage = contacts_page.click_banner()
    # Проверяем, что есть блок 'Сила в людях'
    assert tensor_page.get_block().text == TensorPage.BLOCK_HEADER

    about_page: AboutPage = tensor_page.click_about_link()
    # Проверяем, что открывается https://tensor.ru/about
    assert about_page.get_url() == AboutPage.URL

    # Проверяем, что у всех фотографии раздела Работаем одинаковые высота и ширина
    images: list[WebElement] = about_page.get_images()
    first_image_size: tuple[int, int] = (images[0].size["width"], images[0].size["height"])
    all_have_same_size: bool = all((image.size["width"], image.size["height"]) == first_image_size for image in images)

    if not all_have_same_size:
        pytest.fail("У фотографий разные размеры")
