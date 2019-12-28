fib = 3
prev1 = 1
prev2 = 2
sum = prev2
while True:    
    fib = prev1 + prev2
    if fib >= 4000000:
        break    
    prev1 = prev2
    prev2 = fib    
    if fib % 2 == 0:
        sum = sum + fib    

print(sum)