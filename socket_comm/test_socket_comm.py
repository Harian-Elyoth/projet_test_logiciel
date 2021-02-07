import unittest
from socket_comm import socket_comm
from mock import patch

class test_socket_comm(unittest.TestCase):

	# --------------------- #
	# TEST __NEW__ FUNCTION #
	# --------------------- #

	# everything's fine
	def test_new(self):
		pass

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

	# --------------------- #
	# TEST LISTEN FUNCTION #
	# --------------------- #

	# everything's fine
	def test_listen(self):
		pass

	# ip is a string
	def test_listen_backlog_type(self):
		pass

	# --------------------- #
	# TEST CONNECT FUNCTION #
	# --------------------- #

	# everything's fine
	def test_connect(self):
		pass

	# ip is a string
	def test_connect_ip_type(self):
		pass

	# ip is something like 192.168.41.2
	def test_connect_ip_format(self):
		pass

	# port is an integer
	def test_connect_port_type(self):
		pass

	# port is between 0 and 65535
	def test_connect_port_format(self):
		pass

	# port is available : 49152 - 65535
	def test_connect_port_allow(self):
		pass

if __name__ == '__main__':
	unittest.main()
