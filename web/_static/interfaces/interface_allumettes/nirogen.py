def ia(nbAllu):
    AlluARetire = 0
    
    AlluARetire = nbAllu%4
    if AlluARetire == 0:
        AlluARetire = 3
        
        
    if AlluARetire < 0:
        AlluARetire = 1
    
    if nbAllu == 3:
        AlluARetire = 2
    
    nbAllu -= AlluARetire
    
    
    return(AlluARetire)