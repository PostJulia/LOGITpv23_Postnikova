from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
    else:
        texbox.configure(show="*")
def textpealkirjasse():
    vastus=mb.askquestion("Küsimus","Kas tõesti tahad info kopeerida?")
    if vastus=='yes':
        mb.showwarning("Tähelepanu","Kohe teiseldatakse info!")
        t=texbox.get()
        pealkiri.configure(text=t)
        texbox.delete(0,END)
    else:
        mb.showinfo("Valik oli tehtud","Info jääb omal kohal")
        nimi=sd.askstring("Saame tuttavaks!","Mis on sinu nimi?") #askinteger(),askfloat()
        pealkiri.configure(text=nimi)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#03c2fc")
aken.iconbitmap("1.ico")
pealkiri=Label(aken,text="Põhielemendid",bg="#0362fc",fg="#03fcf4",cursor="man",font="Kunstler_Script 16", justify=CENTER, height=3, width=26)
raam=Frame(aken)
texbox=Entry(raam,bg="#03fcf4",fg="#0362fc",font="Kunstler_Script 16",width=16,show="*")
pilt=PhotoImage(file="2.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,image=pilt,variable=var,onvalue=True,offvalue=False,command=lambda:tehtudvalik(var))
#valik.deselect()
nupp=Button(raam,text="Vajutaja mind",bg="#0362fc",fg="#03fcf4",width=16,command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0)
valik.grid(row=0,column=1)
nupp.grid(row=0,column=2)
aken.mainloop()
