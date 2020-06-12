import regex as re

def decipher_this(string):
    
    numbers = re.findall(r'\d+', string)  # Find list of numbers
    for i in numbers:
        string = string.replace(i, chr(int(i)))  # Replace each number with character code
    string = string.split(' ')
    
    # For words with more than two letters, was 2nd and last letters
    result = [i[0] + i[-1] + i[2:-1] + i[1] if len(i) > 2 else i for i in string]
    
    return ' '.join(result)

decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka')