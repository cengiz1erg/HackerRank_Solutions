import re
input_list = []
tekrar = int(input())
for _ in range(tekrar):
    input_list.append(input())
for x in range(tekrar):
    string = input_list[x]
    if(re.search(r'^([1-2]?\d{1,2}\.){3}[1-2]?\d{1,2}$',string)):
        print("IPv4")
    elif(re.search(r'^([a-f\d]{1,4}:){7}[a-f\d]{1,4}$',string)):
        print("IPv6")
    else:
        print("Neither")
