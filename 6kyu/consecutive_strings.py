def longest_consec(strarr, k):
    
    result = ''  # If conditions aren't met, will return ''. Also serves at initialiser
    
    # Initial checks
    if k > 0 and len(strarr) > 0:
        
        for i in range(len(strarr)-(k-1)):
            concats = ''.join(strarr[i:i+k])  # concatenate consecutive k strings
            if len(concats) > len(result):  # keeps track of longest concatenation
                result = concats           
    return result

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)