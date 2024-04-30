import tkinter as tk
import random

def laadi(sõnad_fail):
    with open(sõnad_fail, 'r', encoding='utf-8') as fail:
        sõnad=[rivi.strip().upper() for rivi in fail if len(rivi.strip())==5]
    return sõnad

def vali(sõnad):
    return random.choice(sõnad)

def kontrolli(arvamine, sõna):
    tulemus=[]
    for i, täht in enumerate(arvamine):
        if täht==sõna[i]:
            tulemus.append("#32CD32")
        elif täht in sõna:
            tulemus.append("#FFFF00")
        else:
            tulemus.append("#080808")
    return tulemus

def liidest(arvamine, tulemus):
    for i, täht in enumerate(arvamine):
        sisestus=sisestused[üritus][i]
        sisestus.delete(0, 'end')
        sisestus.insert('end', täht)
        sisestus.config(disabledforeground=tulemus[i], state='disabled')

def saatmine():
    global üritus, hetke
    arvamine=arvamine_muutuja.get().upper()
    if len(arvamine)!=5:
        tulemus.config(text="Sõna peab olema 5 tähemärki pikk!")
        return
    
    tulemus=kontrolli(arvamine, hetke)
    liidest(arvamine, tulemus)

    if arvamine==hetke or üritus==5:
        if arvamine!=hetke:
            tulemus.config(text=f"Õige sõna: {hetke}", fg="#ff0000")
        else:
            tulemus.config(text="")
        for sisestusrida in sisestused:
            for sisestus in sisestusrida:
                sisestus.config(state='disabled')
    else:
        üritus+=1
        silt.config(text=f"Jäänud püüdeid: {6 - üritus}")
        arvamine_muutuja.set("")

def algus():
    global hetke, üritus
    hetke=vali(sõnad)
    üritus=0
    arvamine_muutuja.set("")
    silt.config(text="")

    for sisestusrida in sisestused:
        for sisestus in sisestusrida:
            sisestus.config(state='normal')
            sisestus.delete(0, 'end')

sõnad=laadi('Sõnad.txt')
hetke=vali(sõnad)
üritus=0

aken=tk.Tk()
aken.title("Wordle")
aken.geometry("400x800")  
aken.config(bg='#87ceeb')

põhiraam=tk.Frame(aken, bg="#87ceeb")
põhiraam.pack(expand=True)

sisestused=[[tk.Entry(põhiraam, font=('Tahoma', 24), width=2, bg="#928aff", fg="#87ceeb") for _ in range(5)] for _ in range(6)]
for i, rida in enumerate(sisestused):
    for j, sisestus in enumerate(rida):
        sisestus.grid(row=i, column=j, padx=10, pady=10)

arvamine_muutuja=tk.StringVar()
arvamine_sisestus=tk.Entry(põhiraam, textvariable=arvamine_muutuja, font=('Tahoma', 24), width=7, bg="#928aff", fg="#87ceeb")
arvamine_sisestus.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

saatmis_nupp=tk.Button(põhiraam, text="Saada", command=saatmine, bg="#928aff", fg="#87ceeb")
saatmis_nupp.grid(row=8, column=0, columnspan=3, padx=5, pady=10)

silt=tk.Label(põhiraam, text="", font=('Tahoma', 24), bg="#87ceeb", fg="#ffffff")  
silt.grid(row=9, column=0, columnspan=5, padx=10, pady=10)


algus_uuesti_nupp=tk.Button(põhiraam, text="Alusta uuesti", command=algus, bg="#928aff", fg="#87ceeb")
algus_uuesti_nupp.grid(row=8, column=1, columnspan=5, padx=5, pady=10)

aken.mainloop()