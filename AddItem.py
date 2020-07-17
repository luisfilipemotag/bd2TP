import psycopg2
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import MenuIA

class AddIten:

    def __init__(self, master):
        self.master = master
        master.title("Adicionar item")
        master.geometry("600x240")
        master.configure(background='green')
        

        #-----------------------Tipo de Item------------------------------
        Ti = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("select * from listar_tipositens")
        rti = curs.fetchall()  
        i=0
        for item in rti :
         Ti.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #-----------------------------------------------------------------

        #-----------------------------Alergias----------------------------
        A = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("select * from listar_alergias")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         A.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #------------------------------------------------------------------




        self.labelR = Label(master, text="Criar Items" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
        self.labelR = Label(master, text="Nome do Item :" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        self.comboTi = Combobox(master,values=Ti ,  width = 600)
        self.comboTi.pack()
        self.comboTi.bind('<<ComboboxSelected>>', self.comboTi.get())

        self.labelR = Label(master, text="Alergias :" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        self.comboA = Combobox(master,values=A ,  width = 600)
        self.comboA.pack()
        self.comboA.bind('<<ComboboxSelected>>', self.comboA.get())
        
        self.labelR = Label(master, text="Custo :" , height = 2, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
        
        self.passw = Entry(master, width = 600)
        self.passw.pack()


        self.btnlogin = Button(master, text="Adicionar item", command=lambda: self.insert(), height = 1, width = 100)
        self.btnlogin.pack()
        self.btnlogin = Button(master, text="Voltar", command=lambda: self.new_window4(), height = 1, width = 100)
        self.btnlogin.pack()




    def new_window4(self):
     self.master.destroy() 
     self.master = tk.Tk() 
     self.app = MenuIA.MenuIA(self.master) 
     self.master.mainloop()         
   
        
    def getid(self):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
       
        curs.execute("select * from saber_t_item ('"+self.comboTi.get()+"')")
        resta = curs.fetchall()  
        val=0
        i=0
        for item in resta :
           val = item[0]
           i+1
        curs.close()
        connection.close()
        return val 


    def getidAl(self):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
       
        curs.execute("select * from saber_id_alergia('"+self.comboA.get()+"')")
        resta = curs.fetchall()  
        val=0
        i=0
        for item in resta :
           val = item[0]
           i+1
        curs.close()
        connection.close()
        return val 

    def getitem(self):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
       
        curs.execute("select * from saber_id_itens('"+str(self.getid())+"')")
        resta = curs.fetchall()  
        val=0
        i=0
        for item in resta :
           val = item[0]
           i+1
        curs.close()
        connection.close()
        return val 


    def insert(self):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
        
        curs.execute("CALL insertitens("+ str(self.getid()) +","+  str(self.passw.get()) +")")
        
        connection.commit()
        curs.close()
        connection.close()
        self.inserts()

    def inserts(self):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
        print(self.getid())
        curs.execute("CALL insertalergia_item("+ str(self.getitem()) +","+ str(self.getidAl()) +")")
        
        connection.commit()
        curs.close()
        connection.close()
        

        
        
 
   
       

       

    
      