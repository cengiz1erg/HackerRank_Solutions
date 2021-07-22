def merge_the_tools(string, k):
    # your code goes here
    str_to_list = list(string)
    output_list = []
    while True:
        for i in range(k):
            if str_to_list[i] not in output_list:
                output_list.append(str_to_list[i])
        del str_to_list[0:k]
        print(''.join(output_list))
        output_list.clear()
        if len(str_to_list) == 0:
            break

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
