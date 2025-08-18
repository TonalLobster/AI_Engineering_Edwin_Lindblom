import pandas as pd

# path in python and junyper notebook, you have to import pathlib
from pathlib import Path
DATA_PATH = Path(__file__).parents[2] / "data"

df = pd.read_csv(DATA_PATH /"Sales.csv", index_col=0, parse_dates=True)
print(df.head)
# print(DATA_PATH)