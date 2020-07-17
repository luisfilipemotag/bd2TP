import psycopg2
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2

class IndexEmp:

    def __init__(self, master):
        self.master = master
        master.title("R&R")
        master.geometry("600x600")
        master.configure(background='green')
        

        self.labelc = Label(master, text="Clientes:" , height = 2, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
        
        self.btnVercli = Button(master, text="Ver Cliente" , height = 2, width = 600)
        self.btnVercli.pack()
        self.btnAddCli = Button(master, text="Adicionar " , height = 2, width = 600)
        self.btnAddCli.pack()

        self.labela = Label(master, text="Ementa:" , height = 2, width = 600)
        self.labela.pack()
        self.labela.configure(  background='green')

        self.btnVerEm = Button(master, text="Ver ementa do dia" , height = 2, width = 600)
        self.btnVerEm.pack()
        
        self.labelC = Label(master, text="Consumo " , height = 2, width = 600)
        self.labelC.pack()
        self.labelC.configure(  background='green')

        self.btnPag = Button(master, text="Pagamento" , height = 2, width = 600)
        self.btnPag.pack()
      

             

 
   
       

    
    
   