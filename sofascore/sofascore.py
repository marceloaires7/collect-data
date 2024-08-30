# %%
import pandas as pd

# %%

df = (
        pd.read_html('https://fbref.com/en/comps/24/Serie-A-Stats',
                    attrs={"id":"results2024241_overall"})[0]
                    
                    .drop(columns=['Rk', 'Notes'])
     )


df