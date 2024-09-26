# Sqauares using list concept

n = int(input("Enter the number till you wan't the square : "))
squares = [x ** 2 for x in range(n+1)]
print(squares)

# OP : Enter the number till you wan't the square : 10
#      [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
