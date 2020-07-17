import psycopg2
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import MenuADU
import xml.etree.cElementTree as ET

class EmitirFac:

    def __init__(self, master):
        self.master = master
        master.title("Adicionar Consumo")
        master.geometry("600x700")
        master.configure(background='green')
        

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
        #----------------------------------------------------------------

        self.labelR = Label(master, text="Cliente :" , height = 1, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        self.comboA = Combobox(master , values = Clientess,  width = 600)
        self.comboA.pack()
        self.comboA.bind('<<ComboboxSelected>>', self.comboA.get())
        
        self.labelR = Label(master, text="" , height = 2, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
 
       
        self.btnlogin = Button(master, text="Emitir fatura" ,command=lambda: self.EmitirXML(),  height = 1, width = 100)
        self.btnlogin.pack()
        self.btnlogin = Button(master, text="Voltar", command=lambda: self.new_window4(), height = 1, width = 100)
        self.btnlogin.pack()


    def new_window4(self):
     self.master.destroy() 
     self.master = tk.Tk() 
     self.app = Index_Ger_V.IndexGer(self.master) 
     self.master.mainloop()     
    
   
  

    def EmitirXML(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       root = ET.Element("Fatura") 
       doc1 = ET.SubElement(root, "RandR")
       ET.SubElement(doc1, "Cliente").text = self.comboA.get()
       doc = ET.SubElement(root, "Itens")

       curs.execute("SELECT public.mostrar_fatura_itens_custo('"+self.comboA.get()+"')")
       resta = curs.fetchall()  
       for item in resta :
          ET.SubElement(doc, "Item").text = item[0]

       curs.close()
       connection.close()
       tree = ET.ElementTree(root)
       tree.write("fatura_"+self.comboA.get()+".xml")


       connection1 = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curss = connection1.cursor()
       curss.execute(" CALL public.deletecl_consumo('"+self.comboA.get()+"')")
       resta = curss.fetchall()  
       connection1.commit()

       curss.close()
       connection.close()
      

      
    
  

  
      