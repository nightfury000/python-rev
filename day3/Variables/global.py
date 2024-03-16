price = 100

def cost1():
    
    print("The price is ", price)

# in this example the price is defined outside the functions hence it is accessible everywhere
def cost2():
    print("The price is ", price)

cost1()
cost2()
