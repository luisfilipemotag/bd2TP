import psycopg2
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import MenuADU

class AConsumo:

    def __init__(self, master):
        self.master = master
        master.title("Adicionar Consumo")
        master.geometry("600x700")
        master.configure(background='green')
        

      
         #-----------------------------ITEMS----------------------------
        Items = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("Select * from listar_itens_comida")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         Items.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #------------------------------------------------------------------

        
        #-----------------------------Restaurante--------------------------
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
        #-----------------------------------------------------------------

        #-----------------------------Clientes----------------------------
        Clientess = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("SELECT * FROM  public.listar_restaurantes")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         Clientess.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        #------------------------------------------------------------------

        #-----------------------------Clientes-----------------------------
        Clientess = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("SELECT nif FROM public.listar_clientes;")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         Clientess.append(item[0])
        
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



        self.labelR = Label(master, text="Funcionario : " , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
      
        self.comboDS = Combobox(master ,  width = 600)
        self.comboDS.pack()
        self.comboDS.bind('<<ComboboxSelected>>', self.comboDS.get())

        self.labelR = Label(master, text="Cliente :" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        self.comboA = Combobox(master , values = Clientess,  width = 600)
        self.comboA.pack()
        self.comboA.bind('<<ComboboxSelected>>', self.comboA.get())
        
        self.labelR = Label(master, text="" , height = 2, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
 
        self.btnlogin = Button(master, text="Refresh local de consumo e empregado ", command=lambda: self.refresh(), height = 1, width = 100)
        self.btnlogin.pack()

        self.labeli = Label(master, text="Local consumo:" , height = 2, width = 600)
        self.labeli.pack()
        self.labeli.configure(  background='green')

        self.Lconsumo = Combobox(master ,  width = 600)
        self.Lconsumo.pack()
        self.Lconsumo.bind('<<ComboboxSelected>>', self.Lconsumo.get())
      

        self.labeli = Label(master, text="Items:" , height = 2, width = 600)
        self.labeli.pack()
        self.labeli.configure(  background='green')

        self.Items = Combobox(master,values=Items ,  width = 600)
        self.Items.pack()
        self.Items.bind('<<ComboboxSelected>>', self.comboA.get())
      


        self.btnlogin = Button(master, text="Adicionar Ementa" , command=lambda: self.Inserts() , height = 1, width = 100)
        self.btnlogin.pack()
        self.btnlogin = Button(master, text="Voltar", command=lambda: self.new_window4(), height = 1, width = 100)
        self.btnlogin.pack()


    def refresh(self ):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
        a = []
        b = []
        
        curs.execute("SELECT public.listar_l_consumo('"+str(self.IdRest())+"')")
        resta = curs.fetchall()  
        i=0
        for item in resta :
         a.append(item[0])
        
         i+1
        curs.execute("SELECT public.mostrar_funcionarios_restaurante('"+str(self.IdRest())+"')")
        resta = curs.fetchall()  
        i=0
        for item in resta :
         b.append(item[0])
        
         i+1
        curs.close()
        connection.close()


        self.Lconsumo.configure(value=a)
        self.comboDS.configure(value=b)

    def new_window4(self):
     self.master.destroy() 
     self.master = tk.Tk() 
     self.app = Index_Ger_V.IndexGer(self.master) 
     self.master.mainloop()     
    
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
    
    def idItens(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT saber_id_item_nome('"+self.Items.get()+"')")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val  

    def idCliente(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT public.saber_id_cliente('"+self.comboA.get()+"')")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val  
    
    def idFuncionario(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT public.saber_id_funcuinario('"+self.comboDS.get()+"')")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val  

    def idConsumo(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT max FROM public.saber_id_consumo;")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val  

    def idLocalConsumo(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT public.saber_id_l_consumo('"+self.Lconsumo.get()+"',"+ str(self.IdRest()) +")")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val  
       
    def Inserts(self  ):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
      
       curs.execute("CALL public.insertconsumo("+ str(self.idLocalConsumo()) +","+ str(self.idFuncionario()) +","+ str(self.idCliente()) +")")
    
       connection.commit()
       curs.close()
       connection.close()

       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("CALL public.insertconsumo_itens("+ str(self.idConsumo()) +","+ str(self.idItens()) +")")
      
       connection.commit()
       curs.close()
       connection.close()   

    
      