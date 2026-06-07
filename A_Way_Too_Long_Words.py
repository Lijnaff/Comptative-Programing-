n = int(input())

for i in range(n):
    inputword = input()
    
    if len(inputword) > 10:
        print(inputword[0] + str(len(inputword) - 2) + inputword[-1])
    else:
        print(inputword)












