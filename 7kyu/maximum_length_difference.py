def mxdiflg(a1, a2):
    
    if not a1 or not a2:
        return -1
    
    diff_1 = abs(len(min(a1, key=len)) - len(max(a2, key=len)))
    diff_2 = abs(len(max(a1, key=len)) - len(min(a2, key=len)))
    return max(diff_1, diff_2)

    
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2)