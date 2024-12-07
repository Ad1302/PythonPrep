# num = 20
# Multiple = True
# def prob_solver(num, i):
#     while num % i != 0:
#         if 
#         num +=1
#     return num
# for i in range(2,21):
#     if num % i !=0:
#         multiple = False
#         num = prob_solver(num,i)
    
#         # while multiple != True:
#         #     num += 1
#         #     if num % i == 0:
#         #         multiple = True
#         #     else:
#         #         num += 1
# print(num)
# list = []
# mul = 1
# i = 1
# def multiple(i,mul):
#     list = [[i][mul]]
#     if i>mul:
        
#     else:
#         for i in range():
        

# def is_divisible_by_all(n, max_divisor):
#     for i in range(1, max_divisor + 1):
#         if n % i != 0:
#             return False
#     return True

# def find_smallest_multiple_simple():
#     n = 1
#     while True:
#         if is_divisible_by_all(n, 20):
#             return n
#         n += 1

# print(find_smallest_multiple_simple())

















no = int(input("enter the no. till which you want the LCM"))
def is_divisible(n, max_no):
    for i in range(2,max_no+1):
        if n % i !=0:
            return False
    return True

def num_to_calc(n,no):
    n=1
    while True:
        if is_divisible(n,no):
            return n
        n += 1

# print(f'''the smallest no. that is the LCM of all no.s till{max_no} is {num_to_calc()}''')
print(num_to_calc(1,no))