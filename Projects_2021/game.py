import random,os,time
ozel = input("Özel Bir İsminiz Var mı?(Yoksa Geçiniz:)")

if ozel =="Mustafa Kemal Atatürk":
	print("Hoş geldin Türkiye Cumhuriyet'inin tek atası")

if ozel =="Dilşah":
	print("Hoş geldin Dünya'nın en pozitif en tatlı ve en güzel insanı")



if ozel =="İsmet İnönü":
	print("Hoş geldiniz batı orduları komutanı , Cumhuriyet'in 2. Adamı Atatürk'ün kadim dostu.Buyrun size bir kahve ısmarlayalım.")
boy = ["Hüseyin","Ege","Mustafa Selim","Ali Özkan","Kadir","Talha Kamil","Süleyman Tuna","Burhan","Cemil Taha","Fırat","Gökalp","Efe","Yağız"]

girl = ["Melisa","Pelin","Yasemin Tuğba","Nisanur","Ezgi","Melis","Elif Buse","Şilya","Melek","Azra Nur","Nisa Duru","Melike","Şevval","Sıla","Dilşah","Simay","Kübra","Nisanur Kabucu","Sema","Esmanur","Elif","Emel","Ece Nur","Sena Nur","Rukiye","Ezel","Zeynep"]

herkes = ["Hüseyin","Ege","Mustafa Selim","Ali Özkan","Kadir","Talha Kamil","Süleyman Tuna","Burhan","Cemil Taha","Fırat","Gökalp","Efe","Yağız","Melisa","Pelin","Yasemin Tuğba","Nisanur","Ezgi","Melis","Elif Buse","Şilya","Melek","Azra Nur","Nisa Duru","Melike","Şevval","Sıla","Dilşah","Simay","Kübra","Nisanur Kabucu","Sema","Esmanur","Elif","Emel","Ece Nur","Sena Nur","Rukiye","Ezel","Zeynep"]

soran = ["Erkek","Kız"]

random.shuffle(herkes)

sayi3 = random.randint(0,1)


print("""

1-)Birbirimize Açılalım


2-)Geç Bu Aşk Olaylarını Sar DC



	""")


secim = int(input("Seçiminizi Yapın: "))

if secim == 1:
	sayi1 = random.randint(0,len(boy))
	sayi2 = random.randint(0,len(girl))
	print(f"Soran Kişi:{soran[sayi3]} |Kişiler: Erkek {boy[sayi1]} Kız {girl[sayi2]}")

if secim == 2:

	sayi4 = random.randint(0,len(herkes))
	sayi5 = random.randint(0,len(herkes))
	print(f"Soran Kişi: {herkes[sayi4]} | Sorulan Kişi: {herkes[sayi5]}")



else:

	print("Hatalı Tuşlama Yaptınız")
