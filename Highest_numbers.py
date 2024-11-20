#program to get only the required number of highest numbers from list where noumber of highest requirements is user input


a = int(input("Enter a number from 1 to 6: "))
numbers = [81, 52, 45, 3, 2, 96] 
sorted_list = sorted(numbers)
print(sorted_list)


for num in numbers[(a-2)::-1]:
 print(num, end =" ")
print(numbers[-1])
