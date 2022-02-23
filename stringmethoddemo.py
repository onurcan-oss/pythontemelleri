website = "https://www.sadikturan.com/"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


#1- 'Hello World' akrakteri dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()

result = website.lstrip('/:pth')

print(result)

#2- 'www.sadikturan.com içindeki sadikturan bilgisi haricindeki her akrakteri siliniz

result = 'www.sadikturan.com'.strip('w.com')
print(result)

# 'course karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
result = course.title()
print(result)