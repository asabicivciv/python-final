
import pymysql.cursor

db=pymysql.connect(host='localhost')
user='root',
password='',
db='yemektarifleri',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

baglanti=db.cursor()


print(" Yemek Tariflerine Hoşgeldiniz :)")

kayıt = open("yemektarifleri.txt", "w") 
kayıt.write(input(  "Yemek Adı Giriniz = " )) 
kayıt.write(input( "Yemek Tarifi Giriniz = " ))
kayıt.close()

dosya = open("yemektarifleri.txt","r",encoding="utf-8")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)
