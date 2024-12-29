min = int(input("Enter the first num of the range"))
max = int(input("Enter the last num of the range"))
prime_list = []
prime = False

def prime_checker(i):
    if i > 2:
        if i % 2 != 0:
            prime = True
        else:
            prime = False

    elif i == 2:
        prime = True
    else:
        prime = False
    return prime
for i in range(min, max+1):
    prime_val = prime_checker(i)
    if prime_val == True:
        prime_list.append(i)

print(prime_list)