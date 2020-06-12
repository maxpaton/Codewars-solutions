import time

def expanded_form(num):
    
    nums = []
    for i in range(len(str(num))):
        exp_form = int(str(num)[-(i+1)])*10**i
        if exp_form != 0:
            nums.append(exp_form)
    
    return ' + '.join(str(n) for n in reversed(nums))

expanded_form(70304)