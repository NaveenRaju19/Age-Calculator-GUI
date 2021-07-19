from tkinter import *
from datetime import date
root=Tk()
root.geometry("500x500")
root.title("Age Calculator App")
def calculateage():
    today=date.today()
    birthdate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    days=age*365
    months=age*12
    hours=days*24
    mins=hours*60
    secs=mins*60
    Label(text=f" Your Age is  :{age} Years").grid(row=40,column=1)
    Label(text=f" Total Number Of Days Till Now is:  {days} Days.").grid(row=50,column=1)
    Label(text=f" Total Number Of Months Till Now is:  {months} Months.").grid(row=80,column=1)
    Label(text=f" Total Number Of Hours Till Now is:  {hours} Hours.").grid(row=110,column=1)
    Label(text=f" Total Number Of Minutes Till Now is:  {mins} Minutes.").grid(row=140,column=1)
    Label(text=f" Total Number Of Seconds Till Now is:  {secs} Seconds.").grid(row=170,column=1)
    
Label(text="Name:").grid(row=1, column=0, padx=90)
Label(text="Year:").grid(row=2, column=0)
Label(text="Month:").grid(row=3, column=0)
Label(text="Day:").grid(row=4, column=0)
namevalue= str()
yearvalue=str()
monthvalue=str()
dayvalue=str()
nameEntry=Entry(root, textvariable = namevalue)
yearEntry=Entry(root, textvariable = yearvalue)
monthEntry=Entry(root, textvariable = monthvalue)
dayEntry=Entry(root, textvariable = yearvalue)
nameEntry.grid(row=1,column=1,pady=10)
yearEntry.grid(row=2,column=1,pady=10)
monthEntry.grid(row=3,column=1,pady=10)
dayEntry.grid(row=4,column=1,pady=10)
Button(text="CALCULATE AGE",bg="violet",command=calculateage).grid(row=5,column=1,pady=10)



