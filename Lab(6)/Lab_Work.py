def Reverse(l):
    count =len(l)-1
    ll=[]
    for i in range(0,len(l)):
        ll.append(l[count])
        count=count-1
    return ll


print Reverse([1,2,3,4])
