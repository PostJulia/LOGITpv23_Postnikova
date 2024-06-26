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
    arvamine=[sisestus.get().upper() for sisestus in sisestused[üritus]]
    
    if len(arvamine)!=5:
        silt.config(text="Sisestage täpselt 5 tähte!", fg="#ff0000")  
        return
    
    tulemus=kontrolli(arvamine, hetke)
    liidest(arvamine, tulemus)

    if arvamine==list(hetke) or üritus == 5:
        if arvamine!=list(hetke):
            silt.config(text=f"Õige sõna: {''.join(hetke)}", fg="#ff0000")  
        else:
            silt.config(text="")
        for sisestusrida in sisestused:
            for sisestus in sisestusrida:
                sisestus.config(state='disabled')
    else:
        üritus += 1
        jäänud.config(text=f"Jäänud püüdeid: {6 - üritus}")
        for sisestus in sisestused[üritus]:
            sisestus.focus_set()

def algus():
    global hetke, üritus
    hetke=vali(sõnad)
    üritus=0
    jäänud.config(text="")
    silt.config(text="")

    for sisestusrida in sisestused:
        for sisestus in sisestusrida:
            sisestus.config(state='normal')
            sisestus.delete(0, 'end')

def sisesta_täht(täht):
    focused=aken.focus_get()
    if focused:
        focused.insert(tk.END, täht)

sõnad=laadi('Sõnad.txt')
hetke=vali(sõnad)
üritus=0

aken=tk.Tk()
aken.title("Wordle")
aken.geometry("1000x1000")  
aken.config(bg='#87ceeb')

põhiraam=tk.Frame(aken, bg="#87ceeb")
põhiraam.pack(expand=True)

sisestused=[[tk.Entry(põhiraam, font=('Tahoma', 24), width=4, bg="#928aff", fg="#87ceeb", bd=2, relief=tk.GROOVE) for _ in range(5)] for _ in range(6)]
for i, rida in enumerate(sisestused):
    for j, sisestus in enumerate(rida):
        sisestus.grid(row=i, column=j, padx=3, pady=5)

saatmis=tk.Button(põhiraam, text="Saada", command=saatmine, bg="#928aff", fg="#87ceeb")
saatmis.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

jäänud=tk.Label(põhiraam, text="", font=('Tahoma', 24), bg="#87ceeb", fg="#ffffff")  
jäänud.grid(row=7, column=0, columnspan=5, padx=10, pady=5)

silt=tk.Label(põhiraam, text="", font=('Tahoma', 24), bg="#87ceeb", fg="#ffffff")  
silt.grid(row=8, column=0, columnspan=5, padx=10, pady=5)

nupp=tk.Button(põhiraam, text="Alusta uuesti", command=algus, bg="#928aff", fg="#87ceeb")
nupp.grid(row=6, column=1, columnspan=9, padx=5, pady=5)

tähestik="a b d e f g h i j k l m n o p r s š z ž t u v õ ä ö ü".split()
alphabet_frame=tk.Frame(põhiraam, bg="#87ceeb")
alphabet_frame.grid(row=9, column=0, columnspan=5, pady=5)
for i, täht in enumerate(tähestik):
    tk.Button(alphabet_frame, text=täht, font=('Tahoma', 12), width=2, bg="#928aff", fg="#87ceeb", bd=2, relief=tk.GROOVE, command=lambda t=täht: sisesta_täht(t)).grid(row=0, column=i, padx=3)

aken.mainloop()