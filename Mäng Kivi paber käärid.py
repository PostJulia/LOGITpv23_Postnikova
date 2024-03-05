i=input("Sisesta täht => ")
if(i.isupper()):
    print("See on suur täht", i)
a=input("Sisesta arv => ")
if (a.isdigit()):
    print("See on täisarv ", a)







#import random
#while True:
#    v1=input("Mängija 1, vali märk (kivi/käärid/paber): ").lower()
#    v2=random.choice(["kivi", "käärid", "paber"])
#    print(v2)
    
#    if v1 not in ["kivi", "käärid", "paber"]:
#        print("Vale valik. Palun vali uuesti.")
#        continue

#    if v1==v2:
#        print("Viik!")
#    elif (v1=="kivi" and v2=="käärid") or (v1=="käärid" and v2=="paber") or (v1=="paber" and v2=="kivi"):
#        print("Mängija 1 võidab!")
#    else:
#        print("Mängija 2 võidab!")
        
#    kordus=input("Kas soovite veel mängida? (jah/ei): ").lower()
#    if kordus !="jah":
#        break