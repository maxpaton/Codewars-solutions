def iq_test(numbers):
    
    num_list = list(map(int, numbers.split(' ')))  # Convert to list of ints
    is_even = [i%2 for i in num_list]  # Convert to binary list depending on evenness
    
    # Return position of number with different evenness (by getting lowest count)
    return is_even.index(min(is_even, key=is_even.count)) + 1
    
# iq_test("2 4 7 8 10")
iq_test("1 1 1 2 1")