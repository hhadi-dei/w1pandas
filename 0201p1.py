import pandas as pd
import pandas as np
#1
df = pd.DataFrame({"Name": ["Jacob", "Emily", "Peter","Camilla","Ulrika","Majd"], "Age": [22, 33, 34, 27, 26, 27], "Score": [123, 223, 132, 111, 321, None]})
#2
df = df.set_index("Name")
#3
df = df[df["Age"] >= 25]
#4
df["Score"] = df["Score"].astype(float)
df2 = df.groupby("Age")["Score"].mean()

#5
mean_score = df["Score"].mean()
df = df.fillna(mean_score)
print(df) 
print(df2)