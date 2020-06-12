def likes(names):
    
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return ''.join(names) + ' likes this'
    if len(names) == 2:
        return ' and '.join(names) + ' like this'
    if len(names) == 3:
        return ', '.join(names[0:2]) + ' and ' + names[2] + ' like this'
    if len(names) > 3:
        return ', '.join(names[0:2]) + ' and ' + str(len(names)-2) + ' others like this'
    
likes([])