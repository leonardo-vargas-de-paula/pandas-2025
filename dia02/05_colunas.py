# %%

import pandas as pd
# %%

df = pd.read_csv("./data/transacoes.csv")
df
# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%

df.dtypes

# %%
df.rename(columns={"qtdePontos": "qtPontos"})
# %%

df
df = df.rename(columns={"qtdePontos": "qtPontos"})
# %%
df
# %%
df = df.rename(columns={"qtdePontos": "qtPontos" ,
                        "descSistemaOrigem": "sistemaOrigem"})
df
# %%
df["idCliente"]

# %%

df[["idCliente", "idTransacao"]]
# %%

#SELECT * FROM DF
df
#select idCliente from df
df[["idCliente"]]
#select idCliente, qtPontos from df limit 5
df[["idCliente", "qtPontos"]].sample(5)
#select idCliente, idTransacao, qtPontos from df limit 5
df[["idCliente", "idTransacao", "qtPontos"]].head(5)
# %%

colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]  
# %%
