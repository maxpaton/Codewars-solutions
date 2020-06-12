# Inputs just one number 'a'
# Returns sum of each integer of 'a' to its consecutive power
def consec_pow_sum(a):
    return sum(int(y)**x for x, y in enumerate(str(a), 1))

# computes dig_pow on each number of input range, and check if sum is equal to original number
def sum_dig_pow(a, b):
    return [i for i in range(a, b+1) if consec_pow_sum(i) == i]    
        
sum_dig_pow(1, 90)