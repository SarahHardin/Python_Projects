amount = float(input("How much was your bill?: "))

people = float(input("How many people are spliting the bill?: "))

tip = amount * 0.2

total = amount + tip

per_person = total / people

print(f"\nThe tip is: ${tip}\nThe total bill is: ${total}\nEach person owes: ${per_person}")
