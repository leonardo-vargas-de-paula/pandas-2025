# %%

import pandas as pd
# %%

df = pd.read_csv("./data/clientes.csv")
df
# %%
df.to_csv("./data/clientes.csv")
# %%

df.to_csv("clientes.csv", index=False)
# %%
df.to_parquet("dia02/clientes.parquet")
# %%
df.to_excel("clientes.xlsx", index=False)
# %%
df = pd.read_csv("./data/teste.csv", sep=";")
df
# %%
