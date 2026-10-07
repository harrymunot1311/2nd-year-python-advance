import numpy as np
import pandas as pd

runs = np.array([3200, 4500, 2800, 5100, 6200, 3900, 4800, 5500, 2900, 7000])

print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))

df = pd.DataFrame({
    "Player": [f"Player {i}" for i in range(1, len(runs) + 1)],
    "Runs": runs
})

print("\nDataFrame:")
print(df)

print("\nPlayers scoring more than 5000 runs:")
print(df[df["Runs"] > 5000])
