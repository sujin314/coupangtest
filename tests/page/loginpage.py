import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.LOGIN_LINK_TEXT = "로그인"
        
    # 로그인 버튼 클릭
    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.LOGIN_LINK_TEXT))
        )
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.LOGIN_LINK_TEXT))
        )
        login_button.click()

    # 링크 텍스트 버튼 클릭
    def click_by_LINK_TEXT(self, link_text: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_text))
        )
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, link_text))
        )
        login_button.click()

    # 로그인 정보 입력
    def login(self, username=None, password=None):
        if username is None or password is None:
            try:
                from tests.page.password import ID, PASSWORD
            except ImportError:
                ID = "test_user"
                PASSWORD = "test_password"
                print("⚠️ password.py 파일이 없습니다. 테스트용 기본값을 사용합니다.")
        else:
            ID = username
            PASSWORD = password

        id_input = self.wait.until(EC.presence_of_element_located((By.ID, "login-email-input")))
        id_input.click()
        time.sleep(1)
        id_input.send_keys(ID)

        pw_input = self.wait.until(EC.presence_of_element_located((By.ID, "login-password-input")))
        pw_input.click()
        time.sleep(1)
        pw_input.send_keys(PASSWORD) 

        pw_input.send_keys(Keys.RETURN)
        time.sleep(2)
    
    # 로그인 후 페이지 로딩 대기
        WebDriverWait(self.driver, 10).until(EC.url_contains("mypage"))