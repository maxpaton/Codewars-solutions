def find_nb(m):
    
    result = 0
    for i in range(1, int(m**(1/3))+1):
        result = result + i**3
        if result == m:
            return i
        if result > m:
            return -1
    return -1

find_nb(517044411678348009)