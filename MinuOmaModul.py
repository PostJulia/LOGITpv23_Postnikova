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
