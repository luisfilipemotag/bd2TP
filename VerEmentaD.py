import psycopg2
import tkinter as tk
from tkinter import * 
from tkinter.ttk import Combobox
import os
import psycopg2

import Index_Ger_V


class VEm(tk.Frame):
    def __init__(self, master):
     
        self.master = master
        
        master.title("Clientes")
        master.geometry("600x600")
        master.configure(background='green')
        

         #-----------------------Dia da semana------------------------------
        Dsemana = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("SELECT * FROM listar_data_dia")
        rti = curs.fetchall()  
        i=0
        for item in rti :
         Dsemana.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #-----------------------------------------------------------------

        #-----------------------------Pdia----------------------------
        PDia = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("SELECT * FROM listar_data_periodo")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         PDia.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #------------------------------------------------------------------


         #-----------------------------Restaurante----------------------------
        TRr = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("SELECT * FROM  public.listar_restaurantes")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         TRr.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #------------------------------------------------------------------

        self.labelR = Label(master, text="Restaurante" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
      
        self.comboRest = Combobox(master,values=TRr ,  width = 600)
        self.comboRest.pack()
        self.comboRest.bind('<<ComboboxSelected>>', self.comboRest.get())


        self.labelR = Label(master, text="Dia da semana" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
      
        self.comboDS = Combobox(master,values=Dsemana ,  width = 600)
        self.comboDS.pack()
        self.comboDS.bind('<<ComboboxSelected>>', self.comboDS.get())


        self.labelR = Label(master, text="Periodo do dia :" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        self.comboA = Combobox(master,values=PDia ,  width = 600)
        self.comboA.pack()
        self.comboA.bind('<<ComboboxSelected>>', self.comboA.get())






       
        self.other_button = Button(master, text="mostrar ementa" ,command=lambda:self.show(),  height = 2, width = 600)
        self.other_button.pack()
        self.other_button = Button(master, text="mostrar ementa da semana" ,command=lambda:self.showAll(),  height = 2, width = 600)
        self.other_button.pack()
       
        self.Lb1 = Listbox()
        self.other_button = Button(master, text="voltar" , command=lambda:self.new_window() , height = 2, width = 600)
        self.other_button.pack(side=BOTTOM)
       
    def dataid(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT public.saber_id_data('"+self.comboDS.get()+"','"+self.comboA.get()+"')")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val     
  
    def IdRest(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT public.saber_id_restaurante('"+self.comboRest.get()+"')")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val    

    def PlatoDDia(self,v):
        if v == 1 : 
         return 'Prato do dia'
        else:
         return "Nao e prato do dia"     
        
       
    def show(self):

        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()
        print(str(self.dataid()))
        curs.execute("select * from mostrar_ementa_dia("+str(self.dataid())+","+str(self.IdRest())+")")
        clientes = curs.fetchall() 
        
        
        self.Lb1.delete(0,END)
        self.Lb1.pack(side="left",fill="both", expand=True)
        
        i=0
        for item in clientes :
           self.Lb1.insert(i ,"Tipo de ementa    "+item[0] ,"Item :  "+item[1] ,"Custo:   "+ str(item[2]),"tipo de refeicao:   "+self.PlatoDDia(item[3])+"\n\n" )
           i+1
        
        
        self.Lb1.pack()
        curs.close()
        connection.close()
      

    def showAll(self):

        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()
        print(str(self.dataid()))
        curs.execute("select * from mostrar_ementa_semana()")
        clientes = curs.fetchall() 
        
        
        self.Lb1.delete(0,END)
        self.Lb1.pack(side="left",fill="both", expand=True)
        
        i=0
        for item in clientes :
           self.Lb1.insert(i ,"Tipo de ementa    "+item[0] ,"Item :  "+item[1] ,"Custo:   "+ str(item[2]),"tipo de refeicao:   "+self.PlatoDDia(item[3])+"\n\n" )
           i+1
        
        
        self.Lb1.pack()
        curs.close()
        connection.close()
      
    def new_window(self):

        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Index_Ger_V.IndexGer(self.master) 
        self.master.mainloop()
    


      