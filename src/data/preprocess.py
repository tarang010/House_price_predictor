import pandas as pd
df = pd.read_csv("data/raw/house_data.csv")

df = df.drop_duplicates()

df.fillna(df.mean(numberic_only=True), inplace=True)
df.to_csv(
    "data/processed/processed_house_data.csv",
    index=False
)

print("Processing Completed")