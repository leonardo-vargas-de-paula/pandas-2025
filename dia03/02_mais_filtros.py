# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacao_produto.csv")
df.sample(10)
# %%

df["idProduto"].isin([5,11])
# %%

dfClientes = pd.read_csv("../data/clientes.csv")
# %%
filtroCliente = dfClientes["dtCriacao"].isna()
# %%
dfClientes[filtroCliente]
# %%
filtroCliente = dfClientes["dtCriacao"].notna()
# %%
dfClientes[filtroCliente]
# %%
filtroCliente = ~dfClientes["dtCriacao"].notna()
dfClientes[filtroCliente]
# %%
