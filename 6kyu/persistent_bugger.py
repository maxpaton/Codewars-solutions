def persistence(n):
     
    count = 0  # keep track of number of multiplication persistances
    while len(str(n)) > 1:  # Do until left with one digit
        product = 1
        for i in range(len(str(n))):
            product *= int(str(n)[i])  # Multiply each digit in number
        n = product  # Return result to while condition
        count += 1

    return count
    
persistence(999)