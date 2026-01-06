import pandas as pd

#2. Rename columns not to have any whitespaces or special characters.
#3. For all persons under the age of 18, set "sex" column value to be "child“.
#4. Create a new DataFrame which displays the average fare per sex.
#5. Create a new DataFrame which displays the average fare per sex and Pclass.
#6. Create a new DataFrame which displays the average fare per survived column.
#7. Split the DataFrame into 3 DataFrame based on the sex column. So, one for male, another for female 
#and third for child. How many records does each dataset have?
#8. Create a new DataFrame that only includes Pclass, Name and age, for those persons that had 
#siblings, spouses, parents or children aboard.
#9. Filter off those persons who had both siblings/spouses AND parents/children.
#10. What is the average fare paid by the people in the DataFrame from last step?



df = pd.read_csv("titanic.csv")
df.columns = df.columns.str.replace(' ', '_')

df.loc[df['Age'] > 18, "Sex"] = "child"
print(df)

