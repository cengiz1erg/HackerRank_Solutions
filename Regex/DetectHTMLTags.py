import re

input_number = int(input()) #take input number from user
input_list = [] #list of strings of input tags
captured_tags = []
for _ in range(input_number):
    input_list.append(input()) #take input tags
for x in range(input_number):
    p = re.findall(r'<\s*(\w+)',input_list[x]) #return list of strings
    captured_tags = captured_tags + p #concat lists
a = list(set(captured_tags)) #list of distinct strings
a.sort()
print(";".join(a))
