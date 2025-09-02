# Pandas_Employee_Data_Analytics


# Data Analysis Project

This repository contains a Python script performing basic data analysis using Pandas and NumPy. Below are the code snippets with their respective outputs.

---

## 1. Creating DataFrame


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


**Output:**

```
      Name  Age    City  Salary JoiningDate
0    Alice   25      NY   50000  2020-01-15
1      Bob   30  London   60000  2019-07-22
2  Charlie   35   Paris   70000  2021-03-10
3    David   28      NY   55000  2020-12-05
4      Eva   40  London   80000  2018-06-30
```

---

## 2. Basic Exploration


print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["City"].unique())


**Output:**

```
      Name  Age    City  Salary JoiningDate
0    Alice   25      NY   50000  2020-01-15
1      Bob   30  London   60000  2019-07-22
2  Charlie   35   Paris   70000  2021-03-10
3    David   28      NY   55000  2020-12-05
4      Eva   40  London   80000  2018-06-30

(5, 5)


RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Name         5 non-null      object
 1   Age          5 non-null      int64
 2   City         5 non-null      object
 3   Salary       5 non-null      int64
 4   JoiningDate  5 non-null      object
dtypes: int64(2), object(3)
memory usage: 332.0+ bytes
None

            Age        Salary
count   5.00000      5.000000
mean   31.60000  63000.000000
std     5.94138  12041.594579
min    25.00000  50000.000000
25%    28.00000  55000.000000
50%    30.00000  60000.000000
75%    35.00000  70000.000000
max    40.00000  80000.000000

Name           0
Age            0
City           0
Salary         0
JoiningDate    0
dtype: int64

['NY' 'London' 'Paris']
```

---

## 3. Updating Data

df["Experience"] = [5,7,3,4,10]
df["Salary"] = df["Salary"] * 1.1
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)


**Output:**

```
      Name  Age    City   Salary JoiningDate  Experience
0    Alice   25      NY  55000.0  2020-01-15           5
1      Bob   30  London  66000.0  2019-07-22           7
2  Charlie   35   Paris  77000.0  2021-03-10           3
3    David   28      NY  60500.0  2020-12-05           4
4      Eva   40  London  88000.0  2018-06-30          10
```

---

## 4. Sorting and Indexing


df.sort_values(by="Salary", ascending=False, inplace=True)
df.set_index("Name", inplace=True)
print(df)


**Output:**

```
         Age    City   Salary JoiningDate  Experience
Name
Eva       40  London  88000.0  2018-06-30          10
Charlie   35   Paris  77000.0  2021-03-10           3
Bob       30  London  66000.0  2019-07-22           7
David     28      NY  60500.0  2020-12-05           4
Alice     25      NY  55000.0  2020-01-15           5
```

---

## 5. Categorization and Salary Buckets


df["AgeGroup"] = pd.cut(df["Age"], bins=[0,25,35,50], labels=["Young","Adult","Senior"])
df["SalaryCategory"] = df["Salary"].apply(lambda x: "High" if x>60000 else "Low")
df["SalaryK"] = df["Salary"].apply(lambda x: x/1000)
print(df)


**Output:**

```
         Age    City   Salary JoiningDate  Experience AgeGroup SalaryCategory  SalaryK
Name
Eva       40  London  88000.0  2018-06-30          10   Senior           High     88.0
Charlie   35   Paris  77000.0  2021-03-10           3    Adult           High     77.0
Bob       30  London  66000.0  2019-07-22           7    Adult           High     66.0
David     28      NY  60500.0  2020-12-05           4    Adult           High     60.5
Alice     25      NY  55000.0  2020-01-15           5    Young            Low     55.0
```

---

## 6. Pivot Table


pivot = df.pivot_table(
    values="Salary", 
    index="City", 
    columns="AgeGroup", 
    aggfunc="mean", 
    observed=False
)
print(pivot)


**Output:**

```
AgeGroup    Young    Adult   Senior
City
London        NaN  66000.0  88000.0
NY        55000.0  60500.0      NaN
Paris         NaN  77000.0      NaN
```

---

## 7. Merging and Concatenation


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


**Output:**

```
      Name  Age    City   Salary JoiningDate  Experience AgeGroup SalaryCategory  SalaryK  Score
0      Eva   40  London  88000.0  2018-06-30          10   Senior           High     88.0    NaN
1  Charlie   35   Paris  77000.0  2021-03-10           3    Adult           High     77.0   95.0
2      Bob   30  London  66000.0  2019-07-22           7    Adult           High     66.0   85.0
3    David   28      NY  60500.0  2020-12-05           4    Adult           High     60.5    NaN
4    Alice   25      NY  55000.0  2020-01-15           5    Young            Low     55.0   90.0
5    Frank   29   Paris  60000.0  2022-02-10           2      NaN            NaN      NaN    NaN
6    Grace   33      NY  65000.0  2021-05-12           5      NaN            NaN      NaN    NaN
```

---

## 8. Resampling Monthly Salary


if 'JoiningDate' not in df_final.columns:
    df_final.reset_index(inplace=True)
df_final['JoiningDate'] = pd.to_datetime(df_final['JoiningDate'])
df_final.set_index('JoiningDate', inplace=True)
monthly_salary = df_final['Salary'].resample('ME').sum()
print(monthly_salary)


**Output:**

```
JoiningDate
2018-06-30    88000.0
2018-07-31        0.0
2018-08-31        0.0
...
2022-02-28    60000.0
Freq: ME, Name: Salary, dtype: float64
```

---

## 9. Encoding and Correlation

df_encoded = pd.get_dummies(df_final, columns=["City"])
df_encoded["AgeGroupCode"] = df_encoded["AgeGroup"].astype("category").cat.codes
print(df_encoded)

X = df_encoded[["Age","Salary","Experience","AgeGroupCode"]].values
y = df_encoded["Score"].fillna(0).values
numeric_df = df_encoded.select_dtypes(include=np.number)
print(numeric_df.corr())
print("\nX shape:", X.shape, "y shape:", y.shape)


**Output:**

```
                Name  Age   Salary  Experience AgeGroup SalaryCategory  SalaryK  Score  City_London  City_NY  City_Paris  AgeGroupCode
JoiningDate
2018-06-30       Eva   40  88000.0          10   Senior           High     88.0    NaN         True    False       False             2
2021-03-10   Charlie   35  77000.0           3    Adult           High     77.0   95.0        False    False        True             1
2019-07-22       Bob   30  66000.0           7    Adult           High     66.0   85.0         True    False       False             1
2020-12-05     David   28  60500.0           4    Adult           High     60.5    NaN        False     True       False             1
2020-01-15     Alice   25  55000.0           5    Young            Low     55.0   90.0        False     True       False             0
2022-02-10     Frank   29  60000.0           2      NaN            NaN      NaN    NaN        False    False        True            -1
2021-05-12     Grace   33  65000.0           5      NaN            NaN      NaN    NaN        False     True       False            -1

                   Age    Salary  Experience   SalaryK  Score  AgeGroupCode
Age           1.000000  0.966717    0.543949  0.999389    0.5      0.491822
Salary        0.966717  1.000000    0.602279  1.000000    0.5      0.675730
Experience    0.543949  0.602279    1.000000  0.546177   -1.0      0.636396
SalaryK       0.999389  1.000000    0.546177  1.000000    0.5      0.880830
Score         0.500000  0.500000   -1.000000  0.500000    1.0      0.000000
AgeGroupCode  0.491822  0.675730    0.636396  0.880830    0.0      1.000000

X shape: (7, 4) y shape: (7,)
```


