def find_outlier(integers):

    odd = [i for i in integers if i % 2 != 0]
    even = [i for i in integers if i % 2 == 0]
    
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]

find_outlier([2, 4, 6, 8, 10, 3])