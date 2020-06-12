def delete_nth(order, max_e):
    
    new_order = []  # New list to append values of first time occurence
    for i in range(0, len(order)):
        if order[:i].count(order[i]) < max_e:  # Check if current number is in previous numbers (less than max_e times)
            new_order.append(order[i])
    return new_order
    
delete_nth([1,1,3,3,7,2,2,2,2], 3)