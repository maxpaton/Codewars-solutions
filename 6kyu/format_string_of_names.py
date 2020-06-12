def wave(string):
    
    wave = [string[:i] + string[i:].capitalize() for i in range(len(string)) if string[i] != ' ']
    return wave

wave("hello")