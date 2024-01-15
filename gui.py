import tkinter as gui
from tkinter import ttk as gui2
import os  as system
import re
from email.message import EmailMessage
import smtplib
import ssl
import pywhatkit as kit
import time

class Path:
    def __init__(self):
        self.imagesFolder = system.path.abspath(system.path.join(system.path.dirname(__file__), '.', 'images'))
        self.dataFolder = system.path.abspath(system.path.join(system.path.dirname(__file__), '.', 'data'))
        self.nameFile = '\dataFile.txt'
    
    def getDatafolder(self):
        return  self.dataFolder + self.nameFile
        
class Data:
    def __init__(self):
        self.users=[]
        self.path= Path()
        self.link = self.path.getDatafolder()
    
    def get(self):
        return self.users
    
    def add(self, element):
        self.users.append(element)
    
    def sort(self):
        self.users.sort()
    
    def set(self,newUser, index):
        self.users[index] = newUser
    
    def delete(self, index):
        self.users.pop(index)

    def writeFile(self, indexfile):
        self.file = open(self.link , 'a')
        self.file.write(self.users[indexfile-1].strfile()+'\n')
        self.file.close()

    def writeFileFull(self):
        self.file = open(self.link , 'w')
        for user in self.users:
            self.file.write(user.strfile())
        self.file.close()
    
    def getLength(self):
        return len(self.users)
    
    def checkFile(self):
        if system.path.exists(self.link):
            self.file = open(self.link,'r')
            for l in self.file:
                self.element = User()
                userLine= l.split(' ')    
                prueba = userLine[1].split(',')
                self.element.setname(prueba[0])
                prueba = userLine[3].split(',')
                self.element.setlastname(prueba[0])
                prueba = userLine[7].split(',')
                self.element.setbirthdate(prueba[0])
                prueba = userLine[9].split(',')
                self.element.setcountry(prueba[0])
                prueba = userLine[11].split(',')
                self.element.setemail(prueba[0])
                prueba = userLine[13].split(',')
                self.element.setteleph(prueba[0])
                self.users.append(self.element)
            self.file.close()
      
class User:
    def __init__(self, ):
        self.name = ""
        self.lastName = ""
        self.birthDate = ""
        self.country = ""
        self.eMail = Email()
        self.telfNumb = Telephone()

    def __str__(self):
        return f'Nombre: {self.name}\n Apellido: {self.lastName}\n Fecha de Nac.: {self.birthDate}\n País: {self.country}\n E-mail: {self.eMail.get()}\n Teléfono: {self.telfNumb.get()}'
    
    def strfile(self):
        return 'Nombre: '+ self.name + ', Apellido: ' + self.lastName + ', Fecha de Nac.: ' + self.birthDate + ', País: ' + self.country + ', E-mail: ' + self.eMail.get() + ', Teléfono: ' + self.telfNumb.get()

    def setname(self,nome):
        self.name = nome

    def getname(self):
        return self.name

    def setlastname(self,lnome):
        self.lastName = lnome

    def getlastname(self):
        return self.lastName
    
    def setbirthdate(self, dob):
        self.birthDate = dob
    
    def getbd(self):
        return self.birthDate
    
    def setcountry(self, land):
        self.country = land
    
    def getcountry(self):
        return self.country
    
    def setemail(self,em):
        self.eMail.set(em)
    
    def getemail(self):
        return self.eMail
    
    def setteleph(self,tlf):
        self.telfNumb.set(tlf)
    
    def gettel(self):
        return self.telfNumb


    def notifyEmail(self):
        self.eMail.send(self.name + " " + self.lastName)
    
    def notifyWS(self):
        self.telfNumb.send(self.name + " " + self.lastName)

class Email:
    def __init__(self):
        self.email = ""

    def set(self, em):
        self.email = em
    
    def get(self):
        return self.email

    def send(self, nombre):
        email_sender = 'herr100j@gmail.com'
        email_password = 'ogbe igch jcpl hdpq'
        email_receiver = self.email

        subject= 'Bienvenido'
        body=("Recibe nuestra bienvenida "+nombre+" a esta aplicación.\n Primero que todo queremos darte las gracias por registrarte.\n A continuación, puedes conocer todos los beneficios que brinda y todo lo demas...")

        em=EmailMessage()
        em['From']= email_sender
        em['To']= email_receiver
        em['Subject']= subject
        em.set_content(body)

        context =ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

class Telephone:
    def __init__(self):
        self.telephone = ""

    def set(self,telf):
        self.telephone =telf
    
    def get(self):
        return self.telephone
    
    def send(self, nombre):
        nmr_ws= self.telephone
        msg= "Recibe nuestra bienvenida "+nombre+" a esta aplicación.\n Primero que todo queremos darte las gracias por registrarte.\n A continuación, puedes conocer todos los beneficios que brinda  y todo lo demás..."
        self.tupleTime = time.localtime(time.time())
        kit.sendwhatmsg(nmr_ws,msg,self.tupleTime.tm_hour, self.tupleTime.tm_min+1, wait_time=20)

class Gui(gui.Tk):
    def __init__(self, msgMain, textBtnStart):
        super().__init__()
        self.usuarios =Data()
        self.usuarios.checkFile()

        self.originx = 0.02
        self.originy = 0.1
        self.deltax = 0.15
        self.deltay1 = 0.15
        self.deltay2 = 0.10
        self.diff = 0.03
        self.cancel = False
        self.delelim = False
        self. edit = False
 
        self.msgMain = gui.StringVar()
        self.msgMain.set(msgMain)

        self.textBtnStartCancel = gui.StringVar()
        self.textBtnStartCancel.set(textBtnStart)
        self.textBtnSend = gui.StringVar()
        self.textBtnModify = gui.StringVar()
        self.textBtnDelete = gui.StringVar()
        self.textBtnedit = gui.StringVar()

        self.nameMainLabel = gui.StringVar()
        self.nameText = gui.StringVar()
        self.lastnameMainLabel = gui.StringVar()
        self.lastnameText = gui.StringVar()
        self.datbirthMainLabel = gui.StringVar()
        self.datbirthText = gui.StringVar()
        self.countryMainLabel = gui.StringVar()
        self.countryText = gui.StringVar()
        self.emailMainLabel = gui.StringVar()
        self.emailText = gui.StringVar()
        self.telfMainLabel = gui.StringVar()
        self.telfText = gui.StringVar() 
        self.usersLabel= gui.StringVar()
        self.elimdelLabel = gui.StringVar()
        self.elimdelText = gui.StringVar()
      
        self.msgOut = gui.StringVar() 

        self.title('Registro de Usuarios')
        self.geometry('600x450')
        self.configure(background='black')
        self.resizable(False, False)

        self.mainFrame = gui.Frame(self, width=600, height=300, bg="black")
        self.mainFrame.grid(row=0,column=0, padx=0, pady=0)
        self.mainFrame.grid_propagate(0)
        self.nothingFrame = gui.Frame(self, width=600, height=5, bg="#66b297")
        self.nothingFrame.grid(row=1,column=0, padx=0, pady=0)
        self.nothingFrame.grid_propagate(0)
        self.buttonFrame = gui.Frame(self, width=600, height=110, bg="black")
        self.buttonFrame.grid(row=2,column=0, padx=0, pady=0)
        self.buttonFrame.grid_propagate(0)
        self.nothing2Frame = gui.Frame(self, width=600, height=1, bg="#66b297")
        self.nothing2Frame.grid(row=3,column=0, padx=0, pady=0)
        self.nothing2Frame.grid_propagate(0)
        self.msgFrame = gui.Frame(self, width=600, height=34, bg="black")
        self.msgFrame.grid(row=4,column=0, padx=0, pady=0)
    
    def firstWindow(self):
        self.mainLabel = gui.Label(self.mainFrame, textvar=self.msgMain)
        self.mainLabel.config(fg="white", bg="black", font=("Verdana",25)) 
        self.mainLabel.place(relx=0.5, rely=0.5, width=400, anchor='c')
        self.startCancelButton = gui.Button(self.buttonFrame, textvar=self.textBtnStartCancel, width=25, bg="#66b297", command=self.secondWindow)
        self.startCancelButton.place(relx=0.5, rely=0.5, width=100, anchor='c')
        
    def clearall(self):
        self.nameText.set("")
        self.lastnameText.set("")
        self.datbirthText.set("")
        self.countryEntry.set("")
        self.emailText.set("")
        self.telfText.set("")

    def secondWindow(self):
        if self.cancel == True:
            self.msgOut.set("Datos borrados. Ingrese los datos requeridos para su registro...")
            self.clearall()
            
        else:
            self.mainLabel.place_forget()
            self.nameMainLabel.set("Nombre")
            self.nameLabel = gui.Label(self.mainFrame, textvar=self.nameMainLabel)
            self.nameLabel.config(fg="white", bg="black", font=("Verdana",12)) 
            self.nameLabel.place(relx=self.originx, rely=self.originy, anchor="nw")

            self.nameEntry = gui.Entry(self, textvar=self.nameText)
            self.nameEntry.config(fg="black", bg="white", font=("Verdana",12)) 
            self.nameEntry.place(relx=self.originx + self.deltax, rely=self.originy - self.diff, width=200, anchor="nw")

            self.lastnameMainLabel.set("Apellido")
            self.lastnameLabel = gui.Label(self.mainFrame, textvar=self.lastnameMainLabel)
            self.lastnameLabel.config(fg="white", bg="black", font=("Verdana",12)) 
            self.lastnameLabel.place(relx=self.originx, rely=self.originy +1*self.deltay1, anchor="nw")
 
            self.lastnameEntry = gui.Entry(self, textvar=self.lastnameText)
            self.lastnameEntry.config(fg="black", bg="white", font=("Verdana",12)) 
            self.lastnameEntry.place(relx=self.originx + self.deltax, rely=self.originy +(1*self.deltay2)-self.diff, width=200, anchor="nw")

            self.datbirthMainLabel.set("F/Nac.")
            self.datbirthLabel = gui.Label(self.mainFrame, textvar=self.datbirthMainLabel)
            self.datbirthLabel.config(fg="white", bg="black", font=("Verdana", 12)) 
            self.datbirthLabel.place(relx=self.originx, rely=self.originy +2*self.deltay1, anchor="nw")
            
            self.datbirthEntry = gui.Entry(self, textvar=self.datbirthText)
            self.datbirthEntry.config(fg="black", bg="white", font=("Verdana",12)) 
            self.datbirthEntry.place(relx=self.originx + self.deltax, rely=self.originy +(2*self.deltay2)-self.diff, width=200, anchor="nw")

            self.countryMainLabel.set("País")
            self.countryLabel = gui.Label(self.mainFrame, textvar=self.countryMainLabel)
            self.countryLabel.config(fg="white", bg="black", font=("Verdana",12)) 
            self.countryLabel.place(relx=self.originx, rely=self.originy +3*self.deltay1, anchor="nw")

            self.styleCountry = gui2.Style()
            self.styleCountry.configure("BW.TLabel", foreground="black", background="White", selectforeground="black", selectbackground="white" )
            self.countryEntry = gui2.Combobox(self,  values=["Argentina", "Bolivia", "Brasil", "Colombia", "Chile", "Ecuador", "Guyana", "Mexico", "Peru", "Venezuela" ], style="BW.TLabel", font=("Verdana", 12))
            self.countryEntry.place(relx=self.originx + self.deltax, rely=self.originy +(3*self.deltay2)-self.diff, width=200, anchor="nw")
            
            self.emailMainLabel.set("E-mail")
            self.emailLabel = gui.Label(self.mainFrame, textvar=self.emailMainLabel)
            self.emailLabel.config(fg="white", bg="black", font=("Verdana",12)) 
            self.emailLabel.place(relx=self.originx, rely=self.originy +4*self.deltay1, anchor="nw")

            self.emailEntry = gui.Entry(self, textvar=self.emailText)
            self.emailEntry.config(fg="black", bg="white", font=("Verdana",12)) 
            self.emailEntry.place(relx=self.originx + self.deltax, rely=self.originy +(4*self.deltay2)-self.diff, width=200, anchor="nw")

            self.telfMainLabel.set("Teléfono")
            self.telfLabel = gui.Label(self.mainFrame, textvar=self.telfMainLabel)
            self.telfLabel.config(fg="white", bg="black", font=("Verdana",12)) 
            self.telfLabel.place(relx=self.originx, rely=self.originy +5*self.deltay1, anchor="nw")

            self.telfEntry = gui.Entry(self, textvar=self.telfText)
            self.telfEntry.config(fg="black", bg="white", font=("Verdana",12)) 
            self.telfEntry.place(relx=self.originx + self.deltax, rely=self.originy +(5*self.deltay2)-self.diff, width=200, anchor="nw")

            self.msgOut.set("Ingrese los datos requeridos para su registro...")
            self.msgOutLabel = gui.Label(self.msgFrame, textvar=self.msgOut)
            self.msgOutLabel.config(fg="white", bg="black", font=("Verdana",9)) 
            self.msgOutLabel.place(relx=0.02, rely=0.5, anchor="w")

            self.textBtnStartCancel.set("Cancelar")
            self.startCancelButton.place(relx=0.80, rely=0.5, width=100, anchor='c') 

            self.textBtnSend.set("Enviar")
            self.sendButton = gui.Button(self.buttonFrame, textvar=self.textBtnSend, width=25, bg="#66b297", command=self.register)
            self.sendButton.place(relx=0.20, rely=0.5, width=100, anchor='c')
            self.cancel = True

            self.textBtnDelete.set("Eliminar")
            self.modifyButton = gui.Button(self.buttonFrame, textvar=self.textBtnDelete, width=25, bg="#66b297", command=self.deleter)
            self.modifyButton.place(relx=0.40, rely=0.5, width=100, anchor='c')
            self.checkElimdel()

            self.textBtnModify.set("Editar")
            self.modifyButton = gui.Button(self.buttonFrame, textvar=self.textBtnModify, width=25, bg="#66b297", command=self.editer)
            self.modifyButton.place(relx=0.60, rely=0.5, width=100, anchor='c')

    def validate(self):
        self.validated = False
        matchName = re.search("([^a-zA-Z]+)", self.nameText.get())
        if  matchName or self.nameText.get()=="":
            print('validado1')
            self.msgOut.set(f'El {self.nameMainLabel.get()} acepta solo caracteres alfabéticos.')
        else: 
            matchLastname = re.search("([^a-zA-Z]+)", self.lastnameText.get())
            if matchLastname or self.lastnameText.get()=="":
                self.msgOut.set(f'El {self.lastnameMainLabel.get()} acepta solo caracteres alfabéticos.')
            else:
                matchDatbirth = re.search("([0-2]\d|3[01])[-/]([0]\d|1[12])[-/](19[0-9]{2}|20[0-9]{2})", self.datbirthText.get())
                if not matchDatbirth or self.datbirthText.get()=="":
                    self.msgOut.set(f'El {self.datbirthMainLabel.get()} es incorrecto.formato DD/MM/AAAA o DD-MM-AAAA.')
                else:
                    self.countryText.set(self.countryEntry.get())
                    if  self.countryText.get() =="":
                       self.msgOut.set(f'Selección de {self.countryMainLabel.get()} no valida.')
                    else:
                        matchEmail = re.search("(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$", self.emailText.get())
                        if not matchEmail or self.emailText.get()=="":
                            self.msgOut.set(f'El {self.emailMainLabel.get()} es incorrecto.')
                        else:
                            matchTelf = re.search("[+](1|\d{2}|\d{3})\d{10}", self.telfText.get()) #"[+](1|\d{2}|\d{3})[24](\d{2}|12|([12][46]))\d{3}\d{4}"
                            if not matchTelf or self.telfText.get()=="":
                                self.msgOut.set(f'El {self.telfMainLabel.get()} es incorrecto.')
                            else:
                                print
                                self.validated =True                   
        return self.validated

    def register(self):
        self.usuario = User()
        if self.edit == False:
            if self.validate():
                self.usuario.setname(self.nameText.get().title())
                self.usuario.setlastname(self.lastnameText.get().title())     
                self.usuario.setbirthdate(self.datbirthText.get())
                self.usuario.setcountry(self.countryText.get())
                self.usuario.setemail(self.emailText.get()) 
                self.usuario.setteleph(self.telfText.get())
                self.usuario.notifyEmail()
                self.usuario.notifyWS()
                self.msgOut.set("Usuario Registrado!")
                self.clearall()
                self.usuarios.add(self.usuario)
                self.usuarios.writeFile(self.usuarios.getLength())
                self.checkElimdel()
                print('no paso')
        else:
            print('Que paso ahora')
            if self.validate():
                self.usuario.setname(self.nameText.get().title())
                self.usuario.setlastname(self.lastnameText.get().title())     
                self.usuario.setbirthdate(self.datbirthText.get())
                self.usuario.setcountry(self.countryText.get())
                self.usuario.setemail(self.emailText.get()) 
                self.usuario.setteleph(self.telfText.get())
                self.msgOut.set("Usuario Actualizado!")
                print(str(self.usuario))
                self.usuarios.set(self.usuario,int( self.elimdelText.get())-1)
                self.usuarios.writeFileFull()
                self.clearall()
                self.edit = False
                    
    def deleter(self):
        if  self.usuarios.getLength() == 0:
            self.msgOut.set("No Hay datos en la base de datos.")
        else:
            matchElem = re.search("\d", self.elimdelText.get())
            if not matchElem or self.elimdelText.get()=="":
                self.msgOut.set(f'El valor introducido no es un caracter numérico.')
            else:
                if int(self.elimdelText.get()) <= 0 or int(self.elimdelText.get()) > self.usuarios.getLength():
                    self.msgOut.set('El valor introducido no es válido.')
                else:
                    self.usuarios.delete(int(self.elimdelText.get())-1)
                    self.checkElimdel()
                    self.usuarios.writeFileFull()

    def editer(self):
        if  self.usuarios.getLength() == 0:
            self.msgOut.set("No Hay datos en la base de datos.")
        else:
            matchElem = re.search("\d", self.elimdelText.get())
            if not matchElem or self.elimdelText.get()=="":
                self.msgOut.set(f'El valor introducido no es un caracter numérico.')
            else:
                if int(self.elimdelText.get()) <= 0 or int(self.elimdelText.get()) > self.usuarios.getLength():
                    self.msgOut.set('El valor introducido no es válido.')
                else:
                    self.nameText.set(self.usuarios.get()[int(self.elimdelText.get())-1].getname())
                    self.lastnameText.set(self.usuarios.get()[int(self.elimdelText.get())-1].getlastname())
                    self.datbirthText.set(self.usuarios.get()[int(self.elimdelText.get())-1].getbd())
                    self.countryText.set(self.usuarios.get()[int(self.elimdelText.get())-1].getcountry())
                    self.emailText.set(self.usuarios.get()[int(self.elimdelText.get())-1].getemail().get())
                    self.telfText.set(self.usuarios.get()[int(self.elimdelText.get())-1].gettel().get())
                    self.edit= True
                    
    def checkElimdel(self):  
        if self.delelim == False:  
            if self.usuarios.getLength() != 0:    
                self.names ='Elementos Registrados: \n'    
                for index, user  in enumerate(self.usuarios.get()):
                    #print(str(user))
                    value = str(index + 1) +'. ' + user.getname() + ' ' + user.getlastname() +'\n' 
                    #print(value)
                    self.names += value

                #print(self.names)
                self.usersLabel.set(self.names)
                self.usersShowLabel = gui.Label(self.mainFrame, textvar=self.usersLabel)
                self.usersShowLabel.config(fg="white", bg="black", font=("Verdana",12)) 
                self.usersShowLabel.place(relx=self.originx + 0.5, rely=self.originy +0*self.deltay1, anchor="nw")

                self.elimdelLabel.set("Item a editar/modificar?")
                self.elimdelLabel = gui.Label(self.mainFrame, textvar=self.elimdelLabel)
                self.elimdelLabel.config(fg="white", bg="black", font=("Verdana",12)) 
                self.elimdelLabel.place(relx=self.originx + 0.5, rely=self.originy +4*self.deltay1, anchor="nw")

                self.elimdelEntry = gui.Entry(self, textvar=self.elimdelText)
                self.elimdelEntry.config(fg="black", bg="white", font=("Verdana",12)) 
                self.elimdelEntry.place(relx=self.originx + 0.5, rely=self.originy +(5*self.deltay2)-self.diff, width=100, anchor="nw")
                self.delelim = True
        else:
            if self.usuarios.getLength() != 0:    
                self.names ='Elementos Registrados: \n'    
                for index, user  in enumerate(self.usuarios.get()):
                    #print(str(user))
                    value = str(index + 1) +'. ' + user.getname() + ' ' + user.getlastname() +'\n' 
                    #print(value)
                    self.names += value
                #print(self.names)
                self.usersLabel.set(self.names)
                self.usersShowLabel.place(relx=self.originx + 0.5, rely=self.originy +0*self.deltay1, anchor="nw")
                self.elimdelLabel.place(relx=self.originx + 0.5, rely=self.originy +4*self.deltay1, anchor="nw")
                self.elimdelEntry.place(relx=self.originx + 0.5, rely=self.originy +(5*self.deltay2)-self.diff, width=100, anchor="nw")
            else:
                self.usersShowLabel.place_forget()
                self.elimdelLabel.place_forget()
                self.elimdelEntry.place_forget()

if __name__ == "__main__":
    myInterface = Gui("¡Bienvenidos!","Iniciar")
    myInterface.firstWindow()
    myInterface.mainloop()
