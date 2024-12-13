# Input : geeks_for_geeks              Output : GeeksforGeeks
# Input : left_index                   Output : leftIndex
#___________________________________

def remove(string, char_remove):
    return string.replace(char_remove, "")

string = "geeks_for_geeks".title()
char_remove = "_"
result = remove(string, char_remove)
print(result)
