import pandas as pd
from datetime import datetime

def log(message):
    with open("logs/pipeline.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

try:
    log("Pipeline started")

    # Extract
    df = pd.read_csv("data/sales.csv")
    log("Data extracted successfully")

    # Validation
    if df.empty:
        raise Exception("Input file is empty")

    if df["customer_name"].isnull().sum() > 0:
        log("Warning: Missing customer names found")

    if (df["amount"] < 0).sum() > 0:
        log("Warning: Negative amounts found")

    # Transform
    df_clean = df.drop_duplicates()

    # Remove bad records
    df_clean = df_clean.dropna(subset=["customer_name"])
    df_clean = df_clean[df_clean["amount"] >= 0]

    log("Data cleaned successfully")

    # Load
    df_clean.to_csv("data/clean_sales.csv", index=False)

    log("Output file created")
    log("Pipeline completed successfully")

    print("ETL Completed Successfully!")

except Exception as e:
    log(f"Pipeline failed: {str(e)}")
    print("Error:", e)