import csv
import pandas as pd
df = pd.read_csv("data/raw/CICIDS2017.csv")
print(df[" Label"].unique())