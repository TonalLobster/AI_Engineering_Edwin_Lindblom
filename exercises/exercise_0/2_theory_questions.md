# Theory Questions

## Questions to answer

  a) Why could it be good to combine duckdb and pandas?

  b) How do you create a DataFrame in Pandas from a dictionary, a list of dictionaries, and a CSV file, json object?

  c) What is the difference between .loc[] and .iloc[] for indexing in Pandas?

  d) What is the purpose of the .groupby() method in Pandas? How is it used in data aggregation?

  e) How do you export a pandas dataframe into a csv file?

  f) How do you save a pandas dataframe into a duckdb database?


## Answers
a)
Duckdb makes it easier for you to search through databases wwith the help of sql queries, which makes you write a less redundant code. you can also run duckdb directly in Pandas DataFrames so you dont have to export the data.


b)
import pandas as pd
From a dictionary:
  df1 = pd.DataFrame({"name": ["John", "Jane"], "age": [25, 30]})
From a list of dictionaries:
  df2 = pd.DataFrame([{"name": "John", "age": 25}, {"name": "Jane", "age": 30}])
From a CSV file:
  df3 = pd.read_csv("data.csv")
From a JSON object:
  df4 = pd.read_json("data.json")


c)
.loc[] uses label-based indexing(ex. "name"), while .iloc[] uses integer(numbers)-based indexing.


d)
.groupby() is used to group data by one or more columns, and then appy aggregation functions like sum, mean, count etc.
example:
df.groupby("category")["sales"].sum()


e)
df.to_csv("new_data.csv", index=False)


f)
import duckdb

Connect to a DuckDB database file
  conn = duckdb.connect("my_database.duckdb")

Save the DataFrame as a table
  conn.execute("CREATE TABLE IF NOT EXISTS my_table AS SELECT * FROM df")




