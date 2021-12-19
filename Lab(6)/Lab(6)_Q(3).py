def isPrime(num):
    if num == 1:
        return False
    for i in range(2,num/2+1):
        if num % i == 0:
            return False
        else:
            continue
    return True


def printPrimeNumbers(num):
    for i in range(num+1):
        if(isPrime(i)):
            print i,
    return

num = input("Enter a number: ")
print "Result:",printPrimeNumbers(num)