# BUILDING A LIST - multiple ways
# Method 1: Direct
list1 = [1, 2, 3, 4, 5]
print(f"Direct: {list1}")

# Method 2: Using list() constructor
list2 = list(range(10))
print(f"list(range(10)): {list2}")

# Method 3: List comprehension (MOST IMPORTANT for DE)
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Method 4: From string
chars = list("hello")
print(f"From string: {chars}")

# Method 5: Using split()
sentence = "data,engineering,python"
words = sentence.split(',')
print(f"Using split(): {words}")

# Real DE: Building a partition list
dates = []
for year in [2023, 2024]:
    for month in range(1, 4):
        dates.append(f"year={year}/month={month:02d}")
print(f"Partition paths: {dates}")

# List comprehension version
dates_comp = [f"year={y}/month={m:02d}" for y in [2023,2024] for m in range(1,4)]
print(f"Comprehension: {dates_comp}")

#output
Direct: [1, 2, 3, 4, 5]
list(range(10)): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Squares: [1, 4, 9, 16, 25]
From string: ['h', 'e', 'l', 'l', 'o']
Using split(): ['data', 'engineering', 'python']
Partition paths: ['year=2023/month=01', 'year=2023/month=02', 'year=2023/month=03', 'year=2024/month=01', 'year=2024/month=02', 'year=2024/month=03']
Comprehension: ['year=2023/month=01', 'year=2023/month=02', 'year=2023/month=03', 'year=2024/month=01', 'year=2024/month=02', 'year=2024/month=03']



# SUBSETTING LISTS (Slicing)
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Original: {data}")

# Basic slicing [start:stop:step]
print(f"data[0]: {data[0]}")
print(f"data[-1]: {data[-1]}")
print(f"data[2:6]: {data[2:6]}")
print(f"data[:4]: {data[:4]}")
print(f"data[5:]: {data[5:]}")
print(f"data[::2]: {data[::2]}")  # Every 2nd element
print(f"data[::-1]: {data[::-1]}")  # Reverse

# Real DE: Processing log files
log_lines = [
    "2024-01-01 10:00:00 INFO Job started",
    "2024-01-01 10:00:05 INFO Processing batch 1",
    "2024-01-01 10:00:10 WARN Slow query detected",
    "2024-01-01 10:00:15 INFO Processing batch 2",
    "2024-01-01 10:00:20 ERROR Connection timeout",
    "2024-01-01 10:00:25 INFO Job completed"
]

last_3_logs = log_lines[-3:]
error_logs = [line for line in log_lines if "ERROR" in line]
print(f"\nLast 3 logs: {last_3_logs}")
print(f"Error logs: {error_logs}")

# Slicing for batch processing
chunk_size = 3
for i in range(0, len(data), chunk_size):
    chunk = data[i:i+chunk_size]
    print(f"Batch {i//chunk_size + 1}: {chunk}")

#OUTPUT
Original: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data[0]: 10
data[-1]: 100
data[2:6]: [30, 40, 50, 60]
data[:4]: [10, 20, 30, 40]
data[5:]: [60, 70, 80, 90, 100]
data[::2]: [10, 30, 50, 70, 90]
data[::-1]: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

Last 3 logs: ['2024-01-01 10:00:20 ERROR Connection timeout', '2024-01-01 10:00:25 INFO Job completed']
Error logs: ['2024-01-01 10:00:20 ERROR Connection timeout']

Batch 1: [10, 20, 30]
Batch 2: [40, 50, 60]
Batch 3: [70, 80, 90]
Batch 4: [100]
