import sys
import scapy.all



list = [[51, 8, 19, 25], [98, 16, 13, 22], [25, 10, 66, 13], [20, 12, 64, 58]]

max = -sys.maxint - 1

for i in range(len(list)):
    for j in list[i]:
        if j >= max:
            max = j

print ("Max number is: ", max)

for i in range(len(list)):
    for j in list[i]:
        if j < min:
            min = j



print ("Min number is: ", min)
