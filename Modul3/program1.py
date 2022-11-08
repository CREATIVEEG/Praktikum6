#RhendyDikiNugraha
modal = 100000000
sum = 0
y = 0
lb = [int(0), int(0), int(modal) * .1, int(modal) * .1, int(modal) * .5, int(modal) * .5, int(modal) * .5, int(modal) * .2]
print("modal awal seorang pengusaha :', modal")
for i in lb:
    sum = sum + i
    y += 1
    print("#Laba bulan ke - ", y, "sebesar :", i)

    print("  TOTAL LABA YANG DIDAPAT ADALAH :", sum)