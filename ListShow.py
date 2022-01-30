from tkinter import ttk
from tkinter import *
from database import DBConnect

db = DBConnect()
class ListTrash:
	def __init__(self):
		self._root=Tk()
		self._root.iconbitmap("trash_dCf_icon.ico")
		self._db = DBConnect()
		self._root.title("List Data")
		tv = ttk.Treeview(self._root)
		tv.pack()
		tv.heading('#0',text='ID')
		tv.configure(column=("#Name","#id_number","#va_ty","#va_num","#trash_ty","#date"))
		tv.heading('#Name',text='Full Name')
		tv.heading('#id_number',text='ID Number')
		tv.heading('#va_ty',text='Vehicle type')
		tv.heading('#va_num',text='Vehicle Number')
		tv.heading('#trash_ty',text='Trash Type')
		tv.heading('#date',text='date')
		cur = self._db.list_date()
		for row in cur:
			tv.insert('',"end",'#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#id_number',row['id_number'])
			tv.set('#{}'.format(row['ID']),'#va_ty',row['va_ty'])
			tv.set('#{}'.format(row['ID']),'#va_num',row['va_num'])
			tv.set('#{}'.format(row['ID']),'#trash_ty',row['trash_ty'])
			tv.set('#{}'.format(row['ID']),'#date',row['date'])


		self._root.mainloop()


