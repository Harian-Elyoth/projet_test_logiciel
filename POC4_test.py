from class_interface import MySQL
import unittest,os,sys,sqlite3

conn = sqlite3.connect('chatsystem.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
#download the db in POC3
db_path = 'chatsystem.db'


#CREATE TABLE User (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, username TEXT, password TEXT, adminStatus BOOLEAN);
mysql = MySQL('chatsystem.db')

class TestDB(unittest.TestCase):
	def test_A_user_select(self):
		ex1 = mysql.select("127.0.0.1:8888/User")
		ex2 = mysql.select("127.0.0.1:8888/User/username")
		ex3 = mysql.select("127.0.0.1:8888/User/username/password/'MissEmma'")

		ex1_1 = [ex[1] for ex in ex1]
		ex2_1 = [ex[0] for ex in ex2]
		ex3_1 = [ex[0] for ex in ex3]

		self.assertEqual(ex1_1,['Emma'])
		self.assertEqual(ex2_1,['MissEmma'])
		self.assertEqual(ex3_1,['jhLO7649'])

	def test_B_user_insert(self):
		query = "{'firstName':['Yingshan'],'lastName':['LIU'],'username': ['yingshan'], 'password': ['password1'],'adminStatus': [false]}"
		mysql.insert("127.0.0.1:8888/User",query)

		sql = "select username from User where username = 'yingshan';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'yingshan')

	def test_C_user_delete(self):
		mysql.delete("127.0.0.1:8888/User/username/'yingshan'")

		sql = "select username from User where username = 'yingshan';"
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
		mysql.delete("127.0.0.1:8888/Room/roomName/'Emergency meeting'")

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
		ex1 = mysql.select("127.0.0.1:8888/Room_User_Table/1/idUser/idRoom")

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
		mysql.delete("127.0.0.1:8888/Room_User_Table/idRoom/5")

		sql = "select idRoom from Room_User_Table where idRoom = 5;"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')

	def test_J_message_select(self):
		#Known room_id, return the record
		ex1 = mysql.select("127.0.0.1:8888/Message/1/content/idRoom")

		ex1_1 = [ex[0] for ex in ex1]

		self.assertEqual(ex1_1,["Philippe, you must call the IT department"])

	def test_K_message_insert(self):
		query = "{'idRoom': [1], 'idUser': [2],'content':['OK,I will call them']}"
		mysql.insert("127.0.0.1:8888/Message",query)

		sql = "select content from Message where content = 'OK,I will call them';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'OK,I will call them')

	def test_L_message_delete(self):
		mysql.delete("127.0.0.1:8888/Message/idUser/1")

		sql = "select content from Message where idUser = 1;"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')

if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()
