def longest_palindrome (s):
    
    if not s:
        return 0
    
    palins = []
    for i in range(len(s)):
        for j in range(len(s)):
            orig = s[i:i+j+1]  # We are iterating through all possible palindromes, taking slices of each one
            if orig == orig[::-1]:  # Check if equals reverse
                palins.append(len(orig))
    return max(palins)
    
longest_palindrome("bab")