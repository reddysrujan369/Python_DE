# DICTIONARIES - key-value pairs, O(1) lookup
# Creating dictionaries
empty = {}
user = {"name": "John", "age": 30, "role": "engineer"}
print(f"Empty dict: {empty}")
print(f"User dict: {user}")

# Accessing values
print(f"user['name']: {user['name']}")
print(f"user.get('age'): {user.get('age')}")
print(f"user.get('salary', 'N/A'): {user.get('salary', 'N/A')}")

# Dictionary operations
user['age'] = 31  # Update
user['department'] = 'Data'  # Add new key
print(f"\nAfter update: {user}")

# Get all keys, values, items
print(f"Keys: {user.keys()}")
print(f"Values: {user.values()}")
print(f"Items: {user.items()}")

# Real DE: Configuration management
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "warehouse"
    },
    "batch_size": 10000,
    "retry_attempts": 3,
    "enable_logging": True
}

print(f"\nDatabase host: {config['database']['host']}")
print(f"Batch size: {config['batch_size']}")

##outputt##
Empty dict: {}
User dict: {'name': 'John', 'age': 30, 'role': 'engineer'}
user['name']: John
user.get('age'): 30
user.get('salary', 'N/A'): N/A

After update: {'name': 'John', 'age': 31, 'role': 'engineer', 'department': 'Data'}
Keys: dict_keys(['name', 'age', 'role', 'department'])
Values: dict_values(['John', 31, 'engineer', 'Data'])
Items: dict_items([('name', 'John'), ('age', 31), ('role', 'engineer'), ('department', 'Data')])

Database host: localhost
Batch size: 10000


# BUILDING DICTIONARIES - multiple methods
# Method 1: Curly braces
dict1 = {"a": 1, "b": 2, "c": 3}
print(f"Direct: {dict1}")

# Method 2: dict() constructor
dict2 = dict(name="Alice", age=25, city="NYC")
print(f"dict(): {dict2}")

# Method 3: From list of tuples
pairs = [("x", 10), ("y", 20), ("z", 30)]
dict3 = dict(pairs)
print(f"From tuples: {dict3}")

# Method 4: Dictionary comprehension (MOST USEFUL)
squares = {x: x**2 for x in range(1, 6)}
print(f"Comprehension: {squares}")

# Method 5: Using zip()
keys = ["id", "name", "score"]
values = [101, "Bob", 95.5]
dict4 = dict(zip(keys, values))
print(f"zip(): {dict4}")

# Real DE: Building record mapping
field_mapping = {
    "customer_id": "cust_id",
    "transaction_date": "txn_date", 
    "amount_usd": "amount"
}

source_record = {"customer_id": 1001, "transaction_date": "2024-01-01", "amount_usd": 500.00}
transformed = {field_mapping[k]: v for k, v in source_record.items()}
print(f"\nOriginal: {source_record}")
print(f"Mapped: {transformed}")

# Real DE: Building lookup table
status_map = {
    1: "Pending",
    2: "Processing", 
    3: "Completed",
    4: "Failed"
}

status_codes = [1, 3, 2, 4, 1]
status_names = [status_map[code] for code in status_codes]
print(f"Status codes: {status_codes}")
print(f"Status names: {status_names}")


#OUTPUT
Direct: {'a': 1, 'b': 2, 'c': 3}
dict(): {'name': 'Alice', 'age': 25, 'city': 'NYC'}
From tuples: {'x': 10, 'y': 20, 'z': 30}
Comprehension: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
zip(): {'id': 101, 'name': 'Bob', 'score': 95.5}

Original: {'customer_id': 1001, 'transaction_date': '2024-01-01', 'amount_usd': 500.0}
Mapped: {'cust_id': 1001, 'txn_date': '2024-01-01', 'amount': 500.0}
Status codes: [1, 3, 2, 4, 1]
Status names: ['Pending', 'Completed', 'Processing', 'Failed', 'Pending']


# WORKING WITH DICTIONARIES - common operations
config = {"host": "localhost", "port": 5432, "database": "warehouse"}
print(f"Config: {config}")

# Checking existence
print(f"'host' in config: {'host' in config}")
print(f"'timeout' in config: {'timeout' in config}")

# Safely get with default
timeout = config.get("timeout", 30)
print(f"timeout (default 30): {timeout}")

# Update multiple values
config.update({"port": 5433, "user": "admin"})
print(f"After update: {config}")

# Remove items
removed = config.pop("user")
print(f"Removed 'user': {removed}")
print(f"After pop: {config}")

# Delete item
del config["port"]
print(f"After del: {config}")

# Looping through dictionaries
record = {"id": 101, "name": "Product A", "price": 29.99}
print(f"\nLooping through dict:")
for key, value in record.items():
    print(f"  {key}: {value}")

# Real DE: Data quality check
def validate_record(record, required_fields):
    missing = [field for field in required_fields if field not in record]
    return len(missing) == 0, missing

record = {"id": 1, "name": "John"}
required = ["id", "name", "email"]
is_valid, missing = validate_record(record, required)

print(f"\nRecord: {record}")
print(f"Valid: {is_valid}")
print(f"Missing fields: {missing}")


Config: {'host': 'localhost', 'port': 5432, 'database': 'warehouse'}
'host' in config: True
'timeout' in config: False
timeout (default 30): 30
After update: {'host': 'localhost', 'port': 5433, 'database': 'warehouse', 'user': 'admin'}
Removed 'user': admin
After pop: {'host': 'localhost', 'port': 5433, 'database': 'warehouse'}
After del: {'host': 'localhost', 'database': 'warehouse'}

Looping through dict:
  id: 101
  name: Product A
  price: 29.99

Record: {'id': 1, 'name': 'John'}
Valid: False
Missing fields: ['email']
