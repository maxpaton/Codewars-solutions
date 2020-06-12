import math

def tankvol(h, d, vt):
    
    # This problem can be broken down into an arc of the tank cross-section, and a triangle 
    # within the arc (sides of len a, b, r)
    
    r = d/2
    
    # Trigonometry
    a = r-h
    theta = math.acos(a/r)  # Angle between vertical and arc meeting top edge of liquid
    b = (r**2 - a**2)**0.5  
    A_tri = 0.5*a*b
    A_arc = 0.5*r**2*theta
    
    A_remain = 2*(A_arc - A_tri) # X2 as have only been working with half the volume of liquid so far
    L = vt/(math.pi*r**2)  # get length of tank
    V_remain = A_remain*L
    
    return math.floor(V_remain)
    
tankvol(40,120,3500)