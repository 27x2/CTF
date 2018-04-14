import itertools
file = open("pw.txt","w")
b = '0123456789'

for i in itertools.product(b,repeat=6):
    file.write('hitb'+''.join(i)+"\n")

