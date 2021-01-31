# test class for http server

import unittest

from http_server import *

# library for launch requests on a server
import requests

import threading

# def create_right_serv():
# 	ip 		= "127.0.0.1"
# 	port 	= 65500
		
# 	serv 	= http_server(ip, port)

# f = lambda ip,port: http_server(ip, port)

# threading.Thread(target=f("127.0.0.1", 65500)).start()

class test_http_server(unittest.TestCase):

	# called at start
	def setUp(self):
		pass

	# --------------------- #
	# TEST __NEW__ FUNCTION #
	# --------------------- #

	# everything's fine
	def test_new(self):
		# THREAD OU MOCK
		# self.assertEqual(http_server("127.0.0.1", 65500), 0)
		pass

	# ip is a string
	def test_ip_type(self):
		self.assertEqual(http_server(65500, 65500), -1)

	# ip is something like 192.168.41.2
	def test_ip_format(self):
		self.assertEqual(http_server("127.899.320.490", 65500), -2)

	# port is an integer
	def test_port_type(self):
		self.assertEqual(http_server("127.0.0.1", "65500"), -3)

	# port is between 0 and 65535
	def test_port_format(self):
		self.assertEqual(http_server("127.0.0.1",   -15), -4)
		self.assertEqual(http_server("127.0.0.1", 65800), -4)

	# port is available : 49152 - 65535
	def test_port_allow(self):
		self.assertEqual(http_server("127.0.0.1",    15), -4)
		self.assertEqual(http_server("127.0.0.1", 65800), -4)

	# -------------------- #
	# TEST DO_GET FUNCTION #
	# -------------------- #

	# do a GET on the server, everything's fine
	def test_get(self):

		# TRY CREATE THREAD TO LAUNCH SERVER WHILE TESTING
		# def create_right_serv():
		# 	ip 		= "127.0.0.1"
		# 	port 	= 65500
				
		# 	serv 	= http_server(ip, port)

		# 	try:
		# 		serv.http_serv.serve_forever()
		# 	except KeyboardInterrupt:
		# 		pass

		# threading.Thread(target=create_right_serv).start()

		# TESTING
		# url 	= "http://127.0.0.1:65500"
		# resp 	= requests.get(url)

		# self.assertEqual((int)(resp.status_code), 200)

	# do a GET on the server, endpoint not found
	def test_get_not_found(self):
		# CAN'T TEST WITHOUT A ACTIVE SERVER, WAIT FOR THREAD OR MOCK
		# url 	= "http://127.0.0.1:65500/room"
		# resp 	= requests.get(url)

		# self.assertEqual((int)(resp.status_code), 404)

	# --------------------- #
	# TEST DO_POST FUNCTION #
	# --------------------- #

		# do a POST on the server, everything's fine
	def test_post():
		# CAN'T TEST WITHOUT A ACTIVE SERVER, WAIT FOR THREAD OR MOCK
		# url 	= "http://127.0.0.1:65500"
		# payload = "test"
		# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		# resp 	= requests.post(url, data=payload, headers=headers)

		# self.assertEqual((int)(resp.status_code), 200)

	# do a POST on the server, endpoint not found
	def test_post_not_found():
		# CAN'T TEST WITHOUT A ACTIVE SERVER, WAIT FOR THREAD OR MOCK
		# url 	= "http://127.0.0.1:65500/room"
		# payload = "test"
		# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		# resp 	= requests.post(url, data=payload, headers=headers)

		# self.assertEqual((int)(resp.status_code), 404)

if __name__ == '__main__':

	unittest.main()