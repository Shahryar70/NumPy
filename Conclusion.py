import numpy as np
import pandas as pd
df = pd.DataFrame({
    "name":["Shahryar","Hamza","Ali","Abdullah"],
    "Age":[23,34,45,56],
    "Bill":[4000,9000,3400,21000]
})
bill_array = df["Bill"].to_numpy()
print(type(bill_array))
df["BillNorm"]= (df["Bill"] - df["Bill"].min()) / (df["Bill"].min() - df["Bill"].max())
df["BillLog"] = np.log(df["Bill"])
df["AgeSquare"]= np.square(df["Age"])

print(df.round(2))