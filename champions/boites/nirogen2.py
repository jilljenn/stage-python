def ia(b): 
    
    t = len (b)
    for i in range(t):
    
        if b[i] > b[t-i-1]:
            if b[i] > b[i+1]:
                return "G"
    
        elif b[i] < b[t-i-1] :
            if b[t-i-1] > b[t-i-2] : 
                return "D"