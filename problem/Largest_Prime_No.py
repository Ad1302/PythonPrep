#600851475143
# num = 0
# factor_list = []
# prime_listing = []
# count = 0
# def factor(num):
#     for i in range(1,num+1):
#         if num % i == 0:
#             factor_list.append(i)
#     return factor_list

# num = int(input("Enter the no. for which you would like to get the highest prime factor: "))
# factor(num)
# print(factor_list)

# def prime_list(factor_list):
#     for i in factor_list:
#         count = 0
#         for j in range(1,i+1):
#             if i % j ==0:
#                 count += 1
#         if count == 2:
#             prime_listing.append(i)
#     return prime_listing

# prime_list(factor_list)
# print(prime_listing)
# Max = 0

# for i in prime_listing:
#     if i>Max:
#         Max = i
# print("The largest prime Factor in the list is ", Max)

# list = [1,2,3,6]
# m_mist = []
# for i in range(list[1], len(list)):
#     count = 0
#     for j in range(1,i+1):
#         if i % j ==0:
#                 count += 1
#     if count == 2:
#         m_mist.append(i)
# print(m_mist)

def largest_prime_factor(n):
    # Start with the smallest prime number
    i = 2

    # Keep dividing n by smaller numbers until i^2 > n
    while i * i <= n:
        if n % i:  # If n is not divisible by i
            i += 1  # Move to the next number
        else:  # If n is divisible by i
            n //= i  # Divide n by i and continue

    # If n is still greater than 1, it's the largest prime factor
    return n if n > 1 else i

# Test the function with a large number
number = 600851475143
result = largest_prime_factor(number)
print(f"Largest prime factor of {number} is: {result}")