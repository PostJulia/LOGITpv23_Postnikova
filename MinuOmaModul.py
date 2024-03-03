def Korrutis(arv1:float,arv2:float,arv3:float,arv4=1.0)->float:
    """Funktsioon tagastab 4 arvude korrutis, arvud sisestab kasutaja. Vaikimisi arv4=1.0. Tulemus tagastatakse float formaadis.

    :param float arv1: sisestatakse nagu parameeter
    :param float arv2: sisestatakse nagu parameeter
    :param float arv3: sisestatakse nagu parameeter
    :param float arv4: sisestatakse nagu parameeter,vaikimisi võrdub ühega
    :rtype:float
    """
    k=arv1*arv2*arv3*arv4
    return k
def Suurim_element(arvud1:list,arvud2:list):   #->any
    """Funktsioon kuvab ekraanile suurim arv listidest.
    
    :param list arvud1: Arvude loetelu
    :param list arvud2: Arvude loetalu
    #:rtype:any
    """
    suurim1=max(arvud1)
    suurim2=max(arvud2)
    suurim=max(suurim1,suurim2)
    #return suurim
    print(suurim)

#1 Простейшие арифметические операции
def summa(arv1:int, arv2:int, arv3 = 0) -> int:
    """ Funksioon tagastab kolme arvu summa
    Summa(arv1, arv2, arv3)
    :param int arv1: arv1 sisetab kasutaja:
    :param int arv2: arv2 sisetab kasutaja:
    :param int arv3: arv3 sisetab kasutaja:
    rtupe: int
    """
    s = arv1 + arv2 + arv3
    return 

def arithmetic(arv1,arv2,sümbol):
    if sümbol=="+":
        s=arv1+arv2
    elif sümbol=="-":
        s=arv1-arv2
    elif sümbol=="*":
        s= arv1*arv2
    elif sümbol == "/":
        if arv2 == 0:
            print("vale andmed(null)")
        else:
             s = arv1 / arv2  
    elif sümbol == "*":
        s = arv1 * arv2       
        return s

#2 Високосный год
def is_year_leap(aasta: int)->bool:
    """Functioon otsustab  kas aasta on liigaasta või ei ole.
    Tagastad True kui aasta on liigaasta ja False kui on tavaline aasta.
    Tagastad True kui aasta on liipaasta ja False kui aasta on tavaline aasta.
    param int aasta: Aasta sisestab kasutaja
    rtupe: bool
    """
    if aasta==0 and aasta%4==0 and aasta%100!=0:
        return
    else:
        return False

#3 Квадрат
from math import *
def square(külg:float)->any:
    """Funktsioon, mis arvutab ruudu perimeetri, pindala ja diagonaali.
      param float külg: ruudu küljed Sisestab kasutaja
      rtupe: any
    """
    S=külg**2
    P=4*külg
    d=külg*sqrt(2)
    return S,P,d

#4 Времена года
from math import *
def season(a:int)->str:
    """Funktsioon, mis tagastab kuu numbri
    pohjal vastava aastaaja.
    param int a:  kuu number Sisestab kasutaja
    rtupe: str
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12, Sisesta veel kord number: "))
            except:
                print("Vigaadnmedmetüübiga")
    if a>2 and a<6:
        s="kevad"
    elif a>5 and a<9:
        s="suvi"
    elif a>8 and a<12:
        s="kevad"
    else:
        s="talv"
    return(s)
#5 Банковский вклад
def bank(a:int, years:int)->int:
    """Funktsioon, mis aktsepteerib hoiuse suurust ja
    aastate arvu ning tagastab summa kasutaja kontol.
    param int a: hoius summas a eurot Sisestab kasutaja
    param years: aastased Sisestab kasutaja
    rtupe: int
    """
    for year in range(years):
        a *= 1.1
    return a
#6 Простые числа
def is_prime(arv:int)->bool:
    """Funktsioon, mis kontrollib, kas arv on lihtne.
    Tagastad True, kui arv on lihtne 
    Tagastad False, kui arv ei ole lihtne
    param int arv: Sisestab kasutaja
    rtupe: bool
    """
    if arv == 1:
        return False
    for divisor in range(2, arv):
        if arv % divisor == 0:
            return False
    return True
#7 Правильная дата
def date(päeval:int, kuu:int, aastal:int)->bool:
    """Funktsioon, mis kontrollib, 
    kas selline kuupäev on meie kalendris olemas.
    Tagastad True, kui kuupäev on olemas.
    Tagastad False, kui kuupäev ei ole olemas.
    param int päeval: Sisestab kasutaja
    param int kuu: Sisestab kasutaja
    param int aastal: Sisestab kasutaja
    rtupe: bool
    """
    kuu_päev = {1: 31,
                    2: 29 if is_year_leap(aastal) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= kuu <= 12 and 1 <= päeval<= kuu_päev[kuu]:
        return True
    return False
