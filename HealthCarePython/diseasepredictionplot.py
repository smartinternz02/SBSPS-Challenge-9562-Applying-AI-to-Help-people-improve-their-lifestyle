# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from PIL import Image



def plot():
    
     
    
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), 
                 dpi = 100)
  
    # list of squares
    y = [i**2 for i in range(100)]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plt.show()
  
    # plotting the graph
    plot1.plot(y)
    
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = TOP)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   TOP)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    
def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height


def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight


def get_age():
    age = float(ENTRY3.get())
    return age

def get_hb():
    hb = float(ENTRY4.get())
    return hb

def get_ecg():
    ecg = float(ENTRY5.get())
    return ecg

def get_bb():
    bb = float(ENTRY6.get())
    return bb



def calculate_age(a=""):   # "a" is there because the bind function gives an argument to the function....
    print(a)
    '''
      This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        age = get_age()
        age = get_age()
        age1 = weight / (height**2)
        hb = get_hb()
        ecg = get_ecg()
        bb = get_bb()
        
        
        print(age1)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if  75 < hb <= 153 and 60 < ecg <= 100 and 80 < bb <= 130:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Normal No Disease", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)
            
        elif  154 < hb <= 500 and 60 < ecg <= 100 and 80 < bb <= 130:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Heat beat is increase by chance you will heart attack", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)

        elif  0 < hb <= 70 and 60 < ecg <= 100 and 80 < bb <= 130:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Heat beat is increase by chance you will heart attack", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)

        elif  75 < hb <= 153 and 101 < ecg <= 200 and 80 < bb <= 130:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Abnormal Ecg Reading(High)", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)
            
        elif  75 < hb <= 153 and 0 < ecg <= 59 and 80 < bb <= 130:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Abnormal Ecg Reading(Low)", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)
            
        elif  75 < hb <= 153 and 60 < ecg <= 100 and 130 < bb <= 300:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Blood Pressure Level is Higher than Normal & Need Immediate Medical Assetment", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)
        elif  75 < hb <= 153 and 60 < ecg <= 100 and 0 < bb <= 79:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="Blood Pressure Level is Lower than Normal & Need Immediate Medical Assetment", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)
                 
        else:
            LABLE4 = Label(TOP, bg="#cef0f1", text="Report", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=180, y=490)
            LABLE4 = Label(TOP, bg="#cef0f1", text="No Disease", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=540)
            LABLE4 = Label(TOP, bg="#cef0f1", text="BMI Value is "+str(age1)+"", bd=6,font=("Helvetica", 15, "bold"), pady=5)
            LABLE4.place(x=150, y=580)
        


if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_age)
    TOP.geometry("700x700")
    TOP.configure(background="#332C5F")
    TOP.title("Applying AI to Healthcare")
    TOP.resizable(width=False, height=False)
    #image=PhotoImage(file="D:\\HealthCarePython\\bank.png")
    #l=Label(TOP,image=image)
    #l.pack(fill=BOTH)

    LABLE = Label(TOP, bg="#FB07FF", text="Applying AI to Healthcare", font=("Helvetica", 15, "bold"), pady=10 ,foreground="white")
    LABLE.place(x=95, y=10)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=1, width=16, font="Roboto 11")
    ENTRY1.place(x=240, y=70)
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in feet):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    LABLE3 = Label(TOP, bg="#cef0f1", text="Enter Age:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE3.place(x=55, y=171)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Heart Beat:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=232)
    
        
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter ECG Reading:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=293)
    
    LABLE3 = Label(TOP, bg="#cef0f1", text="Enter Blood Pressure:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE3.place(x=55, y=341)

    
    ENTRY2 = Entry(TOP, bd=1, width=16, font="Roboto 11")
    ENTRY2.place(x=240, y=131)
    ENTRY3 = Entry(TOP, bd=1, width=16, font="Roboto 11")
    ENTRY3.place(x=240, y=181)

    ENTRY4 = Entry(TOP, bd=1, width=16, font="Roboto 11")
    ENTRY4.place(x=240, y=232)

    ENTRY5 = Entry(TOP, bd=1, width=16, font="Roboto 11")
    ENTRY5.place(x=240, y=293)

    ENTRY6 = Entry(TOP, bd=1, width=16, font="Roboto 11")
    ENTRY6.place(x=240, y=341)



    
    
    BUTTON = Button(bg="#2187e7", bd=1, text="SUBMIT",padx=10, pady=10,  command=calculate_age,foreground="white",
                    font=("Helvetica", 10, "bold"))
    
    BUTTON.place(x=155, y=420)
    plot_button = Button(master = TOP, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "PLOT",bg="#2187e7",foreground="white",font=("Helvetica", 10, "bold"))
  
 
    # in main window
    plot_button.place(x=255, y=420)
    #plt.show()


  

 

    TOP.mainloop()

