import urllib.parse, sqlite3


class MySQL():
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
			req = "select * from %s" %(elem[1])
		elif len(elem) == 3:
			req = "select %s from %s" %(elem[2],elem[1])
		elif len(elem) == 5:
			req = "select %s from %s where %s=%s" %(elem[3],elem[1],elem[4],elem[2])
		return self.c.execute(req).fetchall()
	
	def insert(self,path,query):
		print(query)
		attr = ', '.join(query.keys())
		val = ', '.join('"%s"' %v[0] for v in query.values())
		print(attr,val)
		req = "insert into %s (%s) values (%s)" %(path.split('/')[1], attr, val)
		print(req)
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
