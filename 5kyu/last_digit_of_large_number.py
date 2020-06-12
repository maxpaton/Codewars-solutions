def last_digit(n1, n2):
    
    product = pow(n1, n2, 10)  # returns pow(x, y) % z, which will get the last integer... (speeds up calc)
    string = str(product)
    
    return int(string)

last_digit(4, 2)