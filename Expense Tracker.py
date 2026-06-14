total = 0

while True:
    expense = input("Enter expense (q to quit): ")

    if expense == "q":
        break

    total = total + float(expense)

    print("Current Total =", total)

print("Final Total =", total)