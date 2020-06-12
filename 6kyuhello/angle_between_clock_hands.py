import math

def hand_angle(hours, minutes):
    
    minute_frac = 2*math.pi/60
    minute_hand = minute_frac*minutes
    
    hour_frac = 2*math.pi/12
    hour_hand = hour_frac*hours + (minute_hand/12)
    
    ang_1 = abs(hour_hand - minute_hand)
    ang_2 = abs((2*math.pi) - abs(hour_hand - minute_hand))
    
    return min(ang_1, ang_2)
    
hand_angle(0, 45)