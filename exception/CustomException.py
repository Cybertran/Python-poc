
first_number = int(input("Enter number"))

if first_number > 5:
    raise TypeError("Enter number lower than {}".format(str(first_number)))

