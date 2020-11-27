
def getBondPrice_E(face, couponRate, m, yc):
    pv=[]
    for index,value in enumerate(yc):
        pv.append((1+(value))**-(index+1))

    B= face*(sum(pv)*couponRate+pv[-1])

    return(B)
