#RhendyDikiNugraha
print("Menentukan bilangan terbesar dari 3 input")

a = int(input('Masukkan bilangan a: '))
b = int(input('Masukkan bilangan b: '))
c = int(input('Masukkan bilangan c: '))

if a > b and a > c:
    print(a ,'= A adalah yang terbesar')
elif b > a and b > c:
    print(b ,'= B adalah yang terbesar')
else:
    print(c ,'= C adalah yang terbesar')