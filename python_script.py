import pandas as pd

def extract(file_path):
    print("Extracting data...")
    return pd.read_csv(file_path)

def transform(df):
    print("Transforming data...")
    df["salary"] = df["salary"] * 1.10
    return df

def load(df, output_path):
    print("Loading data...")
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "employees.csv"
    output_file = "transformed_employees.csv"

    df = extract(input_file)
    df = transform(df)
    load(df, output_file)

    print("ETL process completed successfully")