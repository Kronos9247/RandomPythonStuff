def a_pow_n(a, n):
    value = 1;
    for index in range(abs(n)):
        value *= a;
        
    if n < 0:
        value = 1 / value;
        
    return value

print (a_pow_n(10, -2));
