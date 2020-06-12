def evaporator(content, evap_per_day, threshold):
    
    count = 0  # Keep count for number of days elapsed
    amm_left = content  # Set to constant value
    while content > amm_left*(threshold/100):
        content = content - (content*evap_per_day/100)
        count += 1
    return count

evaporator(10, 10, 10)