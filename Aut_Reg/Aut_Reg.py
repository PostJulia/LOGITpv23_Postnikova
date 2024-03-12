from MinuOmaMoodul import *

salasõnad=loe_failist("Salasõnad.txt")
kasutajanimed=loe_failist("Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv "))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad ")
        if vastus=="nimi":
            kasutajanimed=muutmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=muutmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=muutmine(kasutajanimed)
            print("Parooli muutmine: ")
            salasõnad=muutmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")
        kasutajanimed,salasõnad=taastamine(kasutajanimed,salasõnad)
    elif vastus==5:
        print("Lõpetamine")
        Salasõnad.txt=registreerimine(muutmine(Salasõnad:str,salasõnad=[])):
        Kasutajad.txt=registreerimine(muutmine(Kasutajad:str,kasutajanimed=[])):
        f=open(Salasõnad,'a', encoding="utf-8")
        f=open(Kasutajad,'a', encoding="utf-8")
        f.close()
        break
    else:
        print("Tundmatu valik")
