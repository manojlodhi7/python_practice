import pyarrow.parquet as pq
import s3fs

file = "C:\\Users\\mlodhi\\OneDrive - Nice Systems Ltd\\Desktop\\Python Pract\\python_practice\\PractPackage\\files\\gender.parquet"
pq_data = pq.ParquetDataset(file)
reader = pq_data.read_pandas()
# print(type(reader))
# print(reader)
# print("Row count : ", reader.num_rows)
# print("Column count : ", reader.num_columns)
# print("Column names : ", reader.column_names)
pq_df = reader.to_pandas()
# print("Read data : \n", pq_df)

data = pq_data.read()
# print("Row count : ", data.num_rows)
# print("Column count : ", data.num_columns)
# print("Column names : ", data.column_names)
dataframe = data.to_pandas()
# print("Read data : \n", dataframe)
# print(type(dataframe))
# print(type(pq_df))
# print(dataframe.shape)
# print(pq_df.shape)

# print(pq_df.isnull().any())
# print(pq_df.isna().any())
# print(pq_df.index)
# print(pq_df.columns)
# print(pq_df.GENDER_CD)
# print(pq_df['GENDER_CD'])
# print(pq_df[['GENDER_CD']])

# print("data type of columns : \n", pq_df.dtypes)

tables = pq.read_table(file).to_pandas()
# print(len(tables))
# print(tables)

# for i in range(len(tables)):
#     print(tables[i:i+1])
#
# for i in range(len(tables)):
#     print(tables[i:i+1].columns)

for i in range(len(tables)):
    # print(type(tables[i:i + 1].values))
    print("Row no ", i, " data : ", tables[i:i + 1].values)

print("2D Values : \n", tables.values)
print("Single Value : ", tables.values[0][12])