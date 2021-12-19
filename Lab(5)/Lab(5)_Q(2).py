l=[]
pos = 0
neg=0
while 1:
    x = input("Enter Your Number: ")
    if x==0:
        break
    else:
        if x>0:
            pos+=1
        if x<0:
            neg+=1
        l.append(x)

print pos,"Positive inputs and",neg,"Negative inputs"
print "Your inputs Summation: ",sum(l)
print "Your inputs Avarage: ",sum(l)/len(l)
