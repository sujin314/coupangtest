
import time

import pytest 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from urllib import parse

from tests.page.mainpage import MainPage
from tests.page.loginpage import LoginPage

@pytest.mark.usefixtures("driver") 
class TestLoginPage:

# 로그인 후 검색
# 1. 메인페이지 열기
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

# 2. 로그인 버튼 클릭 후 로그인 화면 이동
            login_page = LoginPage(driver)
            login_page.click_by_LINK_TEXT('로그인')
# 3. 로그인
            login_page.login()
            wait.until(EC.url_contains("mypage"))
            assert "mypage" in driver.current_url
            driver.save_screenshot('로그인-성공.png')

            time.sleep(2)
            driver.back()

            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-링크텍스트-실패-노서치.png')
            assert False
        except TimeoutError as e:
            driver.save_screenshot('메인페이지-링크텍스트-실패-타임에러.png')
            assert False

@pytest.mark.usefixtures("driver") 
class TestSearch:
    def test_search_notebook(self, driver: WebDriver):
            try: 
                ITEMS_XPATH = "//form//ul/li"
                SEARCH_BOX_XPATH = "//input[@type='search']"
                wait = ws(driver, 10)

# 3. "노트북" 검색.. 
                main_page = MainPage(driver)
                main_page.search_items('노트북')

# 4. 검색 결과 나타날 때까지 대기
                ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))

# 5. 검색 결과 가져오기
                items = driver.find_elements(By.XPATH, ITEMS_XPATH)
                item_name = parse.quote('노트북')

# 6. 검색 결과 확인
                assert len(items) > 0
                assert item_name in driver.current_url

                driver.save_screenshot('검색-성공.png')

            except NoSuchElementException as e:
                assert False
