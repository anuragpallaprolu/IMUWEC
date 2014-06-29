#count_pattern
#auxiliary program for the GUISE Math System
#PRiMAC: PatteRnIng Matcher on ACid

i=0
j=0

def list_compare(list1,list2):
    matches = 0
    if len(list1)!=len(list2):
        return 0
        #Non comparable lists
    else:
        for i in range(len(list1)):
            if list1[i] == list2[i]:
               matches = 1 
            else:
                matches = 0
    
    return matches

def count_pat(pat, mainlist):
    global i,j
    
    c=0
    h=0
    while h+len(pat)<=len(mainlist):
        new_list = []
        for i in range(h,h+len(pat)):
            new_list.append(mainlist[i])
            print new_list
        if list_compare(new_list,pat)==1:
            print 'Heres the list'
            print new_list
            print 'Comparison Done!'
            ++c
            print c
            h = h + 1
        else:
            'Jumped to Else!'
            h = h + 1
    
    
    return c


pat = ['x','*','x','+','1']
listed = ['x', '*', 'x', '+', '1', 'x', '*', 'x', '+', '1', '1', '*', 'x', '*', 'x', 'x', '*', 'x', '+', '1', 'x', '*', 'x', '+', '1', '1', '*', 'x', '*', 'x', 'x', '+', '2', 'x', '*', 'x', '+', '1', 'x', '*', 'x', '+', '1', '1', '*', 'x', '*', 'x', 'x', '*', 'x', '+', '1', 'x', '*', 'x', '+', '1', '1', '*', 'x', '*', 'x', 'x', '+', '2', '2']

print count_pat(pat, listed)

pat2 = ['a','c','b']

print list_compare(pat,pat2)