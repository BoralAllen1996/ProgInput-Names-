from tkinter import*
import math
import tkinter.messagebox

root = Tk()
root.title("scientific calculator")
root.resizable(width=False, height =False)
root.geometry("400x492+460+40")

MainFrame = Frame(root, pady=2, relief=RIDGE)
MainFrame.grid()
calFrame = Frame(MainFrame, bd=20, pady=2, relief=RIDGE )
calFrame.grid()
#========================================================================================================================

class Calc():
    def __init__(self):
        self.total = 0
        self.current =""
        self.input_value = True
        self.check_sum = False
        self.op=""
        self.result = False
        
added_value = Calc

txtResult = Entry(calFrame, font =('arial',16,'bold'),bg="cadetblue", bd=30, width=26, justify =RIGHT)
txtResult .grid(row=0,column=0, columnspan = 4, pady=1)
txtResult.insert(0, "0")
#=======================================================================================================================
numericButton = "789456123"
i =0
btn=[]
for j in range(2,5):
    for q in range(3):
        btn.append(Button(calFrame, width=6, height=2,font =('arial',16,'bold'),bd=4, 
        text=numericButton[i])) 
        btn[i].grid(row =j, column=q, pady=1)
        btn[i]["command"] = lambda x = numericButton[i]:added_value
        i+=1
# =======================================================================================================================

btn0=Button(calFrame, text="0", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=0, pady=1)

btnDiv=Button(calFrame, text=chr(247), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=3, pady=1)

btnMult=Button(calFrame, text=chr(42), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =4, column=3, pady=1)

btnSub=Button(calFrame, text=chr(45), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =3, column=3, pady=1)

btnDot=Button(calFrame, text=chr(183), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=1, pady=1)

btnAdd=Button(calFrame, text=chr(43), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =2, column=3, pady=1)

btnPM=Button(calFrame, text=chr(177), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=3, pady=1)

btnBackSpace=Button(calFrame, width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=0, pady=1)

btnClearEntry=Button(calFrame, text=chr(67) + chr(69), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=1, pady=1)

btnClear =Button(calFrame, text=chr(67), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=2, pady=1)

btnEquals =Button(calFrame, text=chr(61), width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=2, pady=1)
#=======================================================================================================================

btnsin = Button(calFrame, text="sin", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=4, padx=5, pady=1)

btntan = Button(calFrame, text="tan", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=5, padx=5, pady=1)

btncos = Button(calFrame, text="cos", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=6, padx=5, pady=1)

btnPi = Button(calFrame, text="π", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =1, column=7, padx=5, pady=1)

# =====================================================================================================================

btnsinh = Button(calFrame, text="sinh", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =2, column=4, padx=5, pady=1)

btntanh = Button(calFrame, text="tanh", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =2, column=5, padx=5, pady=1)

btncosh = Button(calFrame, text="cosh", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =2, column=6, padx=5, pady=1)

btn2pi = Button(calFrame, text="2π", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =2, column=7, padx=5, pady=1)

#==================================================================================================================
btnE =Button(calFrame, text="e", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =3, column=4, pady=1)

btnMod =Button(calFrame, text="mod", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =3, column=5, pady=1)

btnExp=Button(calFrame, text="exp", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =3, column=6, pady=1)

btnlog =Button(calFrame, text="log", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =3, column=7, pady=1)

#=======================================================================================================================

btnasinh =Button(calFrame, text="asinh", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =4, column=4, pady=1)

btnacosh =Button(calFrame, text="acosh", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =4, column=5, pady=1)

btndeg =Button(calFrame, text="deg", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =4, column=6, pady=1)

btnlog2 =Button(calFrame, text="log2", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =4, column=7, pady=1)
#======================================================================================================================

btn1gamma =Button(calFrame, text="lgmma", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=4, pady=1)

btnexpm1 =Button(calFrame, text="expm1", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=5, pady=1)

btnlog1p=Button(calFrame, text="logp1", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=6, pady=1)

btnlog10=Button(calFrame, text="log10", width=6, height=2,font =('arial',16,'bold'),bd=4, 
bg="cadetblue").grid(row =5, column=7, pady=1)






def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def scientific():
    root.geometry("796x492+460+40")
    root.resizable(width=False, height =False)
    txtResult.delete(0, END)
    txtResult.delete(0, "0")
    
def standard():
    root.geometry("796x492+460+40")
    root.resizable(width=False, height =False)
    txtResult.delete(0, END)
    txtResult.delete(0, "0")

menubar = Menu(calFrame)

filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label ="File", menu=filemenu)
filemenu.add_command(label ="standard", command =standard)
filemenu.add_separator()
filemenu.add_command(label ="Scientific",  command =scientific)
filemenu.add_separator()
filemenu.add_command(label ="Exit", command =iExit)

root.config(menu = menubar)



root.mainloop()