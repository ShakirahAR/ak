#x = int (input("Masukkan satu nombor:"))
#baki= x%2
#print (baki == 0, x, "ialah nombor genap")
#print (baki != 0, x, "ialah nombor ganjil")


#nomb1 = int(input("Masukkan nombor pertama:"))
#nomb2 = int(input("Masukkan nombor kedua:"))
#if (nomb1>nomb2):
#    terbesar = nomb1
#if (nomb2>nomb1):
 #   terbesar = nomb2
#print ("Nombor terbesar ialah:",terbesar)


nomb1= int(input("Masukkan nombor pertama:"))
nomb2= int(input("Masukkan nombor kedua:"))
nomb3 = int(input("Masukkan nombor ketiga:"))
if (nomb1<nomb2) and (nomb1<nomb3):
    terkecil = nomb1
if (nomb2<nomb1) and (nomb2<nomb3):
    terkecil = nomb2
if (nomb3<nomb1) and (nomb3<nomb2):
    terkecil = nomb3
print ("Nombor terkecil ialah:", terkecil)
