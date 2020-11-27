

def getBondPrice(y, face, couponRate, m, ppy=1):
    bond=face*couponRate/ppy*(1-(1+y/ppy)**-(m*ppy))/(y/ppy)+face/(1+y/ppy)**(m*ppy)
    return(bond)
