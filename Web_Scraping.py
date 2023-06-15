import requests
from bs4 import BeautifulSoup
import pandas as pd
#Solicitando requicao do site
site = "https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/"
requisicao_site = requests.get(site)

#Extraindo tabela  do site
soup = BeautifulSoup(requisicao_site.text, "html.parser")
tabela = soup.find_all('table')
df = pd.read_html(str(tabela))
df = pd.DataFrame(df[0])

#Organizando Tabela
df.drop(['Times.1', 'Times.3'], axis=1, inplace=True)
df = df.rename(columns={'Times':'Posições'})
df = df.rename(columns={'Times.2':'Times'})

#Salvando Arquivo em XLSX
file_name = 'bras_2023.xlsx'
df.to_excel(file_name, index=False)
print('Arquivo Criado com sucesso.')
