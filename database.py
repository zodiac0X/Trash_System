import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect("trashsys.db")
		self._db.row_factory = sqlite3.Row
		self._db.execute("create table if not exists Trash(ID integer primary key autoincrement,Name text,id_number text,va_ty text,va_num text,trash_ty text,date text)")
		self._db.commit()
	def Add(self,name,id_num,var_ty,var_num,trash_ty,dates):
		self._db.execute("insert into Trash(Name,id_number,va_ty,va_num,trash_ty,date) values(?,?,?,?,?,?)",(name,id_num,var_ty,var_num,trash_ty,dates))
		self._db.commit()
		return "Add is submitted..."

	def list_date(self):
		cur = self._db.execute("Select * from Trash")
		return cur
