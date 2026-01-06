import pandas as pd
import pandas as np
#P1
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
#P2
#1
df3 = pd.DataFrame({"Name":["Melina", "Sara", "Oscar", "Driton", "Potato", "Karin"], "Age":[23, 25, 44, 34, 53, 52], "Occupation": ["Welder", "Carpenter", "Engineer", "Doctor", "Service", "COO"]})
df5 = pd.concat([df, df3], axis = 0)
#2
id_df1 = pd.DataFrame({"ID": [1, 2, 3], "Name":["Adam", "Emmelie", "Julia"], "Age": [32, 22, 23]})
id_df2 = pd.DataFrame({"ID":[1, 2, 3], "Name": ["Karolin", "Peter", "Charles"], "Age": [31, 25, 29]})

id_merge_df = pd.merge(id_df1, id_df2, on='ID')
#print(df) 
#print(df3)
#print(df5)

print(id_df1)
print(id_df2)
print(id_merge_df)