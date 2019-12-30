def is_prime(n):
    is_prime = True
    if n == 1 or n == 2:
        is_prime = True
    elif n > 2 and n % 2 != 0:        
        for i in range(2, n // 2):
            if n % i == 0:
                is_prime = False
                break
    else: 
        is_prime = False
    return is_prime

def is_palindromic(n):
    sn = str(n)
    s1 = sn
    s2 = sn[::-1]
    return (s1 == s2)

    
        