def ia(b): 
    
    t = len (b)
    for i in range(t):
    
        if b[i] > b[t-i-1]:
            valeur = b[i]
            return "G"
    
        elif b[i] < b[t-i-1] :
            valeur = b[t-i-1]
            return "D"

 