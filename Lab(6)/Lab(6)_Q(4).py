def isPalindrome(str):
    l1 = []
    l2 = []

    for i in range(0, len(str) / 2):
        l1.append(str[i])

    if len(str)%2==0:
        for i in range(len(str) - 1, (len(str) / 2) - 1, -1):
            l2.append(str[i])
    else:
        for i in range(len(str) - 1, (len(str) / 2), -1):
                l2.append(str[i])
    if l1 == l2:
        return True
    else:
        return False

str = raw_input("Enter a text: ")
print "Result: ",isPalindrome(str)
