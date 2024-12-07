number = ""

def reverser(num):
    number = str(num)
    list = []
    for i in range(len(number)):
        list.append(number[i])
    list.reverse()
    string_a = ""
    for j in list:
        string_a+= j
    return int(string_a)
Palindromic_list =[]

for i in range(999,99,-1):
    for j in range(999,99,-1):
        num = i*j
        opp = reverser(num)
        if num == opp:
            Palindromic_list.append(num)
print(Palindromic_list)

def largest(Palindromic_list):
    Largest = Palindromic_list[0]
    for i in range(len(Palindromic_list)):
        if Palindromic_list[i]> Largest:
            Largest = Palindromic_list[i]
    return Largest
print(largest(Palindromic_list))
#906609 913*993