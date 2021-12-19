print("Enter the 3 numvers you want to sort:\n")

first = input("first N.O.: ")
second = input("second N.O.: ")
third = input("third N.O.: ")
#################################### // First prospect that the 1st number is the biggest
if first >= second and first >= third:
    biggest = first
    if second >= third:     # // cheking to see which from the 2ed or 3rd numbers is the midst one
        mid = second
        smallest = third
    else:                   # // Here it shows that the 3rd number is the midst so the 2ed is the smallest
        mid = third
        smallest = second
#################################### // Second prospect that the 2ed number is the biggest
if second >= first and second >= third:
    biggest = second
    if third >= first:      # // cheking to see which from the 1st or 3rd numbers is the midst one
        mid = third
        smallest = first
    else:                   # // Here it shows that the 1st number is the midst so the 3rd is the smallest
        mid = first
        smallest = third
#################################### // Third prospect that the 3rd number is the biggest
if third >= first and third >= second:
    biggest = third
    if second >= first:  # // cheking to see which from the 1st or 2ed numbers is the midst one
        mid = second
        smallest = first
    else:                # // Here it shows that the 1st number is the midst so the 2ed is the smallest
        mid = first
        smallest = second

print smallest, "<=", mid, "<=", biggest
