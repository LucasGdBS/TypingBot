'''Modulo da classe TypingBot'''
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TypingBot:
    '''Classe que representa o bot que será executado nos sites de digitação'''
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.driver = None

    def init_diver(self):
        '''Inicializa o driver do selenium'''
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def write_alfabet(self):
        '''Escreve o alfabeto no site TypeTheAlphabet'''
        self.init_diver()

        alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.driver.get('https://typethealphabet.app')
        sleep(0.5)

        ActionChains(self.driver).send_keys(alfabet).perform()

        sleep(5)
        self.driver.close()

    def monkey_type(self):
        '''Faz o teste de velocidade de escrita no site MonkeyType'''

        self.init_diver()

        self.driver.get('https://monkeytype.com')
        sleep(2)

        self.driver.find_element(By.TAG_NAME, 'button').click()
        sleep(0.5)

        while self.driver.find_elements(By.CLASS_NAME, 'time'):
            # Aguardar até que a palavra esteja presente
            palavra = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'word.active'))
            )

            letras = palavra.find_elements(By.TAG_NAME, 'letter')

            # Enviar as letras e pressionar a barra de espaço
            ActionChains(self.driver)\
                .send_keys(''.join([letra.text for letra in letras]) + ' ')\
                .perform()

        sleep(10)

        self.driver.close()

alfa = TypingBot()
alfa.write_alfabet()
alfa.monkey_type()
