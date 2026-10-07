import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

for c in df.select_dtypes(include=np.number):
    df[c] = df[c].fillna(df[c].mean())

for c in df.select_dtypes(include="object"):
    df[c] = df[c].fillna(df[c].mode()[0])

print("\nSummary Statistics:")
print(df.describe())

print("\nAverage Monthly Charges:", np.mean(df["MonthlyCharges"]))
print("Average Tenure:", np.mean(df["Tenure"]))

print("\nChurn Count:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

df["Churn"].value_counts().plot(kind="bar", title="Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Customers")
plt.show()

plt.hist(df["MonthlyCharges"], bins=10)
plt.title("Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Customers")
plt.show()

plt.hist(df["Tenure"], bins=10)
plt.title("Customer Tenure")
plt.xlabel("Tenure")
plt.ylabel("Customers")
plt.show()

pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar")
plt.title("Churn by Contract")
plt.xlabel("Contract")
plt.ylabel("Customers")
plt.show()

df.groupby("Churn")["MonthlyCharges"].mean().plot(kind="bar")
plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Charges")
plt.show()

corr = df.select_dtypes(include=np.number).corr()
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix")
plt.show()
