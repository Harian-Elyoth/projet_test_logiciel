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

	# connection success 
	def test_reach_server(self):
		pass

	# --------------------- #
	# TEST REQUEST FUNCTION #
	# --------------------- #

	# method is a string
	def test_method_type(self):
		pass

	# method is GET or POST
	def test_method_format(self):
		pass

	# endpoint is a string
	def test_endpoint_type(self):
		pass

	# endpoint is something like /toto/titit
	def test_endpoint_format(self):
		pass

	# body is a string
	def test_body_type(self):
		pass

	# header is a dict
	def test_header_type(self):
		pass

	# raise expection
	def test_header_format(self):
		pass

	# called at end
	def tearDown(self):
		pass


if __name__ == '__main__':

	unittest.main()