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
#6
df3 = pd.DataFrame({"Name":["Melina", "Sara", "Oscar", "Driton", "Potato", "Karin"], 
                    "Age":[23, 25, 44, 34, 53, 52], 
                    "Occupation": ["Welder", "Carpenter", "Engineer", "Doctor", "Service", "COO"]})

df5 = pd.concat([df, df3], axis = 0)
#7
id_df1 = pd.DataFrame({"ID": [1, 2, 3], 
                       "Name":["Adam", "Emmelie", "Julia"], 
                       "Age": [32, 22, 23]})

id_df2 = pd.DataFrame({"ID":[1, 2, 3], 
                       "Name": ["Karolin", "Peter", "Charles"], 
                       "Age": [31, 25, 29]})

id_merge_df = pd.merge(id_df1, id_df2, on='ID', how="outer")

#8
df_datetime = pd.DataFrame({"Date":['2002-02-03', '2033-12-31', '2012-05-04']})
df_datetime["Date"] = pd.to_datetime(df_datetime["Date"])
#9
df_eventtime = df_datetime.rename(columns={"Date":"EventTime"})

#10

df_unique = pd.DataFrame({"Values": [1, 2, 1, 1 , 3, 4, 4 , 4]})

print(df_unique)
df_unique = df_unique.drop_duplicates()
print(df_unique)
#print(df)  
#print(df3)
#print(df5)
#print(id_df1)
#print(id_df2)
#print(id_merge_df)
#print(df_eventtime)