#dairenin alanı : pi x r^2
#dairenin çevresi : 2 x pi x r
# yarıçapı verilen dairenin alan ve çevresini hesaplayınız. (r: 3.14)

pi = 3.14 

yariCap = float(input("yarı çapı :"))
alan =  pi * (yariCap ** 2)

cevre = 2 * pi *yariCap

print("Alan: ", alan)
print("Çevre: ",cevre)