import json

data = {
    "product" : ["one", "two", "three"],
    "price" : [2.00, 3.00, 4.00]
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

with open("data.json", "r") as json_file:
    data = json.load(json_file)
    totalPrice = 0
    for value in data["price"]:
        totalPrice += value
    currentHigh = 0
    newHigh = 0
    for value in data["price"]:
        newHigh = value
        if newHigh > currentHigh:
            currentHigh = newHigh
            newHigh = 0
    indexOfHigh = data["price"].index(currentHigh)
    mostExpensive = data["product"][indexOfHigh]
    print(f"Total Price: {totalPrice}")
    print(f"Most Expensive Item: {mostExpensive}")