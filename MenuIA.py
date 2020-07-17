import psycopg2
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import AddTpItem
import AddAlergia
import EditAlergia
import AddItem


class MenuIA(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title("R&R")
        master.geometry("600x800")
        master.configure(background='green')
        
        self.labelc = Label(master, text="Items:"  , height = 2, width = 600)
        self.labelc.pack()
        self.labelc.configure(background='green')

        self.btnAddI = Button(master, text="Adicionar" , command=lambda: self.AddItem(), height = 2, width = 600)
        self.btnAddI.pack()


        self.labelc = Label(master, text="Tipo de Items:"  , height = 2, width = 600)
        self.labelc.pack()
        self.labelc.configure(background='green')

        self.btnAddI = Button(master, text="Adicionar" , command=lambda: self.AddTItem(), height = 2, width = 600)
        self.btnAddI.pack()

       
        self.labelc = Label(master, text="Tipo de Alergias"  , height = 2, width = 600)
        self.labelc.pack()
        self.labelc.configure(background='green')

        self.btnVercli = Button(master, text="Adicionar" , command=lambda: self.AddAlergia(),height = 2, width = 600)
        self.btnVercli.pack()

        self.btnVerEm = Button(master, text="Update" , command=lambda: self.EditA() , height = 2, width = 600)
        self.btnVerEm.pack()

        
        self.btnVolta = Button(master, text="Voltar" , command=lambda: self.new_window4() , height = 2, width = 600)
        self.btnVolta.pack()
       
   
    def EditA(self):

        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = EditAlergia.EditAlergia(self.master) 
        self.master.mainloop()
    
      
    def AddItem(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = AddItem.AddIten(self.master) 
        self.master.mainloop()

    def AddTItem(self):

        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = AddTpItem.AddTiEmenta(self.master) 
        self.master.mainloop()

    def AddAlergia(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = AddAlergia.AddAlergia(self.master) 
        self.master.mainloop()

    def new_window4(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Index_Ger_V.IndexGer(self.master) 
        self.master.mainloop()
             
    

   
 
   
       

    
    
   