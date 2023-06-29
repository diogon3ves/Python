from tkinter import*
import math

def sair():
    romaneio.destroy()
def calculo():
    ent1 = float(entrycabeca.get())
    ent2 = float(entrypeso.get())
    ent3 = float(entryapro.get())
    ent4 = float(entryarrob.get())
    ent5 = float(entryfunru.get())
    
    if(ent1>-1 and ent2>-1 and ent3>-1 and ent4>-1 and ent5>-1):
        aprovpeso = float((ent3*ent2)/100)
        aprovpeso1 = ("%.2f"%aprovpeso)
        appesocb  = float(aprovpeso/ent1)
        appesocb1 = ("%.2f"%appesocb)
        calcarrob = float(appesocb/15)
        calcarrob1 = ("%.2f"%calcarrob)
        vlrcb     = float(calcarrob*ent4)
        vlrcb1 = ("%.4f"%vlrcb)
        total     = float(vlrcb*ent1)
        total1 = ("%.2f"%total)
        funru     = float((ent5*total)/100)
        funru1 = ("%.2f"%funru)
        totalliq  = float(total-funru)
        totalliq1 = ("%.2f"%totalliq)
        vlr = Tk()
        vlr.resizable(0,0)
        vlr.title("RESULTADO ROMANEIO")
        vlr.geometry("425x355")
         
        #aproveitamento#
        lbaprovpeso1 = Label(vlr,text="PESO LIQUIDO",font="COURIER 20").place(x=0,y=0)
        lbaprovpeso = Label(vlr,text="",font="COURIER 20")
        lbaprovpeso.place(x=260,y=0)
        lbaprovpeso ["text"] = (aprovpeso1)
    

        layout1 = Label(vlr,text="="*99).place(x=0,y=30)
        
        #peso medio#
        lbpeso1 = Label(vlr,text="MÉDIA KG",font="COURIER 20").place(x=0,y=50)
        lbpeso = Label(vlr,text="",font="COURIER 20")
        lbpeso.place(x=260,y=50)
        lbpeso ["text"] = (appesocb1)

        layout2 = Label(vlr,text="="*99).place(x=0,y=80)
        
        #@#
        lbarrob1 = Label(vlr,text="MÉDIA @",font="COURIER 20").place(x=0,y=100)
        lbarrob = Label(vlr,text="",font="COURIER 20")
        lbarrob.place(x=260,y=100)
        lbarrob ["text"] = (calcarrob1)

        layout3 = Label(vlr,text="="*99).place(x=0,y=130)
        
        #R$ CB#
        lbvlrcb1 = Label(vlr,text="VALOR CB",font="COURIER 20").place(x=0,y=150)
        lbvlrcb = Label(vlr,text="",font="COURIER 20")
        lbvlrcb.place(x=260,y=150)
        lbvlrcb ["text"] = (vlrcb1)

        layout4 = Label(vlr,text="="*99).place(x=0,y=180)

        #TOTAL BRUTO#
        lbtotal1 = Label(vlr,text="TOTAL BRUTO",font="COURIER 20").place(x=0,y=200)
        lbtotal = Label(vlr,text="",font="COURIER 20")
        lbtotal.place(x=260,y=200)
        lbtotal ["text"] = (total1)

        layout5 = Label(vlr,text="="*99).place(x=0,y=230)
        
        #FUNRURAL#
        lbfunru1 = Label(vlr,text="FUNRURAL",font="COURIER 20").place(x=0,y=250)
        lbfunru = Label(vlr,text="",font="COURIER 20")
        lbfunru.place(x=260,y=250)
        lbfunru ["text"] = (funru1)
        
        layout1 = Label(vlr,text="="*99).place(x=0,y=280)
        
        #TOTAL LIQUIDO#
        lbliq1 = Label(vlr,text="TOTAL LIQUIDO",font="COURIER 20").place(x=0,y=300)
        lbliq = Label(vlr,text="",font="COURIER 20")
        lbliq.place(x=260,y=300)
        lbliq ["text"] = (totalliq1)

        

        


        
#MENU#
romaneio = Tk()
romaneio['bg'] = "DARK GREY"
romaneio.title("ROMANEIO")
romaneio.resizable(0,0)
romaneio.geometry("300x400")
layout = Label(romaneio,text="="*99, bg="DARK GREY").place(x=0,y=70)


#LABEL ROMANEIO#
romaneiotitle = Label(romaneio,text="ROMANEIO", font="IMPACT 40", bg="DARK GREY")
romaneiotitle.pack()

#ENTRADAS#

#CABEÇA#
labelcabeca = Label(romaneio,text="QDT. CABEÇA",font="COURIER 18", bg="DARK GREY").place(x=20,y=100)
entrycabeca = Entry(romaneio,width=10)
entrycabeca.place(x=185,y=106)

#PESO BRUTO#
labelpeso   = Label(romaneio,text="PESO BRUTO",font="COURIER 18", bg="DARK GREY").place(x=20,y=150)
entrypeso = Entry(romaneio,width=10)
entrypeso.place(x=185,y=156)

#APROVEITAMENTO#
labelapro   = Label(romaneio,text="APROVEIT.%",font="COURIER 18", bg="DARK GREY").place(x=20,y=200)
entryapro = Entry(romaneio,width=10)
entryapro.place(x=185,y=206)

#VALOR ARROBA#
labelarrob   = Label(romaneio,text="VALOR @",font="COURIER 18", bg="DARK GREY").place(x=20,y=250)
entryarrob = Entry(romaneio,width=10)
entryarrob.place(x=185,y=256)


#FUNRURAL#
labelfunru   = Label(romaneio,text="FUNRURAL %",font="COURIER 18", bg="DARK GREY").place(x=20,y=300)
entryfunru = Entry(romaneio,width=10)
entryfunru.place(x=185,y=306)

#BOTAO#

calcular = Button(romaneio,text="CALCULAR",padx=20,command=calculo)
calcular.place(x=25,y=350)

sair = Button(romaneio,text="SAIR",padx=30,command=sair)
sair.place(x=160,y=350)

romaneio.mainloop()
