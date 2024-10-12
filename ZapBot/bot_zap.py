from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def send_message(driver, contato, message):
    try:
        search_box = driver.find_element('xpath', '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(contato)
        search_box.send_keys(Keys.ENTER)
        sleep(2) 
        message_box = driver.find_element('xpath', '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)  
        sleep(5)  
    except Exception as e:
        print('Não foi possível enviar a mensagem')

driver = get_driver()
driver.get('https://web.whatsapp.com/')
sleep(10) 

while True:
    while True:
        try:
            qr_code = driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')
            if not qr_code:
                break
        except Exception as e:
            break
    sleep(20)  
    contato = '' # Nome do Contato
    mensagem = '' #Mensagem para enviar
    send_message(driver, contato, mensagem)

driver.quit()