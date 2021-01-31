# test class for http server

import unittest

from http_server import *

# library for launch requests on a server
import requests 			

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
		pass

	# do a GET on the server, endpoint not found
	def test_get_not_found(self):
		pass

	# --------------------- #
	# TEST DO_POST FUNCTION #
	# --------------------- #

	# do a POST on the server, everything's fine
	def test_post(self):
		pass

	# do a POST on the server, endpoint not found
	def test_post_not_found(self):
		pass

if __name__ == '__main__':

	unittest.main()