import os
import pandas as pd

OUTPUT_FILE = "transformed_employees.csv"


def test_file_exists():
    assert os.path.exists(OUTPUT_FILE), "Transformed file was not created"


def test_net_salary_column_exists():
    df = pd.read_csv(OUTPUT_FILE)
    assert "net_salary" in df.columns


def test_net_salary_calculation():
    df = pd.read_csv(OUTPUT_FILE)
    for _, row in df.iterrows():
        expected_net = row["salary"] - (row["salary"] * 0.10)
        assert abs(row["net_salary"] - expected_net) < 0.01


def test_salary_not_null():
    df = pd.read_csv(OUTPUT_FILE)
    assert df["salary"].isnull().sum() == 0