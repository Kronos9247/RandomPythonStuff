def pow(a, n):
    value = 1;
    for index in range(abs(n)):
        value *= a;

    if n < 0:
        value = 1 / value;
        
    return value

def root2(r, e):
    a = abs(r);
    b = 0;
    
    val = 1; 
    stepper = 0;
    su = b + val;
    
    while stepper < 15:
        while pow(su, e) < a:
            b += val;

            su = b + val;

        if pow(su, e) == a:
            return su;

        stepper+=1;
        b -= val;
        su = b;
        val /= 10;
        
    return su

print(root2(5139, 6));
