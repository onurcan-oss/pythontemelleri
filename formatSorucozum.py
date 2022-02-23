from unicodedata import name
from unittest import result


# website = "https://www.sadikturan.com/"
# course = "Python Kursu: Baştan sona  Python Programlama Rehberiniz (40 Saat)"

# # 1- 'course' akrakter dizisinde kaç karakter bulunmaktadır.

# result = len(course)

# # 2- 'website' içinden www karakterlerini alın.

# result = website[7:10]
# # 3- 'website' içinden com karakterini alın
# result = website[24:26]
# # 4- 'course' içinden ilk 15 ve son 15 akrakterlerini alın.

# result = course[0:15]
# result = course[:15]
# # 5- 'course' ifadesindeki karakterleri tersten yazdırın.

# result = course[::-1]

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis'

#6- Benim adım Bora Yılmaz , Yaşım 32 ve mesleğim mühendis.

result= "Benim adım "+ name + " "+ surname + " , Yaşım"+ str(age) + " ve mesleğim" + job