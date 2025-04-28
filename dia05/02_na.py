# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes
# %%

clientes.dropna()
# %%

clientes
# %%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

# quando how="all" os subsets precisam ser todos nulos
#quando how="any" basta um dos subsets ser nulo
df.dropna(how="all",subset=["idade", "nome"])
# %%

df["idade"].fillna(0)
# %%
df.fillna({"nome": "lerolero", "idade":0})
# %%

medias = df[["idade", "salario"]].mean()
df.fillna(medias)

# %%
