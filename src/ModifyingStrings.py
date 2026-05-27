# MULTI-LINE STRINGS
# SQL query (most common use case)
sql_query = """
SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(amount) as total_spent
FROM orders
WHERE created_at >= '2024-01-01'
GROUP BY customer_id
ORDER BY total_spent DESC;
"""
print(sql_query)

# JSON payload
json_payload = '''
{
    "event_type": "data_quality_check",
    "metrics": {
        "null_count": 0,
        "duplicate_count": 12
    }
}
'''
print(json_payload)

# Real DE example: Dynamic SQL generator
def generate_query(table, date_col, start_date, end_date):
    return f"""
    SELECT * FROM {table}
    WHERE {date_col} BETWEEN '{start_date}' AND '{end_date}';
    """

query = generate_query("sales_facts", "txn_date", "2024-01-01", "2024-01-31")
print(query)




# STRINGS ARE IMMUTABLE - each modification creates new string
original = "data_engineering"
print(f"Original: {original} (ID: {id(original)})")

modified = original.replace("data", "big_data")
print(f"Modified: {modified} (ID: {id(modified)})")
print(f"Original unchanged: {original}")

# Common string methods
text = "  2024-01-15_RAW_DATA.CSV  "
print(f"\nOriginal: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lower(): '{text.lower()}'")
print(f"upper(): '{text.upper()}'")
print(f"replace('_', '-'): '{text.replace('_', '-')}'")
print(f"split(): {text.strip().split('_')}")

# join() - fast string concatenation
words = ['data', 'lake', 'partition']
print(f"join(): {'-'.join(words)}")

# Real DE: Data masking
def mask_email(email):
    parts = email.split('@')

    if len(parts) != 2:
        return email

    username, domain = parts

    if len(username) <= 2:
        masked = username[0] + '*'
    else:
        masked = username[0] + '*' * (len(username) - 2) + username[-1]

    return masked + '@' + domain

print(f"\nMasked email: {mask_email('john.doe@company.com')}")
