import math #library untuk operasi matematika

#Mendefinisikan fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r*r # Menggunakan rumus πr²
#lambda : fungsi tanpa nama (anonim) yang didefinisikan menggunakan kata kunci lambda

#Contoh penggunaannya
jari_jari = 7 #Menetapkan nilai jari-jari lingkaran
area = luas_lingkaran(jari_jari) #Menghitung luas lingkaran dengan jari-jari yang ditentukan
#area :  ukuran dari ruang yang dikelilingi oleh batas suatu bentuk
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}") #Mencetak hasil dengan format dua desimal