

def getBondPrice(y, face, couponRate, m, ppy=1):
    bond=face*couponRate/yc*(1-(1+y/yc)**-(m*yc))/(y/yc)+face/(1+y/yc)**(m*yc)
    return(bond)
