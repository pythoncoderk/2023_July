import numpy as np
import pandas as pd

s = pd.Series([1,2,np.nan])
print(s)

print(s[0])
print(s.sum())

df = pd.DataFrame({"A":[1,2], "B":[3,4]})
print(df)

print(df.dtypes)