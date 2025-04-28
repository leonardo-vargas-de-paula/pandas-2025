# %%
#primeira transcao diaria de cada cliente
import pandas as pd

# %%

dt = pd.read_csv("../data/transacoes.csv")
# %%
dt.head()
# %%
dt=dt.sort_values("dtCriacao")
# %%
dt["data"] = pd.to_datetime(dt["dtCriacao"]).dt.date
# %%
dt.sample(10)
# %%
dt.drop_duplicates(keep="first", subset=["idCliente", "data"])
# %%
