#RhendyDikiNugraha
print("Menampilkan bilangan acak yang lebih kecil dari 0.5")
import random

n = int(input("Masukan jumlah nilai: "))
a = 0
for c in range(n):
    a += 1
    b = random.uniform(.0, .5)
    print("Data ke:", a, "-->", b)
