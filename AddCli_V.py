import psycopg2
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2
import MenuADU
class AddUser:

    def __init__(self, master):
        self.master = master
        master.title("Adicionar")
        master.geometry("600x600")
        master.configure(background='green')
     
        txt_nif = StringVar()
        txt_nome = StringVar()
        txt_contacto = StringVar()

        self.labelc = Label(master, text="Nif:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.nif = Entry(master, textvariable=txt_nif  , width = 600)
        self.nif.pack()

        self.labelc = Label(master, text="Nome:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.name = Entry(master, textvariable=txt_nome , width = 600)
        self.name.pack()

        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')

        self.labelc = Label(master, text="Contacto:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.name = Entry(master, textvariable=txt_contacto , width = 600)
        self.name.pack()

        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      


        self.other_button = Button(master, text="criar" , command=lambda:self.inserir( txt_nif ,txt_nome,txt_contacto) , height = 2, width = 600)
        self.other_button.pack()
        
        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.other_button = Button(master, text="Voltar" , command=lambda:self.new_window4(), height = 2, width = 600)
        self.other_button.pack()

    
    
    
    def inserir(self , txt_nif ,txt_nome,txt_contacto):

        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()
       
        curs.execute("call insertCliente ('"+txt_nome.get()+"', '"+txt_nif.get()+"', '"+txt_contacto.get()+"');")
#falta buscar o print do trigger !!!
        connection.commit()
        curs.close()
        connection.close()
        self.labeld = Label( text="criado" , height = 1, width = 600)
        self.labeld.pack()
        self.labeld.configure(  background='green')

    def new_window4(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = MenuADU.MenuCli(self.master) 
        self.master.mainloop()
 
   
       

       

    
      