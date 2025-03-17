from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class MainPage:
    URL = "https://www.coupang.com"
    SEARCH_INPUT_ID = "headerSearchKeyword"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)

    # 검색 기능
    def search_items(self, item_name: str):
        search_input_box = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, self.SEARCH_INPUT_ID))
        )
        search_input_box.clear()
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)

    # 로그인 기능 
    # 로그인 버튼 클릭
    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.LOGIN_LINK_TEXT))
        )
        login_button.click()

    # 링크 텍스트 버튼 클릭
    def click_by_LINK_TEXT(self, link_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, link_text)
        login_button.click()


