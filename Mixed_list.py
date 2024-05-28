#Take an array containing both charectors and numbers. The output has to be like  all the chars has to come in the starting of the array and all the numbers after the last char in the list. 
#Input: [ a, 6, h, t, n, 7]
#Output: [a, h, n, t, 6, 7]

list1 = [ "a", 6, "h", "t", "n", 7]
str_list = []
num_list = []

for x in list1:
    if isinstance(x, str):
        str_list.append(x)
    elif isinstance(x,(int,float)):
        num_list.append(x)
        
str_list.sort()
num_list.sort()
print(str_list + num_list)

#Ouput: ['a', 'h', 'n', 't', 6, 7]
