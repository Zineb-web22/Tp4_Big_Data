import pandas as pd

path = "/app/data/File.csv"

total_rows = 0
first_chunk = None
chunk_size = 500_000

for chunk in pd.read_csv(path, chunksize=chunk_size):
    if first_chunk is None:
        first_chunk = chunk.head()
        columns = list(chunk.columns)
    total_rows += len(chunk)

print("Rows:", total_rows)
print("Columns:", len(columns))
print(first_chunk)