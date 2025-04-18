# %%

import pandas as pd
# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs
# %%

len(dfs)
# %%
dfs[1]
# %%
dfs_uf = dfs[1]
dfs_uf.to_csv("./data/ufs.csv", sep=";")
# %%
