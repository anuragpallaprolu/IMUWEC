#The expression depth counter for GUISE Symblint Package
#Lynch Research Corp.

import numpy as np
def depth_count():
    ops = ['+','-','*','/','^']
    parantheses=['(',')']
    input = raw_input('*')
    j=0
    k=0
    l=0
    processed = np.chararray((len(input),1))
    oplist = []
    parlist = []
    for e in input:
        if e in ops:
            oplist.append(e)
            processed[j,0]=k
            k = k + 1
        else:
            if e in parantheses:
                oplist.append(0)
                parlist.append(e)
                processed[j,0]=l
                l = l + 1
            else:
                processed[j,0]=e
        
        j=j+1
                
    print processed
    print oplist
    print parlist
    return k
    
    
    
while(1):
    print depth_count()
    