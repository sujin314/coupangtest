import time

import pytest 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from urllib import parse

from tests.page.mainpage import MainPage


@pytest.mark.skip(reason="다함")
@pytest.mark.usefixtures("driver") 
class TestMainPage:

# 로그인 전 검색
# 2. 메인 페이지 접속
    def test_open_main_page(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//form//ul/li"
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            time.sleep(2)

# 3. "노트북" 검색.. 
            main_page.search_items('노트북')

# 4. 검색 결과 나타날 때까지 대기
            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))

# 5. 검색 결과 가져오기
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)
            item_name = parse.quote('노트북')

# 6. 검색 결과 확인
            assert len(items) > 0
            assert item_name in driver.current_url
         
        except NoSuchElementException as e:
            assert False
