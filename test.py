def calculate_total(items):
    total = 0
    for i in range(len(items)):
        total = total + items[i]

    if total > 100:
        print("High total")
    else:
        print("Low total")

    if total > 100:
        print("Again high")  # duplicate condition

    unused_variable = 5

    return total
