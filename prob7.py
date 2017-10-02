n =100
prime_arr = []
for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
        else:
            if p not in prime_arr:
                prime_arr.append(p)
print(prime_arr)
