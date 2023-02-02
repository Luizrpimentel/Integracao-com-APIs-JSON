import requests
import json
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

# Pegar a Cotação Atual de Todas as Moedas
cotacao = requests.get('https://economia.awesomeapi.com.br/json/all').json()
cotacao_df = pd.DataFrame.from_dict(cotacao,orient='index')
display (cotacao_df)

#Qual foi a última cotação do Dólar, do Euro e do BitCoin?
ultima_cotaçãoUSD = cotacao_df['bid'][0]
ultima_cotaçãoBTC = cotacao_df['bid'][5]
ultima_cotaçãoEUR = cotacao_df['bid'][7]
display('USD: {} , BTC: {} , EUR:{}'.format(ultima_cotaçãoUSD,ultima_cotaçãoBTC,ultima_cotaçãoEUR))

#Pegar a cotação dos últimos 30 dias do dólar
cotacao_usd = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30').json()
cotacao_usd_df = pd.DataFrame.from_dict(cotacao_usd).rename(columns = {'code': 'USD', 'codein': 'BRL'})
display(cotacao_usd_df)

#Pegar as cotações do BitCoin de Jan/20 a Out/20
cotacao_BTC = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20200101&end_date=20201031').json()
cotacao_BTC_df = pd.DataFrame.from_dict(cotacao_BTC).rename(columns = {'code': 'BTC', 'codein': 'BRL'})
display(cotacao_BTC_df)

#Gráfico com as cotações do BitCoin
lista_cotacaoBTC = [float(item['bid'])for item in cotacao_BTC]
lista_cotacaoBTC.reverse()
plt.figure(figsize=(15,5))
plt.plot(lista_cotacaoBTC)
plt.show()