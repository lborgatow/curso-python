from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# ().utils.src.new_selenium

# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'


class ChromeAuto:
    """Realiza ações automaticamente em um navegador do Chrome"""

    def __init__(self, *options: str):
        self.chrome_options = webdriver.ChromeOptions()

        # chrome_options.add_argument('--headless')
        if options is not None:
            for option in options:
                self.chrome_options.add_argument(option)

        self.chrome_service = Service(
            executable_path=CHROME_DRIVER_PATH,
        )

        self.browser = webdriver.Chrome(
            service=self.chrome_service,
            options=self.chrome_options
        )

        self.username = None

    def access(self, url):
        """Acessa um site através do url"""
        self.browser.get(url)

    def sign_in(self):
        """Clica no botão 'Sign in'"""
        try:
            self.browser.find_element(By.LINK_TEXT, 'Sign in').click()
        except Exception as error:
            print(f'Erro ao clicar no botão "Sign in": {error}')

    def login(self, username, password):
        """Realiza o login na conta"""
        self.username = username

        try:
            self.browser.find_element(By.ID, 'login_field').send_keys(username)
            self.browser.find_element(By.ID, 'password').send_keys(password)
            self.browser.find_element(By.NAME, 'commit').click()
        except Exception as error:
            print(f'Erro ao fazer login: {error}')

    def click_profile(self):
        """Clica no botão do perfil"""
        try:
            # Quando não tiver certeza da html, utilizar CSS_SELECTOR:
            # botão direito --> Copy --> Copy selector
            self.browser.find_element(
                By.CSS_SELECTOR,
                'body > div.position-relative.js-header-wrapper > header > '
                'div.Header-item.position-relative.mr-0.d-none.d-md-flex'
            ).click()
        except Exception as error:
            print(f'Erro ao clicar no perfil: {error}')

    def verify_user(self):
        """Verifica se o usuário da conta está correto"""
        try:
            profile_link = self.browser.find_element(By.CLASS_NAME, 'user-profile-link')
            # Pega o html dentro de profile_link
            profile_link_html = profile_link.get_attribute('innerHTML')
        except Exception as error:
            print(f'Erro ao verificar usuário: {error}')
        else:
            try:
                assert self.username in profile_link_html
            except AssertionError:
                raise AssertionError('Usuário incorreto!')

    def enter_profile(self):
        """Entra no perfil do usuário"""
        try:
            # Clica em "Your profile"
            self.browser.find_element(By.LINK_TEXT, 'Your profile').click()
        except Exception as error:
            print(f'Erro ao entrar no perfil: {error}')

    def logout(self):
        """Faz logout da conta"""
        try:
            # Clica em "Sign out"
            self.browser.find_element(
                By.CSS_SELECTOR,
                'body > div.position-relative.js-header-wrapper > header >'
                ' div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button'
            ).click()
        except Exception as error:
            print(f'Erro ao fazer logout: {error}')

    def quit(self):
        """Fecha o navegador"""
        self.browser.quit()


if __name__ == '__main__':
    browser = ChromeAuto('--disable-gpu', '--no-sandbox')

    browser.access('https://github.com/')
    browser.sign_in()
    sleep(1)
    browser.login()  # Inserir o usuário e a senha --> browser.login('usuário', 'senha')

    sleep(1)
    browser.click_profile()
    sleep(1)
    browser.verify_user()

    browser.enter_profile()

    sleep(1)
    browser.click_profile()
    sleep(1)
    browser.logout()

    sleep(3)
    browser.quit()
