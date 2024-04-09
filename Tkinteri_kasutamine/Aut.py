from tkinter import *
from tkinter import messagebox as mb

def tehtudvalik(var, nimi, text):
    f=var.get()
    if f:
        text.configure(show="")
        nimi.configure(image=pilt1)
    else:
        text.configure(show="*")
        nimi.configure(image=pilt2)
def aut():
    kasutajanimi=kasutaja.get()
    parool=texbox.get() 
    if (kasutajanimi,parool) in kasutajad:
        mb.showinfo("Autentimine", f"Tere tulemast, {kasutajanimi}!")
    else:
        mb.showerror("Autentimine", "Kasutajanimi ei ole registreeritud!")
def reg():
    kasutajanimi2=kasutaja2.get()
    parool2=texbox2.get()
    if (kasutajanimi2,parool2) not in kasutajad:
        kasutajad.append((kasutajanimi2,parool2))
        mb.showinfo("Registreerimine", f"Kasutaja {kasutajanimi2} registreeritud!")
    else:
        mb.showerror("Registreerimine", "Kasutajanimi on juba registreeritud!")
def muuda():
    kasutajanimi_uus=kasutaja_muuda.get()
    parool_uus=texbox_muuda.get()
    uus_kasutaja_info=(kasutajanimi_uus, parool_uus)
    vana_kasutaja_info=(kasutaja.get(), texbox.get())
    if vana_kasutaja_info in kasutajad:
        kasutajad.remove(vana_kasutaja_info)
        kasutajad.append(uus_kasutaja_info)
        mb.showinfo("Muuda nime ja paroolit", "Kasutaja andmed edukalt muudetud!")
    else:
        mb.showerror("Muuda nime ja paroolit", "Sellist kasutajat ei leitud!")
aken=Tk()
aken.geometry("700x700")
aken.title("Autoriseerimine või registreerimine")
aken.configure(bg="#08ffa8")
aken.iconbitmap("ico.ico")
kasutajad=[]
pealkiri=Label(aken, text="Autoriseerimine", bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", justify=CENTER, height=1, width=50)
raam=Frame(aken)
kasutaja=Entry(raam, bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", width=16)
texbox=Entry(raam, bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", width=16, show="*")
pilt1=PhotoImage(file="3.png")
pilt2=PhotoImage(file="4.png")
var=BooleanVar()
valik=Checkbutton(raam, image=pilt2, variable=var, onvalue=True, offvalue=False, command=lambda: tehtudvalik(var,valik,texbox))
nupp=Button(raam, text="Sisenema", bg="#08ffd2", fg="#13ad9e", cursor="star", width=16, command=aut)
pealkiri2=Label(aken, text="Registreerimine", bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", justify=CENTER, height=1, width=50)
raam2=Frame(aken)
kasutaja2=Entry(raam2, bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", width=16)
texbox2=Entry(raam2, bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", width=16, show="*")
valik2=Checkbutton(raam2, image=pilt2, variable=var, onvalue=True, offvalue=False, command=lambda: tehtudvalik(var,valik2,texbox2))
nupp2=Button(raam2, text="Registreerima", bg="#08ffd2", fg="#13ad9e", cursor="star", width=16, command=reg)
pealkiri3 = Label(aken, text="Muuda nime ja paroolit", bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", justify=CENTER, height=1, width=50)
raam3 = Frame(aken)
kasutaja_muuda = Entry(raam3, bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", width=16)
texbox_muuda = Entry(raam3, bg="#08ffd2", fg="#13ad9e", cursor="star", font="Kunstler_Script 16", width=16, show="*")
nupp_muuda = Button(raam3, text="Muudab nime ja paroolit", bg="#08ffd2", fg="#13ad9e", cursor="star", width=16, command=muuda)
pealkiri.pack()
raam.pack()
kasutaja.grid(row=0, column=0)
texbox.grid(row=0, column=1)
valik.grid(row=0, column=2)
nupp.grid(row=0, column=3)
pealkiri2.pack()
raam2.pack()
kasutaja2.grid(row=0, column=0)
texbox2.grid(row=0, column=1)
valik2.grid(row=0, column=2)
nupp2.grid(row=0, column=3)
pealkiri3.pack()
raam3.pack()
kasutaja_muuda.grid(row=0, column=0)
texbox_muuda.grid(row=0, column=1)
nupp_muuda.grid(row=0, column=2)
aken.mainloop()