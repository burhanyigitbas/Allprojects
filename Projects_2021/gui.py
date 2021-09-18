from tkinter import *
from tkinter import messagebox
import pywhatkit as py

pencere=Tk()

pencere.title("Whatsapp Bot")

pencere.geometry("600x300")

l1=Label(pencere,text="Numara:",font=(14))
l2=Label(pencere,text="Mesaj  :",font=(14))
l3=Label(pencere,text="Saat    :",font=(14))
l4=Label(pencere,text="Dakika :",font=(14))

l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)
l3.grid(row=2,column=0,padx=5,pady=5)
l4.grid(row=3,column=0,padx=5,pady=5)

numara=StringVar()
mesaj=StringVar()
saat=IntVar()
dakika=IntVar()

t1=Entry(pencere,textvariable=numara,font=(14))
t2=Entry(pencere,textvariable=mesaj,font=(14))
t3=Entry(pencere,textvariable=saat,font=(14))
t4=Entry(pencere,textvariable=dakika,font=(14))

t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)
t4.grid(row=3,column=1)

def login():

	numara1 = numara.get()
	mesaj1 = mesaj.get()
	saat1 = saat.get()
	dakika1 = dakika.get()
	int(saat1)
	int(dakika1)
	
	py.sendwhatmsg(numara1,mesaj1,saat1,dakika1)


def cancel():
	status=messagebox.askyesno(title="Çıkış",message="Gerçekten Çıkmak İstiyor Musun?")
	if status==True:
		pencere.destroy()

	else:
		messagebox.showwarning(title="Uyarı Mesajı",message="Lütfen Yeniden Gönderin!!")







b1=Button(pencere,command=login,text="Gönder",font=(14))
b2=Button(pencere,command=cancel,text="Çıkış",font=(14))
b1.grid(row=5,column=1,sticky=W)
b2.grid(row=5,column=1,sticky=E)



pencere.mainloop()