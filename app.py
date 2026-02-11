def calculate_discount(price, discount):
    # Intentional bug: subtracting instead of multiplying for percentage
    return price - (price - discount) 
