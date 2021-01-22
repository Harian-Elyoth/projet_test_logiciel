# test class for http client

import unittest
from http_client import *

class test_http_client(unittest.TestCase):

	# called at start
	def setUp(self):
		pass

	# --------------------- #
	# TEST __NEW__ FUNCTION #
	# --------------------- #

	# everything's fine
	def test_new(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20), 0)

	# ip is a string
	def test_ip_server_type(self):
		self.assertEqual(http_client("127.0.0.1", 65500, 192.168, 65501, 20), -1)

	# ip is something like 192.168.41.2
	def test_ip_server_format(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "1923.17.435.6524", 65501, 20), -2)

	# port is an integer
	def test_port_server_type(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", "65501", 20), -3)

	# port is between 0 and 65535
	def test_port_server_format(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", -65501, 20), -4)
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 66000, 20) , -4)

	# port is available : 49152 - 65535
	def test_port_server_allow(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 15, 20), -5)

	# timeout is an integer
	def test_timeout_type(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, "20"), -6)

	# timeout is between 10 and 60
	def test_timeout_format(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 0) , -7)
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 70), -7)

	# ip is a string
	def test_ip_client_type(self):
		self.assertEqual(http_client(192.168, 65500, "127.0.0.1", 65501, 20), -8)

	# ip is something like 192.168.41.2
	def test_ip_client_format(self):
		self.assertEqual(http_client("1923.17.435.6524", 65500, "127.0.0.1", 65501, 20), -9)

	# port is an integer
	def test_port_client_type(self):
		self.assertEqual(http_client("127.0.0.1", "65501", "192.168.47.1", 65500, 20), -10)

	# port is between 0 and 65535
	def test_port_client_format(self):
		self.assertEqual(http_client("127.0.0.1", -65501, "192.168.47.1", 65500, 20), -11)
		self.assertEqual(http_client("127.0.0.1", 66000, "192.168.47.1", 65500, 20) , -11)

	# port is available : 49152 - 65535
	def test_port_client_allow(self):
		self.assertEqual(http_client("127.0.0.1", 15, "192.168.47.1", 65500, 20), -12)

	# --------------------- #
	# TEST CONNECT FUNCTION #
	# --------------------- #

	# connection success 
	def test_reach_server(self):
		http_client_test = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		self.assertEqual(http_client_test.connect(), -1)

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