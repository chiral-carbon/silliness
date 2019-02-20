def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
if __name__ == '__main__':
    n = [13710221545914561761, 11066328760152681859]
    a = [13710221545914561760, 11066328760152681858]
    print chinese_remainder(n, a)
    n = [13710221545914561761, 11066328760152681859]
    a = [1, 11066328760152681858]
    print chinese_remainder(n, a)
    n = [13710221545914561761, 11066328760152681859]
    a = [13710221545914561760, 1]
    print chinese_remainder(n, a)
    n = [13710221545914561761, 11066328760152681859]
    a = [1, 1]
    print chinese_remainder(n, a)
    
    print("\n")

    n = [11, 13]
    a = [5, 4]
    print chinese_remainder(n, a)
    n = [11, 13]
    a = [5, 9]
    print chinese_remainder(n, a)
    n = [11, 13]
    a = [6, 4]
    print chinese_remainder(n, a)
    n = [11, 13]
    a = [6, 9]
    print chinese_remainder(n, a)
