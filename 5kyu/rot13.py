def rot13(message):
    converted = []
    for i in message:
        if ord(i) >= 97 and ord(i) <= 122:
            unic = ord(i) + 13
            if unic > 122:
                unic = unic - 26
            converted.append(chr(unic))
        elif ord(i) >= 65 and ord(i) <= 90:
            unic = ord(i) + 13
            if unic > 90:
                unic = unic - 26
            converted.append(chr(unic))
        else:
            converted.append(i)
    return ''.join(converted)

rot13("grfgGrfg")