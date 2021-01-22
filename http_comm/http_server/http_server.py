# class for http server

import http.server

class http_server(http.server.BaseHTTPRequestHandler):

	"""docstring for http_server"""
	def __init__(self, ip, port):
		super(http_server, self).__init__()

		self.ip 		= ip
		self.port 		= port

		self.http_serv 	= http.server.HTTPServer((self.ip, self.port), MyHandler)

		try:
			# self.http_serv.serve_forever()
			pass
		except KeyboardInterrupt:
			# self.__exit__()
			pass

	# handle GET request
	def do_GET():
		pass

	# handle POST request
	def do_POST():
		pass
		
	# called when we close the server
	def exit():
		# httpd.server_close()
		pass