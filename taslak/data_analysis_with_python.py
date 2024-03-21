import pandas as pd
import seaborn as sns

df=sns.load_dataset("titanic")
print(df.pivot_table("survived","sex",["embarked","class"]))


df["new_age"] = pd.cut(df["age"],[0,10,18,25,40,90])
print (df ["new_age"] )



print(df.pivot_table("survived","sex","new_age"))