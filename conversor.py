# %%

import pandas as pd

dt = pd.read_csv("funcionarios.csv")
# %%
dt.head()
# %%
dt.sample()
# %%
dt.to_excel("funcionarios.xlsx", index=False)
# %%
