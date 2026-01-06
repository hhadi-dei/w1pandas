import pandas as pd

df = pd.DataFrame({"Name": ["Jacob", "Emily", "Peter"], "Age": [22, 33, 34], "Score": [123, 223, 132]})
df = df.set_index("Name")
df = df[df["Age"] >= 25]

df["Score"] = df["Score"].astype(float)
print(df) 