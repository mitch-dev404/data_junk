# calculate how much money was spent on items costing $5 or more

prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

spent = {}

money_spent = 0

for key, value in prices.items():
    if value < 5:
        spent[key] = value

for key, value in quantity.items():
    if key in spent:
        spent[key] = spent[key] * value

for key, value in spent.items():
    money_spent += value

print(money_spent)