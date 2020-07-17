import psycopg2
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import MenuADU

class Cementa:

    def __init__(self, master):
        self.master = master
        master.title("Adicionar Ementa")
        master.geometry("600x700")
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

         #-----------------------------Tipo refeicao----------------------------
        TR = []
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("SELECT * FROM listar_tipo_ementa")
        ra = curs.fetchall()  
        i=0
        for item in ra :
         TR.append(item[1])
        
         i+1
        curs.close()
        connection.close()
        #------------------------------------------------------------------


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
        
        self.labelR = Label(master, text="" , height = 2, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        var1 = IntVar()
        self.check = Checkbutton(master, text="Prato do dia:", variable=var1)
        self.check.pack()

        self.labely = Label(master, text="Tipo de refeicao :" , height = 2, width = 600)
        self.labely.pack()
        self.labely.configure(  background='green')

        self.TipoR = Combobox(master,values=TR ,  width = 600)
        self.TipoR.pack()
        self.TipoR.bind('<<ComboboxSelected>>', self.TipoR.get())
        

        self.labeli = Label(master, text="Items:" , height = 2, width = 600)
        self.labeli.pack()
        self.labeli.configure(  background='green')

        self.Items = Combobox(master,values=Items ,  width = 600)
        self.Items.pack()
        self.Items.bind('<<ComboboxSelected>>', self.comboA.get())
      


        self.btnlogin = Button(master, text="Adicionar Ementa", command=lambda: self.Inserts(var1.get()), height = 1, width = 100)
        self.btnlogin.pack()
        self.btnlogin = Button(master, text="Voltar", command=lambda: self.new_window4(), height = 1, width = 100)
        self.btnlogin.pack()




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
   
    def TipoEmenta(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT saber_id_t_ementa('"+self.TipoR.get()+"')")
       resta = curs.fetchall()  
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1
       curs.close()
       connection.close()
       return val     
    
    def Itens(self):
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

    def Idementa(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("SELECT * from saber_id_ementa ")
       resta = curs.fetchall()  
       
       
       val=0
       i=0
       for item in resta :
          val = item[0]
          i+1

      
       return val       
        
    def Inserts(self , var1 ):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       if var1 == 0:
          var1 = 1 
       else:
          var1 = 2
       print(  str(self.Idementa()) )
       curs.execute("CALL public.insertementa("+ str(self.TipoEmenta()) +","+ str(var1) +")")
    
       connection.commit()
       curs.close()
       connection.close()

       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       print(  str(self.Idementa()) )
       curs.execute("CALL public.insert_ementa_data("+ str(self.Idementa()) +","+ str(self.dataid()) +")")
       curs.execute("CALL public.insert_ementa_restaurante("+ str(self.IdRest()) +","+ str(self.Idementa()) +")")
       curs.execute("CALL public.insert_ementa_item("+ str(self.Idementa()) +","+ str(self.Itens())  +")")
      
       connection.commit()
       curs.close()
       connection.close()
     

       

       

    
      