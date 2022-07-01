from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.amazon.com.br/iPhone-Branco-com-Tela-C%C3%83%C2%A2mera/dp/B08N1MG4VL/ref=sr_1_7?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1I5KAQS1F3KJL&keywords=celular%2Biphone&qid=1648250448&sprefix=celular%2Biphon%2Caps%2C185&sr=8-7&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&th=1')

preco_inteiro = browser.find_element(By.CLASS_NAME, "a-price-whole")
preco_decimal = browser.find_element(By.CLASS_NAME, "a-price-fraction")

preco_amazon = preco_inteiro.text +"," +preco_decimal.text
print(preco_amazon)
