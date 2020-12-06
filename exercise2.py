num=input("Enter number: ")
if int(num) %4 == 0:
    print(str(num) + " is a multiple of 4.")
elif int(num) %2 == 0:
    print(str(num) + " is an even number.")
else:
    print(str(num) + " is an odd number.")
