list = [5, 4, 3, 6, 8, 9, 6, 2, 3, 4]
ElementsIndex = []
x = input("Enter a number: ")

if x in list:
    for i in range(0, len(list), 1):
        if x == list[i]:
            ElementsIndex.append(i)
    print "Last Index: ", ElementsIndex[len(ElementsIndex) - 1]
else:
    print "Last Index: Not found!"
