l = list()

for num in range(2, 100):

    if num == 2:  # Special case for the number 2 (the only even prime)
        l.append(num)
    
    else:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0 or num < 2 or num % 2 == 0:  # If num is divisible by any number other than 1 and itself
                is_prime = False
                break
        if is_prime:
            l.append(num)

print("Prime numbers:", l)
