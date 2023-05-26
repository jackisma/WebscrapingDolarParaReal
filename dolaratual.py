!pip install requests
!pip install bs4

from os import replace
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
x = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar',headers=headers)
x2 = x.content
site = BeautifulSoup(x2,'html.parser')
dolar = site.find('div', attrs={'class':'style__Text-sc-1a6mtr6-2 ljisZu'})
valora = float(input('Quantos reais deseja converter para dólar ? '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Cotação atual do dólar:')
num = dolar.text[0:4]
num = num.replace(',','.')
num = float(num)
print(dolar.text)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Voce receberá ',round(valora/num,2),' dólares')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
