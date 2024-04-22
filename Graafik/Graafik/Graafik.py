from tkinter import *
import matplotlib.pyplot as plt #Y funktsiooni loomiseks
import numpy as np #X vahemik X[nim,max]
def Vaal():
    """Joonestatakse vaal paraabolite abil matplotlib mooduli kasutades
    """
    x1=np.arange(0,9,0.5)
    y1=(2/27)*x1**2-3
    x2=np.arange(-10,0,0.5)
    y2=0.04*x2**2-3
    x3=np.arange(-9,-3,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,8.3,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-9,0.5)
    y7=-0.75*(x7+11)**2+6
    x8=np.arange(-15,-13,0.5)
    y8=-0.5*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5) #min max step
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,"r:*",x2,y2,"m-s",x3,y3,"c--D",x4,y4,"y-.H",x5,y5,"g:h",x6,y6,"w-s",x7,y7,"m-s",x8,y8,"m-s",x9,y9,"m-s",x10,y10,"m-s")
    #for i in range(1,11):
    #    plt.plot(eval(f"x{i}"),eval(f"y{i}"),"b--x")
    plt.title("Vaal")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

def valik(event):
    eval(f"{loetelu.get(loetelu.curselection())}()")

    
aken=Tk()
aken.geometry("400x500")
aken.title("Akna pealkiri")
aken.configure(bg="#13e0eb")
l=["Vaal","Vihmavari","Liblikas","Prillid","Kilpkonn"]
loetelu=Listbox(aken,font="Arial 30",fg="green",bg="gold",selectborderwidth=3,selectbackground="lightblue")
for i in range(len(l)):
    loetelu.insert(i,l[i])

loetelu.grid()
loetelu.bind("<Double-1>",valik)

aken.mainloop()
