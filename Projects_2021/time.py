import time


print("""

Burhan'ın Zaman Makinesine Hoş Geldiniz :)

1-)Geri Sayım

2-)Kronometre



	""")

secim = int(input("Seçiminizi yapın: "))

if secim == 1:
	second = int(input("Saniye Giriniz: "))



	while second != 0:
		time.sleep(1)
		second -= 1
		print(f"Geri Sayımın Bitmesine {second} Saniye Kaldı")


if secim == 2:
	second = 0
	minute = 0
	while True:
		time.sleep(1)
		second += 1
		if second == 60:
			second = 0
			minute += 1
		print(f"{minute} Dakika, {second} Saniye Geçti.")	



