def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

num = input("Enter a number to get the Factorial: ")
print "Result: ",factorial(num)
