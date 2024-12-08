n = int(input())
sum_square = 0
sum = 0
for i in range(1,n+1):
    sum += i
sum_square = sum**2
square_series_sum = 0
for i in range(1,n+1):
    square_series_sum += i**2
difference = sum_square - square_series_sum
print(f"the diff between the sum of no.s - the square of the no. is {difference}")
