answer = input("Do you want to introduce a new product [y/n]: ")

products = []
i = 1
while answer == 'y':
    name = input("Enter the product name: ")
    cost = float(input("Enter the cost: "))
    amount = float(input("Enter the amount: "))
    measurement = input("Enter the measurement of amount: ")
    prod_tuple = (i, {"name": name, "cost": cost, "amount": amount, "measurement": measurement})
    products.append(prod_tuple)

    answer = input("Do you want to introduce a new product [y/n]: ")
    i += 1

print("\nEntered products:\n", products)


product_analytics = {}
for val in "name", "cost", "amount", "measurement":
    temp = []
    for j in range(len(products)):
        temp.append(products[j][1].get(val))
    product_analytics.update({val: temp})

print("\nProduct analytics:\n", product_analytics)
