def isPrime(num):
    if num == 1:
        return False

    for i in range(2,num/2+1):
        if num % i == 0:
            return False
        else:
            continue
    return True

num = input("Enter a number: ")
print "Result:",isPrime(num)