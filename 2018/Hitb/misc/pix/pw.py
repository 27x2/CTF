import itertools
file = open("pw.txt","w")
a = 'hitb'
b = '0123456789'

for i in itertools.product(b,repeat=6):
    file.write('hitb'+''.join(i)+"\n")

