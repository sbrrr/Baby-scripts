c=input("Enter number: ")
a = [1, 1, 3, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for element in a:
    if element <= int(c):
        b.append(element)
print(b)
