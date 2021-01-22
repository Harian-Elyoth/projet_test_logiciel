# test class for http client

import unittest
from http_client import *

class test_http_client(unittest.TestCase):

	# called at start
	def setUp(self):
		pass

	# ---------------------- #
	# TEST __INIT__ FUNCTION #
	# ---------------------- #

	# ip is a string
	def test_ip_server_type(self):
		pass

	# ip is something like 192.168.41.2
	def test_ip_server_format(self):
		pass

	# port is an integer
	def test_port_server_type(self):
		pass

	# port is between 0 and 65535
	def test_port_server_format(self):
		pass

	# port is available : 49152 - 65535
	def test_port_server_allow(self):
		pass

	# timeout is an integer
	def test_timeout_type(self):
		pass

	# timeout is between 10 and 60
	def test_timeout_format(self):
		pass

	# ip is a string
	def test_ip_client_type(self):
		pass

	# ip is something like 192.168.41.2
	def test_ip_client_format(self):
		pass

	# port is an integer
	def test_port_client_type(self):
		pass

	# port is between 0 and 65535
	def test_port_client_format(self):
		pass

	# port is available : 49152 - 65535
	def test_port_client_allow(self):
		pass

	# --------------------- #
	# TEST CONNECT FUNCTION #
	# --------------------- #


	# --------------------- #
	# TEST REQUEST FUNCTION #
	# --------------------- #


	# called at end
	def tearDown(self):
		pass


if __name__ == '__main__':

	unittest.main()