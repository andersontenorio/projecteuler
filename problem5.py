n = 0
factor = 20
while True:    
    n = n + factor
    is_divisible = True
    for i in range(1, factor + 1):        
        if n % i != 0:
            is_divisible = False
            break
    if (is_divisible):
        break

print(n)
