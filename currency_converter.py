transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21, 11.22, 33.44, 55.66, 77.88, 99.00 ]

transactions_usd = []

i = 0

while i <= len(transactions_aed) - 1:
    item_usd = transactions_aed[i] * 0.27
    print("Converting value", transactions_aed[i])
    transactions_usd.append(item_usd)
    i += 1


for item in transactions_aed:
    item_usd = item * 0.27
    transactions_usd.append(item_usd)


print(transactions_usd)