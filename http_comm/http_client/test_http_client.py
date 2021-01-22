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
	def test_connect(self):
		pass

	# connection failed
	def test_server_unreachable(self):
		bad_client_class = http_client("127.0.0.1", 65500, "192.168.47.0", 65501, 20)
		self.assertEqual(bad_client_class.connect(), -1)

	# --------------------- #
	# TEST REQUEST FUNCTION #
	# --------------------- #

	def test_request_get(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()

		self.assertEqual(good_client_class.request('GET', '/', good_header, ''), 0)

	def test_request_post(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()
		
		self.assertEqual(good_client_class.request('POST', '/', good_header, 'Hello Server !'), 0)

	# method is a string
	def test_method_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()

		self.assertEqual(good_client_class.request(0, '/', good_header, ''), -1)

	# method is GET or POST
	def test_method_format(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()

		self.assertEqual(good_client_class.request('GETE', '/', good_header, ''), -2)

	# endpoint is a string
	def test_endpoint_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()
		self.assertEqual(good_client_class.request('GET', 0, good_header, ''), -3)

	# endpoint is something like /toto/titit
	def test_endpoint_format(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()
		
		self.assertEqual(good_client_class.request('GET', 'bad_endpoint', good_header, ''), -4)

	# body is a string
	def test_body_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		good_client_class.connect()
		
		self.assertEqual(good_client_class.request('GET', '/', good_header, 0), -5)

	# header is a dict
	def test_header_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		good_client_class.connect()
		self.assertEqual(good_client_class.request('GET', '/', 0, ''), -6)

	# raise expection
	def test_header_format(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 20)
		bad_header  = {"Cntent-typ": "pp/x-www-form-urlencoded", "ccept": "txtu/plin"}

		good_client_class.connect()

		self.assertEqual(good_client_class.request('GET', '/', bad_header, ''), -7)

	###################

	# called at end
	def tearDown(self):
		pass


if __name__ == '__main__':

	unittest.main()