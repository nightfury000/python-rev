def cost1():
    price = 100
    print("The price is ", price)

# in this example the price is defined in only the cost1 function but not cost2 so its lifetime is limited to cost1 
def cost2():
    print("The price is ", price)

cost1()
cost2()
