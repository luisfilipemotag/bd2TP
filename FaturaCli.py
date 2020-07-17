import psycopg2
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2

class GerFac:

    def __init__(self, master):
        self.master = master
        master.title("Pagamento")
        master.geometry("600x300")
        master.configure(background='green')
     
        txt_nif = StringVar()
        txt_nome = StringVar()


        self.labelc = Label(master, text="Nif:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.nif = Entry(master, textvariable=txt_nif  , width = 600)
        self.nif.pack()

        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        var1 = IntVar()
        self.checkpeixe= Checkbutton(master, text="Peixe", variable=var1 , width = 600)
        self.checkpeixe.pack()

        var2 = IntVar()
        self.checkpeixe= Checkbutton(master, text="Carne", variable=var2 , width = 600)
        self.checkpeixe.pack()

        var3 = IntVar()
        self.checkpeixe= Checkbutton(master, text="Bebida", variable=var3 , width = 600)
        self.checkpeixe.pack()

        var4 = IntVar()
        self.checkpeixe= Checkbutton(master, text="Sobremesa", variable=var4 , width = 600)
        self.checkpeixe.pack()

        self.labelc = Label(master, text="Total:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')

        self.other_button = Button(master, text="Gerar fatura" , height = 2, width = 600)
        self.other_button.pack()
        
        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.other_button = Button(master, text="Voltar" , height = 2, width = 600)
        self.other_button.pack()



 
   
       

       

    
      