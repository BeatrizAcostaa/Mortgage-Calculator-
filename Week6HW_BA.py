'''
Programmer: Beatriz Acosta 
Date: 06/30/2023
Version: 1.3
Description: Program accepts user input of mortgage amount, term, interest rate and returns monthly payment amount. 
Program GUI is contained in the class named MYGUI and is called through a object.  
'''

import tkinter 
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_w = tkinter.Tk() #main window widget 

        #FRAME
        self.top_f = tkinter.Frame(self.main_w)        #Title frame 
        self.second_f = tkinter.Frame(self.main_w)     #Mortgage Amount Frame 
        self.third_f = tkinter.Frame(self.main_w)      #Term Amount Frame 
        self.fourth_f = tkinter.Frame(self.main_w)     #Interest Rate Amount Frame 
        self.fifth_f = tkinter.Frame(self.main_w)      #Buttons Frame 

        
        #labels
        self.label = tkinter.Label(self.top_f,text = 'Mortgage Calculator')  #object self uses method Label from tkinter module and it belongs to frame top_f 
        self.label2 = tkinter.Label(self.second_f,text = 'Mortgage Amount: ') #object self uses method Label from tkinter module and it belongs to frame bottom_f
        self.label3 = tkinter.Label(self.third_f,text = 'Term of Mortgage(years): ')
        self.label4 = tkinter.Label(self.fourth_f,text = 'Interest rate of Mortgage:')

        #entries 
        self.amount2 = tkinter.Entry(self.second_f,width = 15, foreground='blue')
        self.amount3 = tkinter.Entry(self.third_f,width = 15, foreground = 'blue')
        self.amount4 = tkinter.Entry(self.fourth_f,width = 15, foreground = 'blue')

        #buttons #NEW CHANGE!
        self.result = tkinter.Button(self.fifth_f, text = '| Calculate Monthly Payment |', command = self.Calculate)
        self.quit = tkinter.Button(self.fifth_f,text = 'QUIT', command = self.main_w.destroy)


        #packing for label 1 Title
        self.label.pack(side = 'top')  

        #packing for label 2/ entry 2
        self.label2.pack(side = 'left')
        self.amount2.pack(side = 'left')

        #packing for label 3/ entry 3 
        self.label3.pack(side='left')
        self.amount3.pack(side='left')
        
        #packing for label 4/ entry 4 
        self.label4.pack(side = 'left')
        self.amount4.pack(side = 'left')

        #packing for buttons 
        self.result.pack(side='left')  #result button
        self.quit.pack(side = 'left')  #quit button 

        #Packing for frames 
        self.top_f.pack()      #Title Frame 
        self.second_f.pack()   #Mortgage Amount Frame 
        self.third_f.pack()    #Term Amount Frame 
        self.fourth_f.pack()   #Interest Rate Frame 
        self.fifth_f.pack()    #Buttons Frame 

        tkinter.mainloop() #loop remains at end to keep window open 

    def Calculate(self):
        mortgage_amount = float(self.amount2.get())           #Get Mortgage amount from entry widget 
        term_amount = float(self.amount3.get()) * 12          #Get Term amount from entry widget 
        interest_rate = float(self.amount4.get()) / 1200.00   #Get Interest rate amount from entry widget 
        numerator = (mortgage_amount * interest_rate)                 #calc 
        denominator = 1-(interest_rate + 1)**(-term_amount)           #calc
        result = 'Your monthly payment is ' + str(format(numerator/denominator,'.2f'))   #concatenate string values 
    
        
        tkinter.messagebox.showinfo(' Monthly Payment ', result)    #pass result value to display in message box 


my_gui = MyGUI()  #create object 
#Test Comment 