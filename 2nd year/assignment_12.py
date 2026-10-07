import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

print("First 5 records:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nNumber of duplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nAverage Monthly Charges:")
print(np.mean(df["MonthlyCharges"]))

print("\nAverage Customer Tenure:")
print(np.mean(df["Tenure"]))

print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

churn_percentage = df["Churn"].value_counts(normalize=True) * 100

print("\nChurn Percentage:")
print(churn_percentage)

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

plt.hist(df["MonthlyCharges"], bins=10)

plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()

plt.hist(df["Tenure"], bins=10)

plt.title("Distribution of Customer Tenure")
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.show()

contract_churn = pd.crosstab(df["Contract"], df["Churn"])

print("\nChurn based on Contract:")
print(contract_churn)

contract_churn.plot(kind="bar")

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

average_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage Monthly Charges by Churn:")
print(average_charges)

average_charges.plot(kind="bar")

plt.title("Average Monthly Charges vs Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.show()

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")
plt.show()

if "InternetService" in df.columns:
    internet_churn = pd.crosstab(
        df["InternetService"],
        df["Churn"]
    )

    print("\nChurn based on Internet Service:")
    print(internet_churn)

    internet_churn.plot(kind="bar")

    plt.title("Customer Churn by Internet Service")
    plt.xlabel("Internet Service")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=0)
    plt.show()

if "PaymentMethod" in df.columns:
    payment_churn = pd.crosstab(
        df["PaymentMethod"],
        df["Churn"]
    )

    print("\nChurn based on Payment Method:")
    print(payment_churn)

    payment_churn.plot(kind="bar")

    plt.title("Customer Churn by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=45)
    plt.show()

print("\nFinal dataset shape:")
print(df.shape)

print("\nEDA completed successfully.")
