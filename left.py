# print the List1 elements which are not present in List2

List1=[ 'nrupatunga', 'tanu', 'nidhi', 'papu', 'muddu', 'pingu']
List2= ['pingu', 'muddu', 'nidhi']
List3 = list(set(List1) - set(List2))

print("List3 =", List3 )
