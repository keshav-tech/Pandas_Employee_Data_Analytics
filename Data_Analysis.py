import pandas as pd
import numpy as np

data = {
"Name": ["Alice","Bob","Charlie","David","Eva"],
"Age": [25,30,35,28,40],
"City": ["NY","London","Paris","NY","London"],
"Salary": [50000,60000,70000,55000,80000],
"JoiningDate": ["2020-01-15","2019-07-22","2021-03-10","2020-12-05","2018-06-30"]
}
df = pd.DataFrame(data)
print(df)

print(df.head())

print(df.shape)

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df["City"].unique())

df["Experience"] = [5,7,3,4,10]
df["Salary"] = df["Salary"] * 1.1
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)



df.sort_values(by="Salary", ascending=False, inplace=True)
df.set_index("Name", inplace=True)
print(df)

df["AgeGroup"] = pd.cut(df["Age"], bins=[0,25,35,50], labels=["Young","Adult","Senior"])
df["SalaryCategory"] = df["Salary"].apply(lambda x: "High" if x>60000 else "Low")
df["SalaryK"] = df["Salary"].apply(lambda x: x/1000)
print(df)

pivot = df.pivot_table(
    values="Salary", 
    index="City", 
    columns="AgeGroup", 
    aggfunc="mean", 
    observed=False  # keep current behavior
)
print(pivot)


scores = pd.DataFrame({"Name":["Alice","Bob","Charlie"],"Score":[90,85,95]})
df_merged = pd.merge(df.reset_index(), scores, on="Name", how="left")
new_employees = pd.DataFrame({
"Name":["Frank","Grace"],
"Age":[29,33],
"City":["Paris","NY"],
"Salary":[60000,65000],
"JoiningDate":["2022-02-10","2021-05-12"],
"Experience":[2,5]
})
df_final = pd.concat([df_merged, new_employees], ignore_index=True)
print(df_final)

if 'JoiningDate' not in df_final.columns:
    df_final.reset_index(inplace=True)
df_final['JoiningDate'] = pd.to_datetime(df_final['JoiningDate'])
df_final.set_index('JoiningDate', inplace=True)
monthly_salary = df_final['Salary'].resample('ME').sum()
print(monthly_salary)


df_encoded = pd.get_dummies(df_final, columns=["City"])
df_encoded["AgeGroupCode"] = df_encoded["AgeGroup"].astype("category").cat.codes
print(df_encoded)

X = df_encoded[["Age","Salary","Experience","AgeGroupCode"]].values
y = df_encoded["Score"].fillna(0).values
numeric_df = df_encoded.select_dtypes(include=np.number)
print(numeric_df.corr())
print("\nX shape:", X.shape, "y shape:", y.shape)