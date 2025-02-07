"""
Duck typing is the functionality of a language where "if it looks like a
duck and quacks like a duck, you might as well treat it like a duck." 
This is quite common in interpreted languages. Create a new file named 
task4.py that calculates the final price of a product after applying a 
given discount percentage inside of a function named calculate_discount. 
The function should accept any numeric type for price and discount. 
Write pytest test cases to test the calculate_discount function with
various types (integers, floats) for price and discount.
"""

def calculate_discount(list_price, discount):
    # validate args are within valid bounds for price discount scenario
    if list_price <= 0: 
        raise ValueError("List price must be greater than 0")
    
    if discount < 0:
        raise ValueError("Discount cannot be less than zero")
    elif discount > list_price:
        raise ValueError("Discount cannot be greater than List Price")

    return list_price - discount
    