# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:06:15 2024

@author: Victor Hugo
"""
!pip install plotly!

import pandas as pd
import numpy as np
import plotly.express as px

dados = pd.read_csv('Dados_totais.csv')
#Fonte dos dados: https://caelum-online-public.s3.amazonaws.com/2604-clustering-aplicado-recomendando-musicas-k-means/01/2604-dados.zip

dados_generos = pd.read_csv('data_by_genres.csv')
dados_anos = pd.read_csv('data_by_year.csv')

#%% Analisando os dados

#dados gerais
dados.head()
dados_describe = dados.describe()

dados.info()
dados['year'].unique()

dados = dados.drop(columns=['explicit', 'key', 'mode'])



#dados por generos

dados_generos.head()
describe_generos = dados_generos.describe()
dados_generos = dados_generos.drop(columns=['key', 'mode'])
dados.isnull().sum()

#dados por anos

dados_anos.head()
describe_anos = dados_anos.describe()
dados_anos = dados_anos.drop(columns=['key', 'mode'])
dados_anos['year'].unique()

dados_anos = dados_anos[dados_anos['year'] >= 2000]

dados_anos['year'].unique()
dados_anos = dados_anos.drop(['index'], axis=1)

#%% Analise gráficas dos dados

fig = px.line(dados, x='year', y='loudness', markers=True)
fig.show()
