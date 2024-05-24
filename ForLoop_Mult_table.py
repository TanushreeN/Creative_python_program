a = int(input("Enter a Number : "))
n = ""
c = ""
print("-------The tables of 1st ", a , "numbers -------")
for i in range(a):
    print(" ")
    for n in range(1, 11, 1):
        c = a * n
        n += 1
        print(c, " ", end="")
    a -= 1
