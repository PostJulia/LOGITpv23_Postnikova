print("***NUMBER MÄNGU ***")
print()
#Kuuendas reas puudus sulg ja oli üleliigne. Ja puudus break
while 1:
    try:
        a=abs(int(input("Sisestage täisarv => ")))
        break
    except ValueError:
         print("See ei ole täisarv")
         break
#Kolmekümne neljandal puudus jämesool ja kolmekümne kaheksandal oli vaja Pluss ümber korraldada
if a==0:
    print("Nulliga pole mõtet midagi teha")
else:
#Üheksateistkümnendal ja kahekümnendal real peaks olema täpselt üleliigne, kahekümne esimesel peaks olema koolon ning kahekümne kolmandal ja kahekümne viiendal oli vaja plussid ümber korraldada
    print("Määrake, kui palju on paaris ja mitu paaritu numbrit")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b>0:
        if b%2==0:
            paaris+=1
        else:
            paaritu+=1
        b=b//10
    print("Isegi numbrid:", paaris)
    print("Kummalised numbrid:", paaritu)
    print()
#Kolmekümne neljandal puudus jämesool ja kolmekümne kaheksandal oli vaja Pluss ümber korraldada
    print("*Pöörake* sisestatud number ümber")
    print()
    b=0
    while a>0:
        number=a%10
        a=a//10
        b=b*10
        b+=number
    print("*Pööratud* number", b)
    print()
#Neljakümne neljandal puudus veel üks täpselt ja ka neljakümne kaheksandal pidi see olema siis, kui C on suurem kui üks. Samuti oli vaja funktsiooni veidi muuta ja Kohad ümber korraldada
    print("Syracuse hüpoteesi testimine")
    print()
    if c%2==0:
        print("s on paarisarv. Jagage 2 -ga.")
    else:
        print("s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
    while c>1:
        if c%2:
            c=3*c+1
        c//=2
        print(c)
    print()
    print("Hüpotees on õige")


