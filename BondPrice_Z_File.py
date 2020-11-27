

def getBondPrice_Z(face, couponRate, times, yc):
    pv=[]
    for index,value in enumerate(yc):
        pv.append((1+(value))**-times[index])
        
    B= face*(sum(pv)*couponRate+pv[-1])
    
    return(B)
