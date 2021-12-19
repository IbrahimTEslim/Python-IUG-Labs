first = input("Enter First triangle rib's:\n")
second = input("")
third=input("")

if first+second>third and first+third>second and third+second>first:
    print"\nThe tirangle with sides (",first,",",second,",",third,") is valid triangle"
else:
    print"No, this triangle is not valid !!"