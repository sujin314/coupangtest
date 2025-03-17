import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.page.mainpage import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 1. 로그인 전 검색
# 2. 메인 페이지 접속
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.coupang.com/")
    yield driver
    driver.quit()

def test_open_main_page(driver: WebDriver):
    main_page = MainPage(driver)
    main_page.open()
    WebDriverWait(driver, 10).until(EC.url_contains("coupang.com"))
    assert "coupang.com" in driver.current_url

# 3. 검색창 찾기
def test_search_product()
search_box = driver.find_element(By.ID, "headerSearchKeyword")

# 4. 검색창 "노트북" 작성, 엔터
search_box.send_keys("노트북")
search_box.send_keys(Keys.RETURN)

# 5. 결과 확인
assert "노트북" in driver.title




# def test_search_with_login(driver):
#     """ 로그인 후 검색 기능 테스트 """
#     driver.get("https://www.coupang.com/")  

#     # 로그인 버튼 클릭
#     login_button = driver.find_element(By.XPATH, "//a[contains(text(), '로그인')]")
#     login_button.click()

#     # 로그인 정보 입력
#     username = driver.find_element(By.NAME, "loginEmail")  # 이메일 입력창
#     password = driver.find_element(By.NAME, "password")  # 비밀번호 입력창

#     username.send_keys("your_email@example.com")  # 여기에 실제 이메일 입력
#     password.send_keys("your_password")  # 여기에 실제 비밀번호 입력
#     password.send_keys(Keys.RETURN)  # 로그인 실행

#     # 로그인 성공 확인 (예: 마이페이지 버튼 존재 여부)
#     assert "마이쿠팡" in driver.page_source  

#     # 검색 테스트 실행
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys("노트북")
#     search_box.send_keys(Keys.RETURN)

#     assert "노트북" in driver.title  # 검색 결과 페이지 확인





# 1. 로그인 후 검색
# 2. 메인 페이지 접속
# 3. 로그인 정보 입력
# 4. 