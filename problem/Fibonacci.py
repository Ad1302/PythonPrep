# fibonacci = [1,2]
# num = 0
# sum = 0
# for i in range(2,400):
#     num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(num)
#     if num % 2 ==0:
#         sum += num
# print(sum)

# Function to find sum of even Fibonacci numbers up to 4 million
def even_fibonacci_sum(limit):
    # Initialize first two Fibonacci numbers
    a, b = 1, 2
    # Initialize sum to store even Fibonacci numbers
    total = 0
    
    # Continue loop until we reach the limit
    while a <= limit:
        # If current Fibonacci number is even, add it to total
        if a % 2 == 0:
            total += a
        
        # Generate next Fibonacci number
        # Store current 'b' in temp variable to calculate next number
        temp = b
        b = a + b  # Next number is sum of previous two
        a = temp   # Move 'b' to 'a' for next iteration
    
    return total

# Set limit to 4 million as per problem requirement
limit = int(input("Please enter the limit e.g. 4000000: "))
# Call function and print result
result = even_fibonacci_sum(limit)
print(f"Sum of even Fibonacci numbers not exceeding {limit}: {result}")