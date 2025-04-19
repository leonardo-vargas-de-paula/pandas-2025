# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacoes.csv")
df.sample()
# %%

filtro = df["qtdePontos"] >= 50

# %%
filtro = (df["qtdePontos"] >= 50)&(df["qtdePontos"] < 100)
filtro

# %%
df[filtro]
# %%
filtro = (df["qtdePontos"] == 1)|(df["qtdePontos"] == 100)
filtro
# %%
df[filtro]
# %%

filtro = (df["qtdePontos"] > 0)&(df["qtdePontos"] <= 50)&(df["dtCriacao"]>="2025-01-01")
# %%
df[filtro]
# %%
