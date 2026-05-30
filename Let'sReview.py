num = int(input())
for i in range(num):
    string = input()
    even = ""
    odd = ""
    for j in range(len(string)):
        if j%2 == 0:
            even += string[j]
        else:
            odd += string[j]
    print(even,odd)