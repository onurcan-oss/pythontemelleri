from email import message


message = 'Hello There. My name is Onurcan Akcay'

# message = message.upper() baş harfler büyük
# message = message.lower() bütün harfler büyük
# message = message.title() bütün harfler küçük
# message = message.capitalize() sadece ilk harf büyük

# index = message.find('Akcay') cümle icerinde kelime arama
# isFound = message.startswith('H') cümle h harfi ile başlıyor mu?
# isFound = message.startswith('B') cümle b harfi ile başlıyor mu?
isFound = message.endswith('y') 
print(isFound)

print(message)