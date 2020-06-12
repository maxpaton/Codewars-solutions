def kebabize(string):

    kebab = ['-' + i.lower() if i.isupper() else i for i in string if i.isalpha()]
    result = ''.join(kebab).strip('-')
            
    return result
    
kebabize('SOS')