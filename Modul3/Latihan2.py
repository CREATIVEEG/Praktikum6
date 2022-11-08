#RhendyDikiNugraha
print("\nMenampilkan bilangan dan berhenti ketika bilangan 0, lalu menampilkan bilangan terbesar\n")

max = 0
while True:
    angka = int(input("Masukan bilangan : "))
    if max < angka:
        max = angka
    if angka == 0:
        break
print("Bilangan terbesarnya adalah = ", max)