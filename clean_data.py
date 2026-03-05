import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", None],
    "age": [25, None, 30, 22],
    "city": ["New York", "Chicago", None, "San Francisco"]
}

df = pd.DataFrame(data)

print("Raw Data:")
print(df)

df = df.dropna()

df["age"] = df["age"].astype(int)

print("\nCleaned Data:")
print(df)

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved")