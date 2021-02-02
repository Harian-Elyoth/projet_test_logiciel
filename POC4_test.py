from class_interface import MySQL
import unittest,os,sys,sqlite3

conn = sqlite3.connect('chatsystem.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
#download the db in POC3
db_path = 'chatsystem.db'

c.execute('DROP TABLE IF EXISTS User;')
sql = 'CREATE TABLE User (idUser INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)'
c.execute(sql)
sql = 'INSERT INTO User (username,password) VALUES ("LIU","password")'
# c.execute(sql)
# c.execute('CREATE TABLE Room (idRoom INTEGER PRIMARY KEY AUTOINCREMENT, roomName TEXT);')
# c.execute('CREATE TABLE Room_User_Table (idRoom INTEGER, idUser INTEGER);')
# c.execute('CREATE TABLE Message (sendingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, idRoom INTEGER, idUser INTEGER, content TEXT);')

mysql = MySQL('chatsystem.db')

class TestDB(unittest.TestCase):
	def test_A_user_select(self):
		ex1 = mysql.select("127.0.0.1:8888/User")
		ex2 = mysql.select("127.0.0.1:8888/User/username")
		ex3 = mysql.select("127.0.0.1:8888/User/username/password")

		ex1_1 = [ex[1] for ex in ex1]
		ex2_1 = [ex[0] for ex in ex2]
		ex3_1 = [ex[0] for ex in ex3]

		self.assertEqual(ex1_1,["LIU"])
		self.assertEqual(ex2_1,["LIU"])
		self.assertEqual(ex3_1,["LIU"])

	def test_B_user_insert(self):
		query = "{'username': ['WANG'], 'password': ['password1']}"
		mysql.insert("127.0.0.1:8888/User",query)

		sql = "select username from User where username = 'WANG';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'WANG')

	def test_C_user_delete(self):
		mysql.delete("127.0.0.1:8888/User/username/'WANG'")

		sql = "select username from User where username = 'WANG';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
	def test_D_room_select(self):

		ex1 = mysql.select("127.0.0.1:8888/Room")
		ex2 = mysql.select("127.0.0.1:8888/Room/roomName")
		ex1_1 = [ex[0] for ex in ex1]
		ex2_1 = [ex[0] for ex in ex2]

		self.assertEqual(ex1_1,[1,2,3])
		self.assertEqual(ex2_1,["Emergency meeting","Daily news","Weekly report"])
	def test_E_room_delete(self):
		mysql.delete("127.0.0.1:8888/Room/'Emergency meeting'")

		sql = "select username from User where roomName = 'Emergency meeting';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')

	def test_F_room_insert(self):
		query = "{'roomName': ['Emergency meeting]}"
		mysql.insert("127.0.0.1:8888/Room",query)

		sql = "select roomName from Room where roomName = 'Emergency meeting';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'Emergency meeting')
#
	def test_G_table_select(self):
		#Known room_id, return the record
		ex1 = mysql.select("127.0.0.1:8888/Room_User_Table/1")

		ex1_1 = [ex[1] for ex in ex1]

		self.assertEqual(ex1_1,[1,2])

	def test_H_table_insert(self):
		query = "{'idRoom': [5], 'idUser': [1]}"
		mysql.insert("127.0.0.1:8888/Room_User_Table",query)

		sql = "select idRoom from Room_User_Table where idRoom = 5;"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,5)

	def test_I_table_delete(self):
		mysql.delete("127.0.0.1:8888/Room_User_Table/5")

		sql = "select idRoom from Room_User_Table where idRoom = 5;"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')

if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()