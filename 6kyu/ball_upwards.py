def max_ball(v0):

    v0 = v0*1000/3600 # km/h to m/s
    g = 9.81
    
    h, t = 0, 0
    h_prev, t_prev = 0, 0
    while h >= 0:
        h = v0*t - 0.5*g*t*t
        if h_prev > h:
            return t_prev*10
        h_prev, t_prev = h, t
        t = round(t + 0.1, 2)

max_ball(37)