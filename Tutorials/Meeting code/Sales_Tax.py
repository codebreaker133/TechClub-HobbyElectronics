

def Sales_Tax():
    price = input("what is the price of the item? ")
    tax = 0.0825
    total_price = price + (price*tax)
    print(total_price)
    
Sales_Tax()