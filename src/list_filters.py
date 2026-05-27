orders = [
    {"order_id":1, "country":"US"},
    {"order_id":2, "country":"IN"},
    {"order_id":3, "country":"IN"},
]

in_order = []

for order in orders:
    if order["country"] == "IN":
        in_order.append(order)

print(in_order)

#in_order = [order for order in orders if order["country"] == "IN"]