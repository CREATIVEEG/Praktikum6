#Rhendy_Diki_Nugraha
#Menentukan bilangan terbesar dari dua input
print("Menentukan bilangan terbesar dari dua bilangan")

a = int(input('Masukkan nilai A: '))
b = int(input('Masukkan nilai B: '))
c = int(input('Masukkan nilai C: '))

if a > b and a > c:
  print("A =",a ,"yang terbesar")
elif b > a and b > c:
  print("B =",b, "yang terbesar")
else :
  print("C =",c, "yang terbesar")