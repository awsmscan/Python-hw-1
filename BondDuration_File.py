

def getBondDuration(y, face, couponRate, m, ppy = 1):
    year=[]
    pvcf=[]
    pvcf_t=[]
    spvcf=[]
    for i in range(m):
        year.append(i+1)
        pv= (1+y)**-(i+1)
        if i+1==m :
            cf=face+face*couponRate
        else:
            cf=face*couponRate
        pvcf.append( pv*cf )

    for j in range(len(pvcf)):
        
        pvcf_t.append(pvcf[j]*year[j])
        j+=1


    pvcfandt=sum(pvcf_t)
    spvcf=sum(pvcf)
    duration=pvcfandt/spvcf
    
    return(duration)
    
