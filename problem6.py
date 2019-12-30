n = 100
squares_sum = 0
sum_squares = 0
for i in range(1, n + 1):
    squares_sum = squares_sum + (pow(i, 2))
    sum_squares = sum_squares + i

sum_squares = pow(sum_squares, 2)

print(sum_squares - squares_sum)
