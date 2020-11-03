from tkinter import *

window = Tk()
window.title("Student No: 789456123")
window.geometry("600x500")


#Labels
l1 = Label(window, text="SicknessCode: ")
l1.place(x=25, y=150, anchor="w")

l2 = Label(window, text="DurationofTreatment: ")
l2.place(x=25, y=200, anchor="w")

l3 = Label(window, text="Weeks/Months")
l3.place(x=390, y=188)

l4 = Label(window, text="DoctorPracticeNumber: ")
l4.place(x=25, y=250, anchor="w")

l5 = Label(window, text="Scan/Consultation Fee: ")
l5.place(x=25, y=300, anchor="w")

l6 = Label(window, text="AmountPaidForTreatment: ")
l6.place(x=25, y=400)


#Creating classes
class SickCode:
    def __init__(self):
        # Creating the entry boxes
        self.sick_code = Entry(window)
        self.sick_code.place(x=300, y=135)

        self.duration = Entry(window, width=10)
        self.duration.place(x=300, y=185)

        self.doc_num = Entry(window)
        self.doc_num.place(x=300, y=235)

        self.scan_or_consult = Entry(window)
        self.scan_or_consult.place(x = 300, y = 285)

        self.v = IntVar()

# Creating the buttons

btn1 = Radiobutton(window, text="Cancer", value=1)
btn1.place(x=20, y=330)

btn2 = Radiobutton(window, text="Influenza", value=2)
btn2.place(x=20, y=360)

exit_btn = Button(window, text="Exit", command=window.destroy).place(x=425, y=450)


def clear(self, sick_code, duration, doc_num, scan_or_consult):
    self.sick_code.delete(0, 'end')
    self.duration.delete(0, 'end')
    self.doc_num.delete(0, 'end')
    self.scan_or_consult.delete(0, 'end')


clear_btn = Button(window, text="Clear", command=clear)
clear_btn.place(x=225, y=450)

#Class for Cancer and INfluenza

class Cancer:

    def __init__(self, scan):
        amount_paid_display = Label(window, text="")
        amount_paid_display.place(x=225, y=400)
        medication = 400
        self.scan = scan

        if float(scan) > 600:
            Message.showinfo("", "Sorry we cannot treat you")
        else:
            amount_paid = float(scan) + medication
            amount_paid_display.config(text="R"+str(round(amount_paid, 4)))

#Child of sick class for influenza calculation and display
class Influenza:

    def __init__(self, consult):
        x = StringVar()
        amount_paid_display = Label(window, textvariable=x)
        amount_paid_display.place(x=225, y=400)
        medication = 350.50
        self.consult = consult
        consult = float(consult)

        if consult > 600:
            consult = 0.98*consult
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")
        else:
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")

# Calculate and its definition
def calculate(self):
    radio = self.v.get()
    if radio == 1:
        can = Cancer(self.scan_or_consult.get())
    elif radio == 2:
        flu = Influenza(self.scan_or_consult.get())

calculate_btn = Button(window, text="Calculate", command=calculate)
calculate_btn.place(x=25, y=450)



app = SickCode()
window.mainloop()