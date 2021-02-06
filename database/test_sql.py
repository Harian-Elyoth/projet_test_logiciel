#/***********************************************
#     Authors : Yingshan LIU, Mingda WANG
#************************************************/

from class_interface import sql

import unittest
import os
import sys
import sqlite3

# CREATE TABLE User (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, username TEXT, password TEXT, adminStatus BOOLEAN);
mysql = sql('chatsystem.db')

class test_sql(unittest.TestCase):
	def test_user_select(self):
		ex1 = mysql.select("127.0.0.1:8888/User")
		ex2 = mysql.select("127.0.0.1:8888/User/username")
		ex3 = mysql.select("127.0.0.1:8888/User/password/username/'MissEmma'")
		ex1_1 = [ex[1] for ex in ex1]
		ex2_1 = [ex[0] for ex in ex2]
		ex3_1 = [ex[0] for ex in ex3]

		self.assertEqual(ex1_1,['John', 'Jane', 'Philippe', 'Karine', 'Theo', 'Emma'])
		self.assertEqual(ex2_1,['Dr.JD', 'MsJD', 'Durandil', 'Kami', 'Ostheoporose', 'MissEmma'])
		self.assertEqual(ex3_1,['jhLO7649'])

	def test_user_insert(self):
		query = {'firstName':['Yingshan'],'lastName':['LIU'],'username': ['yingshan'], 'password': ['password1'],'adminStatus': [0]}
		mysql.insert("127.0.0.1:8888/User",query)

		sql = "select username from User where username = 'yingshan';"
		name = ''
		for row in mysql.select("127.0.0.1:8888/User/username/username/'yingshan'"):
			name = row[0]
		self.assertEqual(name,'yingshan')

	def test_user_delete(self):
		mysql.delete("127.0.0.1:8888/User/username/'yingshan'")

		sql = "select username from User where username = 'yingshan';"
		none = ''
		for row in mysql.select("127.0.0.1:8888/User/username/username/'yingshan'"):
			none = row[0]
		self.assertEqual(none,'')

	def test_room_select(self):

		ex1 = mysql.select("127.0.0.1:8888/Room")
		ex2 = mysql.select("127.0.0.1:8888/Room/roomName")
		ex1_1 = [ex[0] for ex in ex1]
		ex2_1 = [ex[0] for ex in ex2]

		self.assertEqual(ex1_1,[1, 2, 3])
		self.assertEqual(ex2_1,["Emergency meeting","Daily news","Weekly report"])

	def test_room_delete(self):
		mysql.delete("127.0.0.1:8888/Room/roomName/'Emergency meeting'")

		sql = "select id from Room where roomName = 'Emergency meeting';"
		none = ''
		for row in mysql.select("127.0.0.1:8888/Room/roomName/roomName/'Emergency meeting'"):
			none = row[0]
		self.assertEqual(none,'')

	def test_room_insert(self):
		query = {'roomName': ['My meeting']}
		mysql.insert("127.0.0.1:8888/Room",query)

		# sql = "select roomName from Room where roomName = 'Emergency meeting';"
		name = ''
		for row in mysql.select("127.0.0.1:8888/Room/roomName/roomName/'My meeting'"):
			name = row[0]
		self.assertEqual(name,'My meeting')
#
	def test_table_select(self):
		#Known room_id, return the record
		ex1 = mysql.select("127.0.0.1:8888/Room_User_Table/idUser/idRoom/1")
		ex1_1 = [ex[0] for ex in ex1]

		self.assertEqual(ex1_1,[1,2])

	def test_table_insert(self):
		query = {'idRoom': [5], 'idUser': [1]}
		mysql.insert("127.0.0.1:8888/Room_User_Table",query)

		sql = "select idRoom from Room_User_Table where idRoom = 5;"
		name = ''
		for row in mysql.select("127.0.0.1:8888/Room_User_Table/idRoom/idRoom/5"):
			name = row[0]
		self.assertEqual(name,5)

	def test_table_delete(self):
		mysql.delete("127.0.0.1:8888/Room_User_Table/idRoom/5")

		sql = "select idRoom from Room_User_Table where idRoom = 5;"
		none = ''
		for row in mysql.select("127.0.0.1:8888/Room_User_Table/idRoom/idRoom/5"):
			none = row[0]
		self.assertEqual(none,'')

	def test_message_select(self):
		#Known room_id, return the record
		ex1 = mysql.select("127.0.0.1:8888/Message/content/idRoom/1")
		# print(ex1)
		ex1_1 = [ex[0] for ex in ex1]

		self.assertEqual(ex1_1,["Philippe, you must call the IT department"])

	def test_message_insert(self):
		query = {'idRoom': [1], 'idUser': [2],'content':['OK,I will call them']}
		mysql.insert("127.0.0.1:8888/Message",query)

		sql = "select content from Message where content = 'OK,I will call them';"
		name = ''
		for row in mysql.select("127.0.0.1:8888/Message/content/content/'OK,I will call them'"):
			name = row[0]
		self.assertEqual(name,'OK,I will call them')

	def test_message_delete(self):
		mysql.delete("127.0.0.1:8888/Message/idUser/1")

		sql = "select content from Message where idUser = 1;"
		none = ''
		for row in mysql.select("127.0.0.1:8888/Message/content/idUser/1"):
			none = row[0]
		self.assertEqual(none,'')

if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()