def series_sum(n):
    
    x = 0
    
    for i in range(0, n):
        x += 1/(1 + 3*i)
    return '%.2f' % x

series_sum(5)