# test class for http server

import unittest
from http_server import *

class test_http_server(unittest.TestCase):

	# called at start
	def setUp(self):
		pass

	# ---------------------- #
	# TEST __INIT__ FUNCTION #
	# ---------------------- #

	# ip is a string
	def test_ip_type(self):
		pass

	# ip is something like 192.168.41.2
	def test_ip_format(self):
		pass

	# port is an integer
	def test_port_type(self):
		pass

	# port is between 0 and 65535
	def test_port_format(self):
		pass

	# port is available : 49152 - 65535
	def test_port_allow(self):
		pass


	# -------------------- #
	# TEST DO_GET FUNCTION #
	# -------------------- #


	# --------------------- #
	# TEST DO_POST FUNCTION #
	# --------------------- #




if __name__ == '__main__':

	unittest.main()