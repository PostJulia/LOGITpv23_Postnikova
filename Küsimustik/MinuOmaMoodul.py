def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())

        #k.v=line.strip().split(":")
        #kus_vas[k]=v

    fail.close()
    return kus,vas #,kus_vas