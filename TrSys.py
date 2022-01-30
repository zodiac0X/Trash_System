from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from database import DBConnect
from ListShow import ListTrash


db = DBConnect() 
root = Tk()
root.iconbitmap("trash_dCf_icon.ico")
root.title("Trash System")
#style 
style = ttk.Style()
style.theme_use("classic")
style.configure("TLabel",background="#e1d8b2")

#Full Name
ttk.Label(root, text="Full Name:").grid(row=0,column=0,padx=10,pady=10)
EnteryFullName=ttk.Entry(root,width=30,font=('Arial',16))
EnteryFullName.grid(row=0,column=1,columnspan=2,pady=10)
#Date
ttk.Label(root, text="Date:").grid(row=1,column=0)
cal= DateEntry(root,selectmode='day',width=30)
cal.grid(row=1,column=1,pady=10,columnspan=2)
#ID Number
ttk.Label(root, text="ID Number:").grid(row=2,column=0,padx=10,pady=10)
EnteryID=ttk.Entry(root,width=30,font=('Arial',16))
EnteryID.grid(row=2,column=1,columnspan=2,pady=10)
#Vehicle type
ttk.Label(root, text="Vehicle type:").grid(row=3,column=0,padx=10,pady=10)
EnteryVT=ttk.Entry(root,width=30,font=('Arial',16))
EnteryVT.grid(row=3,column=1,columnspan=2,pady=10)
#Vehicle Number
ttk.Label(root, text="Vehicle Number:").grid(row=4,column=0,padx=10,pady=10)
EnteryVN=ttk.Entry(root,width=30,font=('Arial',16))
EnteryVN.grid(row=4,column=1,columnspan=2,pady=10)
#Trash Type 
ttk.Label(root, text="Trash Type:").grid(row=5,column=0,padx=10,pady=10)
n = StringVar()
trashchoosen = ttk.Combobox(root, width = 30, textvariable = n)
trashchoosen['values'] = (
	'Household trash',
	'Plastic ',
	'Minerals ',
	'Natural materials',
	'Building materials'
	)
trashchoosen.grid(row=5,column=1,columnspan=2,pady=10)
#Submit
enter = ttk.Button(root,text="Enter")
enter.grid(row=6,column=3)
lists = ttk.Button(root,text="List")
lists.grid(row=6,column=2)

#data 

def Save_date():
	if(EnteryFullName.get() == '' or EnteryVT.get() == '' or EnteryID.get() == '' or EnteryVN.get() == ''):
		messagebox.showinfo(title='Add info', message="Some data is empty")
	else:
		msg = db.Add(EnteryFullName.get(),EnteryID.get(),EnteryVT.get(),EnteryVN.get(),trashchoosen.get(),cal.get())
		messagebox.showinfo(title='Add info', message=msg)

def BuList():
	#TODO: show orders
	listshow = ListTrash()


enter.config(command=lambda:Save_date())
lists.config(command=lambda:BuList())
root.mainloop()