# %%

import pandas as pd
import numpy as np
# %%

df = pd.read_csv("../data/clientes.csv")
df.sample(10)
# %%

df["pontos_100"] = df["qtdePontos"] + 100
# %%
df

# %%
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
# %%

df["emailTwitch"] = df["flEmail"] * df["flTwitch"]

# %%

df["qtdePontos"].describe()
# %%

df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()
# %%

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()
# %%
