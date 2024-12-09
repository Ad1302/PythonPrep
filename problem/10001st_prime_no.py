# import math
# prime_count = 0
# prime_list = []
# count = 13
# factor_count = 0
# def prime_finder(count, factor_count):
#     prime_no = False
#     # if count == 2:
#     #     return count
#     # else:
#     while prime_no == False:
#         factor_count = 0
#         sqrt = math.floor(count**0.5)
#         for j in range(2, sqrt+1):
#             if count % j ==0:
#                 factor_count += 1
#                 break
#         if factor_count==0:
#             prime_no = True
#         else:
#             count += 2
#     return count

# while prime_count !=9995:
#     num = prime_finder(count, factor_count)
#     prime_list.append(num)
#     prime_count += 1
# print(prime_list[9994])



import math


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for j in range(2, math.isqrt(num) + 1):  # Test divisors up to the square root
        if num % j == 0:
            return False
    return True


# Main loop to generate 9995 prime numbers
prime_list = []
count = 13  # Starting from the first prime number after 2

# Loop until we find 9995 primes
while len(prime_list) < 9996:
    if is_prime(count):  # Check if the number is prime
        prime_list.append(count)  # Save it to the list
    count += 2  # Only test odd numbers (even numbers > 2 are non-prime)

# Print the 9995th prime number
print(prime_list[-1])  # The last prime in the list is the 9995th prime
