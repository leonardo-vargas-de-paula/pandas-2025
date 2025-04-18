# %%

import pandas as pd
# %%

df_clientes = pd.read_csv("./data/clientes.csv")
df_clientes
# %%

df_clientes.head()
# %%

df_clientes.head(n = 10)
# %%
df_clientes.tail()
# %%
df_clientes.to_csv("./data/clientes.csv", index=False)
df_clientes.tail()

# %%
df_clientes= pd.read_excel("./data/clientes.xlsx")
# %%
df_clientes.to_csv("./data/clientes.csv", index=False)
# %%
df_clientes.tail()
# %%

#amostra aleatoria
df_clientes.sample(10)
# %%

df_clientes.shape
# %%
type(df_clientes.shape)
# %%

df_clientes.columns
# %%
df_clientes.index
# %%
df_clientes.info()
# %%
df_clientes.info(memory_usage="deep") #quantidade real de memoria

# %%
df_clientes.dtypes

# %%

df_clientes.dtypes["qtdePontos"]
# %%

