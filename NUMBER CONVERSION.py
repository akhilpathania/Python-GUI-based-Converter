from Tkinter import *
import Tkinter
import tkMessageBox
"""---------------------BINARY TO OTHERS--------------------------------"""

def Binary_To_Others():
    top=Tkinter.Tk()
    top.attributes('-fullscreen',True)
    top.title("BINARY TO OTHERS")
    top.configure(background='pink')
    L0 = Label(top, text="NUMBER CONVERSION CALCULATOR",
           fg="orange",
           bg="purple",
           relief=RAISED,
           font="Times").grid(row=0,column=1)

    LB = Label(top,text="Binary To Others",
               fg="red",
               bg="green",
               relief=RAISED,
               font="Times").grid(row=1,column=1)

    E2 = Entry(top,bd=5,relief=GROOVE)
    E2.grid(row=2,column=1)
    E22=Entry(top,bd=5)
    E22.grid(row=2,column=3)

    def abc():
        if((str(E2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            binary_to_decimal()
    def binary_to_decimal():
        E22.delete(0, END)
        binary=str(E2.get())
        btd = int(binary, 2)
        E22.insert(0,btd)
    
    B2=Tkinter.Button(top,relief=RAISED,text="Convert Binary to Decimal",fg='red',bg='yellow',command=abc)
    B2.grid(row=2,column=2)

  
    E33=Entry(top,bd=5)
    E33.grid(row=3,column=3)

    def abc1():
        if((str(E2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            binary_to_octal()
        
    def binary_to_octal():
        E33.delete(0, END)
        binary=str(E2.get())
        bto= int(binary, 2)
        bto=oct(bto)
        str(bto)
        bto=bto[1:]
        E33.insert(0,bto)

    B3=Tkinter.Button(top,relief=RAISED,text="Convert Binary To Octal",fg='red',bg='yellow',command=abc1)
    B3.grid(row=3,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------BINARY TO HEXADECIMAL-------------------"""
    
    E44=Entry(top,bd=5)
    E44.grid(row=5,column=3)

    def abc2():
        if((str(E2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            binary_to_hexadecimal()

    def binary_to_hexadecimal():
        E44.delete(0, END)
        binary=str(E2.get())
        bth = int(binary, 2)
        bth=hex(bth)
        str(bth)
        bth=bth[2:]
        bth=bth.upper()
        E44.insert(0,bth)

    B4=Tkinter.Button(top,relief=RAISED,text="Convert Binary To Hexadecimal",fg='red',bg='yellow',command=abc2)
    B4.grid(row=5,column=2)

    """--------------------------------BINARY TO HEXADECIMAL COMPLETE---------------------------------------"""
    def convall():
        abc();
        abc1();
        abc2();
    CA=Button(top,text="CONVERT ALL",fg='blue',bg='black',command=convall)
    CA.grid(row=6,column=2)
    def reset_entries1():
         E2.delete(0, END)
         E22.delete(0, END)
         E33.delete(0, END)
         E44.delete(0, END)
        
    RESET1=Button(top,text="RESET",fg='blue',bg='black',command=reset_entries1)
    RESET1.grid(row=7,column=2)
    def close_window1(): 
        top.destroy()
    EXIT1=Button (top,text = "EXIT",fg='blue',bg='black',command=close_window1)
    EXIT1.grid(row=7,column=3)
    top.mainloop()

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """-----------------------------------------------BINARY TO OTHERS COMPLETE-------------------------------------------"""

"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""------------------------------------------DECIMAL TO OTHERS STARTS----------------------------------------------------"""

def decimal_To_Others():
    top1=Tkinter.Tk()
    top1.attributes('-fullscreen',True)
    top1.title("DECIMAL TO OTHERS")
    top1.configure(background='red')
    L0 = Label(top1, text="NUMBER CONVERSION CALCULATOR",
           fg="yellow",
           bg="green",
           relief=RAISED,
           font="Times").grid(row=0,column=1)
    """--------------------DECIMAL TO OTHERS-------------------"""
    LD = Label(top1,text="Decimal To Others",
               fg="blue",
               bg="black",
               relief=RAISED,
               font="Times").grid(row=6,column=1)
    """--------------------DECIMAL TO BINARY-------------------"""
    E5 = Entry(top1,bd=5)
    E5.grid(row=7,column=1)
    E55=Entry(top1,bd=5)
    E55.grid(row=7,column=3)

    def abc3():
        if((str(E5.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            decimal_to_binary()

    def decimal_to_binary():
        E55.delete(0, END)
        decimal=str(E5.get())
        dtb = int(decimal)
        dtb=bin(dtb)
        str(dtb)
        dtb=dtb[2:]
        E55.insert(0,dtb)
    B5=Tkinter.Button(top1,relief=RAISED,text="Convert Decimal To Binary",fg='white',bg='purple',command=abc3)
    B5.grid(row=7,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------DECIMAL TO OCTAL-------------------"""

    E66=Entry(top1,bd=5)
    E66.grid(row=8,column=3)

    def abc4():
        if((str(E5.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            decimal_to_octal()

    def decimal_to_octal():
        E66.delete(0, END)
        decimal=str(E5.get())
        dto=int(decimal)
        dto=oct(dto)
        str(dto)
        dto=dto[1:]
        E66.insert(0,dto)


    B6=Tkinter.Button(top1,relief=RAISED,text="Convert Decimal To Octal",fg='white',bg='purple',command=abc4)
    B6.grid(row=8,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------DECIMAL TO HEXADECIMAL-------------------"""

    E77=Entry(top1,bd=5)
    E77.grid(row=9,column=3)

    def abc5():
        if((str(E5.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            decimal_to_hexadecimal()

    def decimal_to_hexadecimal():
        E77.delete(0, END)
        decimal=str(E5.get())
        dth = int(decimal)
        dth=hex(dth)
        str(dth)
        dth=dth[2:]
        dth=dth.upper()
        E77.insert(0,dth)

    B7=Tkinter.Button(top1,relief=RAISED,text="Convert Decimal To Hexadecimal",fg='white',bg='purple',command=abc5)
    B7.grid(row=9,column=2)

    """------------------------------------------------DECIMAL TO HEXADECIMAL END---------------------------------------------------"""
    def convall1():
        abc3();
        abc4();
        abc5();
    CA1=Button(top1,text="CONVERT ALL",fg="black",bg="yellow",command=convall1)
    CA1.grid(row=10,column=2)
    def reset_entries2():
         E5.delete(0, END)
         E55.delete(0, END)
         E66.delete(0, END)
         E77.delete(0, END)
    
    RESET2=Button(top1,text="RESET",fg="black",bg="yellow",command=reset_entries2)
    RESET2.grid(row=20,column=2)
    def close_window2(): 
        top1.destroy()
    EXIT2=Button (top1,text = "EXIT",fg="black",bg="yellow",command=close_window2)
    EXIT2.grid(row=20,column=3)
    top1.mainloop()

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------DECIMAL TO OTHERS COMPLETE---------------"""
    """-------------------------------------------------------------------------------------------------------------------------------------------------"""

"""-------------------------------------OCTAL TO OTHERS START----------------------------------------"""

def octal_To_Others():
    top2=Tkinter.Tk()
    top2.attributes('-fullscreen',True)
    top2.title("DECIMAL TO OTHERS")
    top2.configure(background='yellow')
    L0 = Label(top2, text="NUMBER CONVERSION CALCULATOR",
           fg="orange",
           bg="black",
           font="Times").grid(row=0,column=1)
    """--------------------OCTAL TO OTHERS-------------------"""
    LO = Label(top2,text="Octal To Others ",
               fg="blue",
               bg="green",
               relief=RAISED,
               font="Times").grid(row=10,column=1)
    """--------------------OCTAL TO BINARY-------------------"""

    E8 = Entry(top2,bd=5)
    E8.grid(row=11,column=1)
    E88=Entry(top2,bd=5)
    E88.grid(row=11,column=3)

    def abc6():
        if((str(E8.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            octal_to_binary()

    def octal_to_binary():
        E88.delete(0, END)
        octal=str(E8.get())
        otb = str(int(octal,8))
        otb=int(otb)
        otb=bin(otb)
        otb=otb[2:]
        E88.insert(0,otb)
    B8=Tkinter.Button(top2,relief=RAISED,text="Convert Octal To Binary",fg='blue',bg='black',command=abc6)
    B8.grid(row=11,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------OCTAL TO DECIMAL-------------------"""

    E99=Entry(top2,bd=5)
    E99.grid(row=12,column=3)

    def abc7():
        if((str(E8.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            octal_to_decimal()

    def octal_to_decimal():
        E99.delete(0, END)
        octal=str(E8.get())
        otd= str(int(octal,8))
        E99.insert(0,otd)

    B9=Tkinter.Button(top2,relief=RAISED,text="Convert Octal To Decimal",fg='blue',bg='black',command=abc7)
    B9.grid(row=12,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------OCTAL TO HEXADECIMAL-------------------"""

    E101=Entry(top2,bd=5)
    E101.grid(row=13,column=3)

    def abc8():
        if((str(E8.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            octal_to_hexadecimal()

    def octal_to_hexadecimal():
        E101.delete(0, END)        
        octal=str(E8.get())
        oth = str(int(octal,8))
        oth=int(oth)
        oth=hex(oth)
        oth=oth[2:]
        oth=oth.upper()
        E101.insert(0,oth)

    B10=Tkinter.Button(top2,relief=RAISED,text="Convert Octal To Hexadecimal",fg='blue',bg='black',command=abc8)
    B10.grid(row=13,column=2)
    """-------------------------------------------OCTAL TO HEXADECIMAL COMPLETE----------------------------------"""
    def convall2():
        abc6();
        abc7();
        abc8();
    CA2=Button(top2,text="CONVERT ALL",bg="red",fg="black",command=convall2)
    CA2.grid(row=14,column=2)
    def reset_entries3():
         E8.delete(0, END)
         E88.delete(0, END)
         E99.delete(0, END)
         E101.delete(0, END)
    
    RESET3=Button(top2,text="RESET",bg="red",fg="black",command=reset_entries3)
    RESET3.grid(row=20,column=2)
    def close_window3(): 
        top2.destroy()
    EXIT3=Button (top2,text = "EXIT",bg="red",fg="black",command=close_window3)
    EXIT3.grid(row=20,column=3)
    top2.mainloop()

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------OCTAL TO OTHERS COMPLETE---------------"""




    """-------------------------------------------------------------------------------------------------------------------------------------------------"""

"""---------------------------------HEXADECIMAL TO OTHERS-------------------------------------------"""

def hexadecimal_To_Others():
    top3=Tkinter.Tk()
    top3.attributes('-fullscreen',True)
    top3.title("DECIMAL TO OTHERS")
    top3.configure(background='black')
    L0 = Label(top3, text="NUMBER CONVERSION CALCULATOR",
           fg="white",
           bg="red",
           relief=RAISED,
           font="Times").grid(row=0,column=1)
    """--------------------HEXADECIMAL TO OTHERS-------------------"""
    LH = Label(top3,text="Hexadecimal To Others ",
               fg="black",
               bg="blue",
               relief=RAISED,
               font="Times").grid(row=14,column=1)
    """--------------------HEXADECIMAL TO BINARY-------------------"""

    E11= Entry(top3,bd=5)
    E11.grid(row=15,column=1)
    E111=Entry(top3,bd=5)
    E111.grid(row=15,column=3)

    def abc9():
        if((str(E11.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            hexadecimal_to_binary()

    def hexadecimal_to_binary():
        E111.delete(0, END)
        hexadecimal=str(E11.get())
        htb = int(hexadecimal,16);
        htb=bin(htb)
        htb=htb[2:]
        E111.insert(0,htb)
        
    B11=Tkinter.Button(top3,relief=RAISED,text="Convert Hexadecimal to Binary",fg='red',bg='green',command=abc9)
    B11.grid(row=15,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------HEXADECIMAL TO DECIMAL-------------------"""

    E121=Entry(top3,bd=5)
    E121.grid(row=16,column=3)

    def abc10():
        if((str(E11.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            hexadecimal_to_decimal()

    def hexadecimal_to_decimal():
        E121.delete(0, END)
        hexadecimal=str(E11.get())
        htd=int(hexadecimal,16)
        E121.insert(0,htd)
        
    B12=Tkinter.Button(top3,relief=RAISED,text="Convert Hexadecimal To Decimal",fg='red',bg='green',command=abc10)
    B12.grid(row=16,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""

    """--------------------HEXADECIMAL TO OCTAL-------------------"""

    E131=Entry(top3,bd=5)
    E131.grid(row=17,column=3)

    def abc11():
        if((str(E11.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            hexadecimal_to_octal()

    def hexadecimal_to_octal():
        E131.delete(0, END)
        hexadecimal=str(E11.get())
        hto =int(hexadecimal,16)
        hto=oct(hto)
        hto=hto[1:]
        E131.insert(0,hto)
    B13=Tkinter.Button(top3,relief=RAISED,text="Convert Hexadecimal To Octal",fg='red',bg='green',command=abc11)
    B13.grid(row=17,column=2)

    """-------------------XXXXXXXXXXXXXXXX-------------------"""
    def convall3():
        abc9();
        abc10();
        abc11();
    CA3=Button(top3,text="CONVERT ALL",fg="black",bg="red",command=convall3)
    CA3.grid(row=18,column=2)
    def reset_entries4():
         E11.delete(0, END)
         E111.delete(0, END)
         E121.delete(0, END)
         E131.delete(0, END)
    
    RESET4=Button(top3,text="RESET",fg="black",bg="red",command=reset_entries4)
    RESET4.grid(row=20,column=2)
    def close_window4(): 
        top3.destroy()
    EXIT4=Button (top3,text = "EXIT",fg="black",bg="red",command=close_window4)
    EXIT4.grid(row=20,column=3)
    top3.mainloop()
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    
           

"""-------------------XXXXXXXXXXXXXXXX-------------------"""



"""---------------------STARTING OF THE CODES-----------------------------"""

top4=Tkinter.Tk()
top4.attributes('-fullscreen',True)
top4.title("NUMBER CONVERTER")
top4.configure(background='yellow')
I0 = Label(top4, text="NUMBER CONVERSION CALCULATOR",
           fg="blue",
           bg="black",
           relief=RAISED,
           font="Times").grid(row=0,column=2)

BTO=Tkinter.Button(top4,relief=RAISED,text="Convert Binary To Others",fg='black',bg='green',command=Binary_To_Others)
BTO.grid(row=1,column=2)
DTO=Tkinter.Button(top4,relief=RAISED,text="Convert Decimal 5To Others",fg='black',bg='green',command=decimal_To_Others)
DTO.grid(row=2,column=2)
OTO=Tkinter.Button(top4,relief=RAISED,text="Convert Octal To Others",fg='black',bg='green',command=octal_To_Others)
OTO.grid(row=3,column=2)
HTO=Tkinter.Button(top4,relief=RAISED,text="Convert Hexadecimal To Others",fg='black',bg='green',command=hexadecimal_To_Others)
HTO.grid(row=4,column=2)
D=Label(top4,text="Developed By:-",bg='green')
D.grid(row=5,column=0)
D1=Label(top4,text="Akhil Pathania",bg='green')
D1.grid(row=6,column=0)
D2=Label(top4,text="Shubham Pandey",bg='green')
D2.grid(row=7,column=0)
D3=Label(top4,text="Seval Patel",bg='green')
D3.grid(row=8,column=0)
def close_window():
    top4.destroy()
B15=Button (top4,text =":    EXIT    :",fg='blue',bg='black',command=close_window)
B15.grid(row=8,column=3)
top4.mainloop()
"""------------------------END OF 1st WINDOW-----------------------------------"""
