import pytest
from pages import HomePage
from pages.DownloadPage import DownloadPage


def test_third_scenario(setup_download_path):
    driver, download_path = setup_download_path

    home_page: HomePage = HomePage(driver)
    download_page: DownloadPage = home_page.click_download_link()
    download_page.click_download_plugin(download_path)

    # Проверка, что плагин скачался
    if not download_page.check_if_file_downloaded(download_path):
        pytest.fail("No such file")

    required_size_mb: float = DownloadPage.PLUGIN_SIZE
    downloaded_file_path: str = download_page.get_downloaded_file_path(download_path)
    actual_size_mb: float = download_page.get_actual_size_mb(downloaded_file_path)

    # Проверка, что размеры файлов совпадают
    if not (actual_size_mb == required_size_mb):
        pytest.fail("Фактический размер скачанного плагина не соответствует требуемому")
