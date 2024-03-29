# -*- coding: utf-8 -*-
"""analise_exploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S2J93BYG6wNzRHiGhm4pHio6iE9Kt7JC
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#upload de arquivo
from google.colab import files
arq = files.upload()

#cria o DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

df.head()

df.shape

df.dtypes

#receita total
df["Valor Venda"].sum()

#cria coluna custo
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])

#custo total (arredonda 2 casas decimais)
round(df["custo"].sum(), 2)

#cria coluna lucro
df["lucro"] = df["Valor Venda"] - df["custo"]

#lucro total
round(df["lucro"].sum(), 2)

df.head(3)

#cria coluna tempo de envio do produto
df["Tempo_Envio"] = df["Data Envio"] - df["Data Venda"]

df.head(3)

#cria coluna tempo de envio do produto (tira os dias)
df["Tempo_Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(3)

df["Tempo_Envio"].dtype

#media tempo de envio por marca
df.groupby("Marca")["Tempo_Envio"].mean()

#verifica se falta dados
df.isnull().sum()

#agrupa por ano e marca, e mostra o lucro total para cada item
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

#melhora a formatacao dos numeros
pd.options.display.float_format = '{:20,.2f}'.format

#colocando um index, resetando
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()

#lucro_ano

#total de produtos vendidos, em ordem decrescente
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#grafico de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de produtos vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro por ano")
plt.xlabel("Ano")
plt.ylabel("Receita");#legenda de cada coluna por padrao na vertical

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro por Mes")
plt.xlabel("Mes")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro por Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');#legenda de cada coluna será horizontal

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro por Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df["Tempo_Envio"].describe()

#grafico de boxplot
plt.boxplot(df["Tempo_Envio"]);

#histograma
plt.hist(df["Tempo_Envio"]);

#tempo minimo de envio
df["Tempo_Envio"].min()

#tempo maximo de envio
df["Tempo_Envio"].max()

#identifica o Outlier
df[df["Tempo_Envio"] == 20]



df.to_csv("df_vendas_novo.csv", index=False)