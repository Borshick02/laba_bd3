import pandas as pd
import psycopg2
import duckdb
import timeit
import statistics
import json

# Чтение конфигурационного файла
with open('benchmarkconfig.json', 'r') as f:
    config = json.load(f)

df = pd.read_csv(config["input_data_file"])

con = duckdb.connect(database=':memory:')
con.register('data', df)


con = duckdb.connect(database=':memory:')
con.register('data', df)

def execute_query_duckdb(query):
    query_times = []
    for _ in range(10):
        start_time = timeit.default_timer()
        result = con.execute(query).fetchdf()
        elapsed = timeit.default_timer() - start_time
        query_times.append(elapsed)
    median_time = statistics.median(query_times)
    return median_time

# Выполнение запросов и измерение времени выполнения для DuckDB
for query in config["queries"]:
    query_time = execute_query_duckdb(query)
    print(f"DuckDB Query: {query}")
    print(f"Median Time: {query_time} seconds")



def execute_query_sqlite(query):
    query_times = []
    for _ in range(10):
        start_time = timeit.default_timer()

        elapsed = timeit.default_timer() - start_time
        query_times.append(elapsed)
    median_time = statistics.median(query_times)
    return median_time

for query in config["queries"]:
    query_time = execute_query_sqlite(query)
    print(f"SQLite Query: {query}")
    print(f"Median Time: {query_time} seconds")


def execute_query_pandas(query):
    query_times = []
    for _ in range(10):
        start_time = timeit.default_timer()
        result = df.groupby('VendorID').size().reset_index(name='counts')  # Здесь мы используем метод groupby и size для выполнения запроса
        elapsed = timeit.default_timer() - start_time
        query_times.append(elapsed)
    median_time = statistics.median(query_times)
    return median_time

for query in config["queries"]:
    query_time = execute_query_pandas(query)
    print(f"Pandas Query: {query}")
    print(f"Median Time: {query_time} seconds")

