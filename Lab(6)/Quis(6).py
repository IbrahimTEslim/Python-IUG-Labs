def Get_Avg(l,n):
    avg1=0
    sum1=0
    avg2=0
    sum2=0
    for i in l:
        sum1 += i
    for u in n:
        sum2+=u
    avg1 = (sum1+sum2)/(len(l)+len(n))
    return avg1

l = [1,2,3,4]
n=[4,3,2,1]
print Get_Avg(l,n)
