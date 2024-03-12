from MinuOmaModul import *
from random import *

#(1) arithmetic() funktsiooni kasutamine
v=arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Operatsioon: "))
print(v)

#(2) liigaasta
vastus=is_year_leap(int(input("Aasta: ")))
if vastus:
    print("Liigaasta")
else:
    print("Tavaline aasta")

a=[]
b=[]
for i in range(5):
    a.append(randint(-20,20))
for i in range(1,4):
    arv=int(input(f"{i}. arv "))
    b.append(arv)
print(a)
print(b)
print()
Suurim_element(a,b)

a=randint(-10,10)
print("Esimene arv=",a)
b=float(input("Teine arv:"))
kor=Korrutis(a,b,5.5)
print("Tulemus: ",kor)
kor=Korrutis(b,a,b,10)
print(f"Tulemus: {b}*{a}*{b}*10=",kor)
