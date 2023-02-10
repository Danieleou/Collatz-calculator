from tkinter import ttk
from tkinter import *
from functions import *

class Application:
    def __init__(self):
        self.root=Tk()
        self.root.title('Calculator Collatz')
        # Creating frame
        self.frame=LabelFrame(self.root,text='Enter a number integer positive')
        self.frame.grid(row=0,column=0,columnspan=2,pady=20)
        # Number input
        Label(self.frame,text='Number:').grid(row=1,column=0)
        self.number=Entry(self.frame)
        self.number.focus()
        self.number.grid(row=1,column=1,columnspan=2,sticky=W+E)
        # Bottom request
        ttk.Button(self.frame,text='Request',command=lambda:self.request(self.number.get())).grid(row=2,column=0,columnspan=3,sticky=W+E)
        # caution message
        self.cautionMessage=Label(self.frame,text='',fg='red')
        self.cautionMessage.grid(row=3,column=0,columnspan=2,sticky=W+E)
        # Output messages
        Label(self.frame,text='Path:').grid(row=4,column=0)
        self.messagePath=Label(self.frame,text='',relief=SUNKEN,wraplength=700)
        self.messagePath.grid(row=4,column=1,sticky=W)
        Label(self.frame,text='Lenght:').grid(row=5,column=0,sticky=W+E)
        self.messageLenght=Label(self.frame,text='')
        self.messageLenght.grid(row=5,column=1,sticky=W)
        Label(self.frame,text='Maximum:').grid(row=6,column=0)
        self.messageMaximum=Label(self.frame,text='')
        self.messageMaximum.grid(row=6,column=1,sticky=W)

        self.root.mainloop()

    def request(self,value):
        self.cautionMessage['text']=''
        self.messagePath['text']=''
        self.messageLenght['text']=''
        self.messageMaximum['text']=''
        if self.validation():
            self.messagePath['text']=path_collatz(int(self.number.get()))
            self.messageLenght['text']=length_path_collazt(int(self.number.get()))
            self.messageMaximum['text']=max_collatz(int(self.number.get()))

    def validation(self):
        try:
            value=int(self.number.get())
            if value>0:
                return True
            else:
                self.cautionMessage['text']='Input a number integer positive'
                return False
        except ValueError as v:
            self.cautionMessage['text']='Input a number integer positive'
            return

def main():
    my_app=Application()
    return 0

if __name__=='__main__':
    main()