import psycopg2
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import AddCli_V
import DelCli_V
import FaturaCli
import VerCliente_V 
import MenuADU 
import MenuIA
import CriarEmenta
import VerEmentaD
import AdicionarConsumo
import EmitirFatura

class IndexGer(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title("R&R")
        master.geometry("600x600")
        master.configure(background='green')
        

        self.labelc = Label(master, text="Clientes:" , height = 2, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
        
        self.btnAddCli = Button(master, text="Adicionar / Remover / Editar", command=lambda: self.MenuADU() , height = 2, width = 600)
        self.btnAddCli.pack()
        self.btnVercli = Button(master, text="Ver Cliente" , command=lambda: self.VerCliente(),height = 2, width = 600)
        self.btnVercli.pack()

        self.labela = Label(master, text="" , height = 2, width = 600)
        self.labela.pack()
        self.labela.configure(  background='green')



        #-------------------------


        self.labela = Label(master, text="Ementa:" , height = 2, width = 600)
        self.labela.pack()
        self.labela.configure(  background='green')

        self.btnMenuIA = Button(master, text="Items/Alergias" ,command=lambda: self.MenuIA(), height = 2, width = 600)
        self.btnMenuIA.pack()


        #-------------------------
        self.btnVerEm = Button(master, text="Ver ementa da semana " ,command=lambda: self.MostrarE() ,height = 2, width = 600)
        self.btnVerEm.pack()
        self.btnAddEm = Button(master, text="criar ementa" ,command=lambda: self.CriarEmenta(), height = 2, width = 600)
        self.btnAddEm.pack()
        
        self.btnEdEm = Button(master, text="Eliminar Ementa da semana",command=lambda: self.ElimiarEm(), height = 2, width = 600)
        self.btnEdEm.pack()


        self.labelC = Label(master, text="Consumo " , height = 2, width = 600)
        self.labelC.pack()
        self.labelC.configure(  background='green')

          
        self.btnPag = Button(master, text="Adicionar consumo" ,command=lambda: self.Consumos(), height = 2, width = 600)
        self.btnPag.pack()
      
    
        self.labelC = Label(master, text="" , height = 2, width = 600)
        self.labelC.pack()
        self.labelC.configure(  background='green')

    
        self.btnPag = Button(master, text="Pagamento" ,command=lambda: self.FAtura() , height = 2, width = 600)
        self.btnPag.pack()
        self.btnFD = Button(master, text="log out" ,command=lambda: self.endApp(), height = 2, width = 600)
        self.btnFD.pack()

    def endApp(self):
        os._exit(1)

    def VerCliente(self):

        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = VerCliente_V.Vcliente(self.master) 
        self.master.mainloop()

    def MenuADU(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = MenuADU.MenuCli(self.master) 
        self.master.mainloop()

    def MostrarE(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = VerEmentaD.VEm(self.master)
        self.master.mainloop()


    def MenuIA(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = MenuIA.MenuIA(self.master) 
        self.master.mainloop()
    
    def CriarEmenta(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = CriarEmenta.Cementa(self.master) 
        self.master.mainloop()

    def FAtura(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = EmitirFatura.EmitirFac(self.master) 
        self.master.mainloop()
    
    
    def Consumos(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = AdicionarConsumo.AConsumo(self.master) 
        self.master.mainloop()
    
    
    def ElimiarEm(self):
       connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
       curs = connection.cursor()
       
       curs.execute("CALL public.deleteementa_data_item()")
        
       self.labela = Label( text="Eliminou as ementa da semana por favor adicione novas !" , height = 2, width = 600)
       self.labela.pack()
       self.labela.configure(  background='green')


       connection.commit()
       curs.close()
       connection.close()
                
   
             
    

   
 
   
       

    
    
   