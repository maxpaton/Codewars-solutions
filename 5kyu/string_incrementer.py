def increment_string(strng):
    
    # If string has no number at end, add 1
    if strng.isalpha():
        return strng + str(1)
    
    # If string has number at end:
    end_num = re.search(r'(\d*)$', strng).group(0)  # Finds last group of numbers in string
    start = strng[:-len(end_num)]  # Gets everything before last group of numbers
    if end_num:
        filled = str(int(end_num) + 1).zfill(len(end_num))  # Adds 1 to end number whilst preserving leading 0s
        return start + filled
    else:
        return str(1)
        
    
increment_string("foo001")