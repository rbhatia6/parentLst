pcpLst = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 9)
]

# noParentLst = [1,2,4, 8]
# OneParentLst = [7, 5, 8]
# rejectLst = [3,6]

def getParentData(pcpLst):
    rejectLst = []
    NoParentLst = []
    OneParentLst = []
    
    for tup in pcpLst:
        parent = tup[0]
        child = tup[1]
        
        if parent in rejectLst:
            pass
        elif parent in OneParentLst:
            pass
        else:
            if parent not in NoParentLst:
                NoParentLst.append(parent)
            
        if child in rejectLst:
            pass
        else:
            if child in NoParentLst:
                NoParentLst.remove(child)
                OneParentLst.append(child)
            elif child in OneParentLst:
                OneParentLst.remove(child)
                rejectLst.append(child)
            else:
                OneParentLst.append(child)
                
    
    return [sorted(NoParentLst), sorted(OneParentLst)]
                   
print(getParentData(pcpLst))
