def find_uniq(arr):

    n = min(set(arr), key = arr.count)
    
    return n  # n: unique integer in the array

find_uniq([3,1,1,1,1,1])