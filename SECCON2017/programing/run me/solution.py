def sum_fibonanci(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n-1):
        sum=a+b
        a=b
        b=sum
    return sum
print "SECCON{" + str(sum_fibonanci(11011))[:32] + "}"
