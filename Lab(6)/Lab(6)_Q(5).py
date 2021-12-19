def GetMin(l):
    min = l[0]
    for i in range(1,len(l)-1):
        if l[i]<min:
            min = l[i]
    return min

l=[0,1,2,3,4,5,6,9,8,7,-1,-8,-7,-6,-5,-4,-10,0]
print"Result: ",GetMin(l)