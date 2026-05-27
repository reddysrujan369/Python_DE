# WORKING WITH STRINGS
file_path = '/data/warehouse/customers.csv'
table_name = "user_events"
print(f"File path: {file_path}")
print(f"Table name: {table_name}")

# String concatenation
prefix = "/data/"
suffix = "transactions.parquet"
full_path = prefix + suffix
print(f"Full path: {full_path}")

# String formatting (f-strings)
batch_id = 1001
record_count = 5432
status = f"Batch {batch_id} processed {record_count} records"
print(f"Status: {status}")

# String methods for cleaning
raw_string = "  RAW_DATA_2024.CSV  "
cleaned = raw_string.strip()
lowercase = cleaned.lower()
extension = cleaned.split('.')[-1]
print(f"Original: '{raw_string}'")
print(f"Cleaned: '{cleaned}'")
print(f"Lowercase: '{lowercase}'")
print(f"Extension: '{extension}'")

# Real DE example: Parsing S3 path
s3_path = "s3://data-lake-prod/year=2024/month=05/day=27/events.jsonl"
bucket = s3_path.split('/')[2]
filename = s3_path.split('/')[-1]
print(f"Bucket: {bucket}")
print(f"Filename: {filename}")
print(f"Is JSONL? {s3_path.endswith('.jsonl')}")

#output 
File path: /data/warehouse/customers.csv
Table name: user_events
Full path: /data/transactions.parquet
Status: Batch 1001 processed 5432 records
Original: '  RAW_DATA_2024.CSV  '
Cleaned: 'RAW_DATA_2024.CSV'
Lowercase: 'raw_data_2024.csv'
Extension: 'CSV'
Bucket: data-lake-prod
Filename: events.jsonl
Is JSONL? True
