# %% 

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv")
df
# %%
df["qtdePontos"].astype(int)
# %%

df["dtCriacao"] = df["dtCriacao"].replace(
    {"0000-00-00 00:00:00.000":"2024-01-01 00:00:00.000"}
)

# %%
df["dtCriacao"] = pd.to_datetime(df["dtCriacao"])
# %%

df["dtCriacao"].dt.year
# %%
