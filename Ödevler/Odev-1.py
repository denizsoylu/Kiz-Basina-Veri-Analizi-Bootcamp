"""
Python dersi 2.hafta ödevlerini içerir.
ödevler ilk değerler kullanıcıdan alınarak
1- girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul
2- girilen sayının tek mi çift mi olduğunu yazan koşul
3- Girilen nota göre harf aralığını yazan koşul (80-100 A, 60-80 B vs.)
4- Girilen ismin karakter sayısı 5den büyükse "uzun bir isminiz var" değilse ismini yazsın
5- Girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
6- notlar=[45,85,75,50] içinde 75 değerinin indisini yazdıran döngü
7- girilen sayının faktöriyelini alalım. (for ve while)
8- Kullanıcıdan pozitif bir sayı bekleyen, pozitifi de gördüğü an bastıran, negatif sayı girildikçe bir daha soran yapı kuralım. (for döngüsü ile)
9- fonksiyon ile girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
10-fonksiyon ile girilen sayının faktöriyelini alalım. (for ve while)

"""
######################################################################
# 1 - Girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul
#######################################################################
x = int(input("Bir sayı yazınız: "))

if x > 0 :
    print("Sayı pozitif.")
elif x < 0 :
    print("Sayı negatif.")
else:
    print("Sayı sıfıra eşittir")


###########################################################
# 2 - girilen sayının tek mi çift mi olduğunu yazan koşul
###########################################################

y = int(input("Bir sayı yazınız: "))

if y % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")



##########################################################################
# 3 - Girilen nota göre harf aralığını yazan koşul (80-100 A, 60-80 B vs.)
##########################################################################

z = int(input("Not giriniz :"))

if 80 <= z <=100:
    print("Harf notunuz : A")
elif 60 <= z < 80:
    print("Harf notunuz : B")
elif 40 <= z < 60:
    print("Harf notunuz : C")
elif 20 <= z < 40:
    print("Harf notunuz : D")
elif 0<= z < 20:
    print("Harf notunuz : F")
else:
    print("Hatalı giriş yaptınız! 0-100 arasında notunuzu giriniz.")


#############################################################################################
# 4 - Girilen ismin karakter sayısı 5den büyükse "uzun bir isminiz var" değilse ismini yazsın
#############################################################################################
a = str(input("Adınızı giriniz:"))

if 5<= len(a):
    print("Uzun bir isminiz var.")
elif 1 < len(a) < 5:
    print("Kısa bir isminiz var")
else:
    print("Hatalı isim girişi yaptınız.")


##########################################################################
# 5 - Girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
##########################################################################

#for
b = int(input("Bir sayı giriniz"))

if b ==2:
    print(f'{b} sayısı asaldır.')
elif b < 2:
    print(f'{b} sayısı asal değildir.')
else:
    for i in range(2, b):
           if b % i ==0:
               print(f'{b} sayısı asal değildir.')
               break

    else: # Bu else, for döngüsüne ait
        print(f'{b} sayısı asaldır.')


#while
b = int(input("Bir sayı giriniz"))

if b ==2:
    print(f'{b} sayısı asaldır.')
elif b < 2:
    print(f'{b} sayısı asal değildir.')
else:
    i = 2
    while i < b:
        if b % i == 0:
            print(f'{b} sayısı asal değildir.')
            break
        i += 1
    else:  # Bu else, while döngüsüne ait
        print(f'{b} sayısı asaldır.')


##########################################################################
# 6 - notlar=[45,85,75,50] içinde 75 değerinin indisini yazdıran döngü
##########################################################################

#for
notlar = [45,85,75,50]

print("Elemanlar:")
for i in notlar:
    print(i)   # i: eleman (değer)

print("-------------------")

print("\nİndeksler ve elemanlar:")
for i in range(len(notlar)):
    print(i, notlar[i])   # i: indeks, notlar[i]: o indeksteki değer

print("-------------------")

for i in range(len(notlar)):
    if notlar[i] ==75:
        print(i)


#while
notlar = [45,85,75,50]

i = 0
while i < len(notlar):
    if notlar[i] == 75:
        print(i)
        break
    i += 1


##########################################################################
# 7 - Girilen sayının faktöriyelini alalım. (for ve while)
##########################################################################

#for
x = int(input("Bir sayı giriniz:"))

sonuc = 1
for i in range(1, x + 1):
    sonuc = sonuc * i

print(sonuc)


#while
x = int(input("Bir sayı giriniz:"))

i = 1
sonuc = 1
while i <= x:
    sonuc = sonuc * i
    i+=1
print(sonuc)


###############################################################################
# 8 - Kullanıcıdan pozitif bir sayı bekleyen, pozitifi de gördüğü an bastıran,
# negatif sayı girildikçe bir daha soran yapı kuralım. (for döngüsü ile)
###############################################################################

for i in range(100):
    x = int(input("Bir sayı giriniz"))
    if x > 0:
        print("Sayı pozitiftir.")
        break
    else:
        print("Girdiğiniz sayı negatif. Tekrar deneyiniz.")

while True:
    x = int(input("Bir sayı giriniz"))
    if x > 0:
        print("Sayı pozitiftir.")
        break
    else:
        print("Girdiğiniz sayı negatif. Tekrar deneyiniz.")

##########################################################################################
# 9 - Fonksiyon ile girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
##########################################################################################

b = int(input("Bir sayı giriniz"))
def asalmi (b):
    if b == 2:
        print(f'{b} sayısı asaldır.')
    elif b < 2:
        print(f'{b} sayısı asal değildir.')
    else:
        for i in range(2, b):
            if b % i == 0:
                print(f'{b} sayısı asal değildir.')
                break

        else:  # Bu else, for döngüsüne ait
            print(f'{b} sayısı asaldır.')

asalmi(b)

##########################################################################
# 10 - Fonksiyon ile girilen sayının faktöriyelini alalım. (for ve while)
##########################################################################

x = int(input("Bir sayı giriniz"))
def faktoriyel (x):
    i=1
    sonuc=1
    while i <= x:
        sonuc = sonuc * i
        i = i + 1
    print(f'{x} sayının faktöriyeli =  {sonuc}')

faktoriyel(x)

x = int(input("Bir sayı giriniz"))
def faktoriyel2 (x):
    sonuc = 1
    for i in range(1, x+1):
        sonuc = sonuc * i
    print(f'{x} sayının faktöriyeli =  {sonuc}')

faktoriyel2(x)
