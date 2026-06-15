import pandas as pd

df = pd.read_csv("data/clean_sales.csv")

print("\nPipeline Report")
print("----------------")
print("Total Records:", len(df))
print("Total Sales:", df["amount"].sum())
print("Average Sale:", round(df["amount"].mean(), 2))
