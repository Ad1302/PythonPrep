mutiple_list = []
# for i in range(1,1000):
#     if i % 3 == 0 or i % 5 ==0:
#         mutiple_list.append(i)
# print(mutiple_list)
# sum = 0
# for i in range(len(mutiple_list)):
#     sum += mutiple_list[i]
# print(sum)

# sum = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 ==0:
#         sum += i

# print(sum)

# num1 = int(input("what is the no. you want to check the multiples of"))
# num2 = int(input("What is the other no.?"))
# num3 = int(input("What is the no. below which you want to see the sum of the multiples of the 2 no.s"))
# sum = 0
# for i in range(num3):
#     if i % num1 == 0 or i % num2 ==0:
#         sum += i

# print(sum)



# if i % 3 == 0 or i % 5 ==0:
mutiple_list = sum([i for i in range(1000) if i % 3 == 0 or i % 5 ==0])

print(mutiple_list)