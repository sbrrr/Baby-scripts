num=input("Enter denominator: ")
check=input("Enter nominator: ")
if int(check) % int(num) == 0:
    print(str(check) + " is divided evenly by " + str(num) + ".")
else:
    print(str(check) + " is divided oddly by " + str(num) + ".")
