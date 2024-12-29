import math
prime_count = 0
prime_list = []
count = 13

def prime_finder(count):
    prime_no = False
    factor_count = 0
    # if count == 2:
    #     return count
    # else:
    while prime_no == False:
        factor_count = 0
        sqrt = math.floor(count**0.5)
        for j in range(3, sqrt+1, 2):
            if count % j ==0:
                factor_count += 1
                break
        if factor_count==0:
            prime_no = True
        else:
            count += 2 
    return count

while prime_count !=9995:
    num = prime_finder(count)
    prime_list.append(num)
    prime_count += 1
    count = num +2
print(prime_list[9994])



# import math


# # Function to check if a number is prime
# def is_prime(num):
#     if num < 2:
#         return False
#     for j in range(2, math.isqrt(num) + 1):  # Test divisors up to the square root
#         if num % j == 0:
#             return False
#     return True


# # Main loop to generate 9995 prime numbers
# prime_list = []
# count = 13  # Starting from the first prime number after 2

# # Loop until we find 9995 primes
# while len(prime_list) < 9996:
#     if is_prime(count):  # Check if the number is prime
#         prime_list.append(count)  # Save it to the list
#     count += 2  # Only test odd numbers (even numbers > 2 are non-prime)

# # Print the 9995th prime number
# print(prime_list[-1])  # The last prime in the list is the 9995th prime





# import math

# prime_count = 0
# prime_list = []
# count = 13  # Start with the first odd number after skipping 2

# def prime_finder(count):
#     prime_no = False
#     while not prime_no:
#         factor_count = 0
#         sqrt = math.floor(count**0.5)
#         for j in range(3, sqrt + 1, 2):  # Skip even divisors
#             if count % j == 0:
#                 factor_count += 1
#                 break
#         if factor_count == 0:  # No divisors found
#             prime_no = True
#         else:
#             count += 2  # Increment by 2 to check the next odd number
#     return count

# while prime_count != 9995:
#     num = prime_finder(count)
#     prime_list.append(num)
#     prime_count += 1
#     count = num + 2  # Start from the next odd number after the found prime

# print(prime_list[9994])  # Print the 9995th prime
