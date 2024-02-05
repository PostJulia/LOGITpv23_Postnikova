nimed=["Mati","Kati","Mati","Mati","Kadri"]
while True:
    valik=input("Andmete lisamine-add\nAndmete nätamine-show\nAndmete kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndmete sortimine-sort\nAndmete otsing-ots\n").lower()
    if valik=="add":
        valik=input("\tKas lisame mitu inimest(mitu) või positsioomile(pos)\n").lower()
        try:
            if valik=="mitu":
                mitu=int(input("Mitu inimest lisame? "))
                for i in range(mitu):
                    nimi=input("Sisesta nimi: ").capitalize()
                    nimed.append(nimi)      
        except :
            else:
                indeks=int(input("Kuhu lisamine? "))
                nimi=input("Mis nimi: ").capitalize()
                nimed.insert(indeks-1,nimi)
    elif valik=="del":
        valik=input("Kas kustutame nimi(nimi) või indeksi järgi(ind)?\n").lower()
        if valik=="nimi":
            nimi=input("Mis nimi on vaja kustutada? ").capitalize()
            kogus=nimed.count(nimi)
            if kogus>0:
                for i in range(kogus):
                    nimed.remove(nimi)
            else:
                print(f"Nimi {nimi} ei ole nimekirjas")
        else:
            indeks=int(input("Mis on järjekorranumber?"))
            nimed.pop(indeks-1)
    elif valik=="show":
        print(nimed)
    elif valik=="rev":
        nimed.reverse()
        print(nimed)
    elif valik=="sort":
        nimed.sort()
        print(nimed)
    elif valik=="clear":
        nimed.clear()
        print(nimed)
    elif valik=="ots":
        ind=-1
        nimi=input("Mis nime otsime? ").capitalize()
        if nimed.count(nimi)>0:
            for nim in nimed:
                if nim==nimi:
                    ind=nimed.index(nimi,ind+1)
                    print(f"{nimi} on indeksiga {ind}")
        else:
            print(f"{nimi} ei ole nimekirjas")

