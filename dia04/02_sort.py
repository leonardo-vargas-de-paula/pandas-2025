# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.sample(10)
# %%

clientes["qtdePontos"].sort_values()
# %%

maxPontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == maxPontos
clientes[filtro]
# %%

clientes.sort_values(by="qtdePontos")
# %%
(clientes.sort_values(by="qtdePontos", ascending=False)
    .head()["idCliente"])
# %%

teste = pd.DataFrame({
    "nome": ["teo", "ana", "nah", "jose"],
    "idade": [32, 43, 35, 42],
    "salario": [2345, 4533, 3245, 4533],
}
)
teste
# %%

teste.sort_values(by=["salario", "idade"], ascending=[False, True])

# %%
