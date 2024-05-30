#Given a string. the task is to check if the string is symmetrical and palindrome or not. A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears the same when read forward or backward.

#Example: 

#Input: khokho
#Output: 
#The entered string is symmetrical
#The entered string is not palindrome

#Input:amaama
#Output:
#The entered string is symmetrical
#The entered string is palindrome



#_______________________________________
#Code

word = input("Enter a word : ").lower()
 
if (len(word) % 2 == 0):
     print("The word is symmetrical")
else:
     print("The word is not symmetrical")


if word == word[::-1]:
    print("The given word" + " " + word + " " + "is Palindrome")
else:
    print("The given word" + " " + word + " " + "is not a Palindrome")
#________________________________________
#Outputs

#Enter a word : Anna
#The word is symmetrical
#The given word anna is Palindrome

#Enter a word : kho_kho
#The word is not symmetrical
#The given word kho_kho is not a Palindrome
