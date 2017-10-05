pcpLst = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 9)
]

def getParentData(kids, pcpLst):
    ancestorHM = {}
    
    
    for tup in pcpLst:
        parent = tup[0]
        child = tup[1]
        print(parent)
        print(child)
        
        if ancestorHM.get(child) == None:
            ancestorHM[child] = [parent]
        else:
            val = ancestorHM[child]
            print(val)
            ancestorHM[child] = val.append(parent)
            print(val)
        
    print(ancestorHM)
    parent0 = ancestorHM[kids[0]]
    parent1 = ancestorHM[kids[1]]
    
    if (set(parent0)).intersect(set(parent1)):
        return True
    else:
        return False
    

getParentData([3, 8], pcpLst)
