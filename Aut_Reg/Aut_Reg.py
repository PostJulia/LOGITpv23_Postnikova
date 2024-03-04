from MinuOmaMoodul import *

salasõnad=[]
kasutajanimed=[]
while True:
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
    elif vastus==4:
        print("Unustanud parooli taastamine")
    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
