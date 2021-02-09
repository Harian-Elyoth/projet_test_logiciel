
from sql import sql
import http.server
from io import BytesIO
import sqlite3

class handler_http_serv(http.server.BaseHTTPRequestHandler):

	"""docstring for handler_http_serv class"""

	def __init__(self, *args, **kwargs):		
		self.mysql = sql('chatsystem.db')
		super(handler_http_serv, self).__init__(*args, **kwargs)

	"""handle GET request"""
	def do_GET(self):

		# print("do_GET : path = " + self.path)

		if self.path == '/':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			body = 	b'server : OK'
			self.wfile.write(body)

		elif self.path == '/room':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			resp = self.mysql.select("/Room/roomName")	
			
			resp_str = ''
			for elem in resp:
				resp_str += '-> ' + str(elem[0]) + '\n'

			body = resp_str.encode()

			self.wfile.write(body)

		else:
			self.send_response(404)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			self.wfile.write(b'error : end point')

	"""handle POST request"""
	def do_POST(self):

		# print("do_POST : path = " + self.path)

		if self.path == '/':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			body = 	b'server : OK'
			self.wfile.write(body)

		elif self.path == '/username':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			content_length = int(self.headers['Content-Length'])
			username = self.rfile.read(content_length)

			username_str = username.decode("utf-8")
			if verify_sql_injection(username_str):
				resp = self.mysql.select(("/User/username/username/" + username_str))
				if(len(resp) > 0):
					body = 	b'username : OK'
				else:
					body = 	b'username : KO'
			else : 
				print("Attention SQL INJECTION DETECTEE")
				body = 	b'username : KO'



			response = BytesIO()
			response.write(body)
			
			self.wfile.write(response.getvalue())

		elif self.path == '/password':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			content_length = int(self.headers['Content-Length'])
			password = self.rfile.read(content_length)

			password_str = password.decode("utf-8")
			if verify_sql_injection(password_str):
				resp = self.mysql.select(("/User/password/password/" + password_str))
				if(len(resp) > 0):
					body = 	b'password : OK'
				else:
					body = 	b'password : KO'
			else : 
				print("Attention SQL INJECTION DETECTEE")
				body = 	b'password : KO'




			response = BytesIO()
			response.write(body)

			self.wfile.write(response.getvalue())

		elif self.path == '/room':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			content_length = int(self.headers['Content-Length'])
			channel = self.rfile.read(content_length)

			channel_str = channel.decode("utf-8")

			resp = self.mysql.select(("/Room/roomName/roomName/" + channel_str))

			if(len(resp) > 0):
				body = 	b'room : OK'
			else:
				body = 	b'room : KO'

			response = BytesIO()
			response.write(body)

		elif self.path == '/create':
			self.send_response(200)

			self.send_header("Content-type", "text/plain")
			self.end_headers()

			content_length = int(self.headers['Content-Length'])
			channel = self.rfile.read(content_length)

			channel_str = channel.decode("utf-8")
			if verify_roomname(channel_str):
				query = {'roomName': [channel_str]}

			# EVENTUAL CONDITION ON NEW ROOM'S NAME (LENGHT, SPEC CHAR)

				resp = self.mysql.insert("/Room", query)

				body = 	b'create : OK'
			else : 
				print("ROOMNAME INCORRECT")
				body =  b'create : KO'

			response = BytesIO()
			response.write(body)

			self.wfile.write(response.getvalue())

		else:
			self.send_response(404)
			self.end_headers()
			self.wfile.write(b'error : end point')

class http_server(object):

	"""docstring for http_server class"""

	"""called when creating instance, return an object (can be an integer)"""
	def __new__(self, ip, port):

		# TESTS on parameters

		# test ip type
		if type(ip) != str:
			return -1

		# test ip_server format
		ip_bytes = []
		ip_bytes = ip.split(".")

		if len(ip_bytes) == 4:
			for ip_byte in ip_bytes:
				int_ip_byte = int(ip_byte)

				if int_ip_byte < 0 or int_ip_byte > 255:
					return -2
		else:
			return -2

		# test port type
		if type(port) != int:
			return -3

		# test port format
		if port > 0 and port < 65535:
			if port < 49152:
				return -5
		else:
			return -4

		return super(http_server, self).__new__(self)

	"""called for initialize object (after new), return None"""
	def __init__(self, ip, port):

		self.ip 		= ip
		self.port 		= port

		try:
			self.http_serv 	= http.server.ThreadingHTTPServer((self.ip, self.port), handler_http_serv)
		except:
			print("Exception in http.server.ThreadingHTTPServer(..)")

	def run(self):
		try:
			self.http_serv.serve_forever()
		except KeyboardInterrupt:
			print("Exception in serve_forever()")


	"""called when there not references anymore to close the server"""
	def __del__(self):
		self.http_serv.server_close()
		# pass

#return true si il n'y a pas de risque d'injection sql
#false sinon
def verify_sql_injection(request):
	banlist = ["\'", "--", ";", "\"", "OR", "SELECT", "DROP", "UNION", "UPDATE", "DELETE", "INSERT"]
	#print(not(any(request.upper().count(banlist[i]) >= 1 for i in range(len(banlist)))))
	return not(any(request.upper().count(banlist[i]) >= 1 for i in range(len(banlist))))

#Limite de caractere
def verify_roomname(roomname):
	special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	if not any(char in special_characters for char in roomname):
		#Si il ne contient aucun symbole
		if len(roomname) <= 40 :
			connect = sqlite3.connect('chatsystem.db')
			cursor = connect.cursor()
			sql = 'SELECT * FROM Room WHERE roomName="%s"' %(roomname)
			rep = cursor.execute(sql).fetchall()
			if len(rep)==0:
				return True
	return False
	

if __name__ == '__main__':

	serv_test = http_server("127.0.0.1", 60000)

	serv_test.run()
