# class for http server

import http.server

class handler_http_serv(http.server.BaseHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		super(handler_http_serv, self).__init__(*args, **kwargs)
			
	# handle GET request
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		# pass

	# handle POST request
	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		# pass

class http_server(object):

	"""docstring for http_server"""

	# called when creating instance, return an object (can be an integer)
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

	# called for initialize object (after new), return None
	def __init__(self, ip, port):
		
		# super(http_server, self).__init__(self)

		self.ip 		= ip
		self.port 		= port

		try:
			self.http_serv 	= http.server.HTTPServer((self.ip, self.port), handler_http_serv)
		except:
			pass

		# try:
		# 	self.http_serv.serve_forever()
		# except KeyboardInterrupt:
		# 	pass
		
	# called when there not references anymore to close the server
	def __del__(self):
		# self.http_serv.server_close()
		pass


# serv_test = http_server("127.0.0.1", 65500)
# serv_test_2 = http_server("127.899.320.490", 65500)
