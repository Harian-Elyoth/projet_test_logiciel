#/***********************************************
#     Authors : Yingshan LIU, Mingda WANG
#************************************************/

import urllib.parse, sqlite3

class sql():
	def __init__(self, name):
		self.c = None
		self.req = None
		self.conn = sqlite3.connect(name)
		self.c = self.conn.cursor()

	def __exit__(self, exc_type, exc_value, traceback):
		self.conn.close()

	def select(self,path):
		elem = path.split('/')
		if len(elem) == 2:
			self.req = "select * from %s" %(elem[1])
		elif len(elem) == 3:
			self.req = "select %s from %s" %(elem[2],elem[1])
		elif len(elem) == 5:
			self.req = "select %s from %s where %s='%s'" %(elem[2],elem[1],elem[3],elem[4])

		# print(self.req)

		return self.c.execute(self.req).fetchall()
	
	def insert(self,path,query):
		# print("query")
		# print(query)
		# print("")
		attr = ', '.join(query.keys())
		val = ', '.join('"%s"' %v[0] for v in query.values())
		# print('attr')
		# print(attr)
		# print("")
		# print('val')
		# print(val)
		# print("")
		req = "insert into %s (%s) values (%s)" %(path.split('/')[1], attr, val)
		# print('req')
		# print(req)
		# print("")
		self.c.execute(req)
		self.conn.commit()

	def delete(self,path):
		elem = path.split('/')
		if len(elem) == 2:
			req = "delete * from %s" %(elem[1])#
		elif len(elem) == 3:
			req = "alter table %s drop column %s" %(elem[1],elem[2])
		elif len(elem) == 4:
			req = "delete from %s where %s=%s" %(elem[1],elem[2],elem[3])
		self.c.execute(req)
		self.conn.commit()
