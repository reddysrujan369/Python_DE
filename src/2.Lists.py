# LISTS - mutable, ordered, allows duplicates
numbers = [1, 2, 3, 4, 5]
mixed = [1, "string", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slicing [1:3]: {numbers[1:3]}")

# List operations (mutable)
batch_ids = [1001, 1002, 1003]
print(f"\nOriginal: {batch_ids}")

batch_ids.append(1004)
print(f"append(1004): {batch_ids}")

batch_ids.insert(1, 1500)
print(f"insert(1,1500): {batch_ids}")

batch_ids.remove(1500)
print(f"remove(1500): {batch_ids}")

popped = batch_ids.pop()
print(f"pop(): {batch_ids} (removed: {popped})")

batch_ids[0] = 9999
print(f"modify index 0: {batch_ids}")

# Real DE: Batch processor
buffer = []
for i in range(1, 6):
    buffer.append(f"record_{i}")
    print(f"Buffer: {buffer}")
print(f"\nFinal batch: {buffer}")
buffer.clear()
print(f"After clear(): {buffer}")


#OUTPUT
Numbers: [1, 2, 3, 4, 5]
Mixed: [1, 'string', 3.14, True]
Nested: [[1, 2], [3, 4], [5, 6]]
First element: 1
Last element: 5
Slicing [1:3]: [2, 3]

Original: [1001, 1002, 1003]
append(1004): [1001, 1002, 1003, 1004]
insert(1,1500): [1001, 1500, 1002, 1003, 1004]
remove(1500): [1001, 1002, 1003, 1004]
pop(): [1001, 1002, 1003] (removed: 1004)
modify index 0: [9999, 1002, 1003]
Buffer: ['record_1']
Buffer: ['record_1', 'record_2']
Buffer: ['record_1', 'record_2', 'record_3']
Buffer: ['record_1', 'record_2', 'record_3', 'record_4']
Buffer: ['record_1', 'record_2', 'record_3', 'record_4', 'record_5']

Final batch: ['record_1', 'record_2', 'record_3', 'record_4', 'record_5']
After clear(): []

