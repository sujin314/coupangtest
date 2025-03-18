from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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



    # 로그인
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

    # 로그인 입력 필드 찾기 (대기 추가)
        id_input = self.wait.until(EC.presence_of_element_located((By.ID, "login-email-input")))
        pw_input = self.wait.until(EC.presence_of_element_located((By.ID, "login-password-input")))
        login_button = self.wait.until(EC.presence_of_element_located((By.ID, "login-button")))

    # 로그인 정보 입력
        id_input.send_keys(ID)
        pw_input.send_keys(PASSWORD)
        login_button.click()

    # 로그인 후 페이지 로딩 대기
        WebDriverWait(self.driver, 10).until(EC.url_contains("mypage"))