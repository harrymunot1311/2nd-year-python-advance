import numpy as np
import pandas as pd

bills = np.array([1200, 2500, 3200, 1800, 4500, 2900, 3500, 2100, 5000, 2700])

print("Mean:", np.mean(bills))
print("Median:", np.median(bills))
print("Maximum:", np.max(bills))
print("Minimum:", np.min(bills))

df = pd.DataFrame({
    "Consumer": [f"Consumer {i}" for i in range(1, len(bills) + 1)],
    "Bill": bills
})

print("\nDataFrame:")
print(df)

print("\nConsumers whose bill exceeds ₹3000:")
print(df[df["Bill"] > 3000])
