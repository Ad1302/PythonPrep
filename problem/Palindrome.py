number = ""

def reverser(i,j,num):
    number = str(num)
    list = []
    print(type(num))
    print(type(number))
    for i in range(len(number)):
        list.append(number[i])
    print(list)
    list.reverse()
    print(list)
    string = ""
    for j in list:
        string += j
    print(string)
Palindromic_list =[]

for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        reverser(num,i,j)
        if num == int(string):
            Palindromic_list.append(num)
