# eine implementierung mit der man Rafaels Zahl berechnen kann!
# urheber der formel: unbekannt!

# R(0) = 4
# R(n) = 2^(R(n - 1)!)

def fac(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    return f

def rafaelsZahl(n):
    if n == 0:
        return 4
    return pow(2, fac(rafaelsZahl(n - 1)))

n = int(input('n = '))
print("".join(['rafaels zahl in ', str(n), ' iterationen = ', str(rafaelsZahl(n))]))
