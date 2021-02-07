import unittest
from mock import patch
from socket_comm import socket_comm
import os, subprocess, shlex
import time

class test_socket_comm(unittest.TestCase):

	list_subprocess = []

	# --------------------- #
	# TEST __NEW__ FUNCTION #
	# --------------------- #

	# everything's fine
	def test_new(self):
		self.assertEqual(type(socket_comm("127.0.0.1", 65500)), socket_comm)

	# ip is a string
	def test_ip_type(self):
		self.assertEqual(socket_comm(192.168, 65501), -1)

	# ip is something like 192.168.41.2
	def test_ip_format(self):
		self.assertEqual(socket_comm("1923.17.435.6524", 65501), -2)

	# port is an integer
	def test_port_type(self):
		self.assertEqual(socket_comm("192.168.47.1", "65501"), -3)

	# port is between 0 and 65535
	def test_port_format(self):
		self.assertEqual(socket_comm("192.168.47.1", -65501), -4)
		self.assertEqual(socket_comm("192.168.47.1", 66000) , -4)

	# port is available : 49152 - 65535
	def test_port_allow(self):
		self.assertEqual(socket_comm("192.168.47.1", 15), -5)

	# --------------------- #
	# TEST LISTEN FUNCTION #
	# --------------------- #

	# everything's fine
	def test_listen(self):
		with patch('socket_comm.threading.Thread') as mock_thread_listen:
			good_socket_comm = socket_comm("127.0.0.1", 65500)
			good_backlog = 5
			self.assertEqual(good_socket_comm.listen(good_backlog), 0)

	# ip is a string
	def test_listen_backlog_type(self):
		with patch('socket_comm.threading.Thread') as mock_thread_listen:
			good_socket_comm = socket_comm("127.0.0.1", 65500)
			bad_backlog = "6"
			self.assertEqual(good_socket_comm.listen(bad_backlog), -1)

	# --------------------- #
	# TEST CONNECT FUNCTION #
	# --------------------- #

	# everything's fine
	def test_connect(self):
		with patch('socket_comm.threading.Thread') as mock_thread_connect:
			with patch('socket_comm.socket') as mock_socket:
				good_socket_comm = socket_comm("127.0.0.1", 65500)
				good_ip   = "127.0.0.1"
				good_port = 65501
				self.assertEqual(good_socket_comm.connect(good_ip, good_port), 0)

	# ip is a string
	def test_connect_ip_type(self):
		with patch('socket_comm.threading.Thread') as mock_thread_connect:
			with patch('socket_comm.socket') as mock_socket:
				good_socket_comm = socket_comm("127.0.0.1", 65500)
				bad_ip   = 192.168
				good_port = 65501
				self.assertEqual(good_socket_comm.connect(bad_ip, good_port), -1)

	# ip is something like 192.168.41.2
	def test_connect_ip_format(self):
		with patch('socket_comm.threading.Thread') as mock_thread_connect:
			with patch('socket_comm.socket') as mock_socket:
				good_socket_comm = socket_comm("127.0.0.1", 65500)
				bad_ip   = "1923.17.435.6524"
				good_port = 65501
				self.assertEqual(good_socket_comm.connect(bad_ip, good_port), -2)

	# port is an integer
	def test_connect_port_type(self):
		with patch('socket_comm.threading.Thread') as mock_thread_connect:
			with patch('socket_comm.socket') as mock_socket:
				good_socket_comm = socket_comm("127.0.0.1", 65500)
				good_ip  = "127.0.0.1"
				bad_port = "65501"
				self.assertEqual(good_socket_comm.connect(good_ip, bad_port), -3)

	# port is between 0 and 65535
	def test_connect_port_format(self):
		with patch('socket_comm.threading.Thread') as mock_thread_connect:
			with patch('socket_comm.socket') as mock_socket:
				good_socket_comm = socket_comm("127.0.0.1", 65500)
				good_ip   = "127.0.0.1"
				bad_port = -65501
				self.assertEqual(good_socket_comm.connect(good_ip, bad_port), -4)

	# port is available : 49152 - 65535
	def test_connect_port_allow(self):
		with patch('socket_comm.threading.Thread') as mock_thread_connect:
			with patch('socket_comm.socket') as mock_socket:
				good_socket_comm = socket_comm("127.0.0.1", 65500)
				good_ip   = "127.0.0.1"
				bad_port = 15
				self.assertEqual(good_socket_comm.connect(good_ip, bad_port), -5)

	# ---------------- #
	# FUNCTIONNAL TEST #
	# ---------------- #

	def test_socket_comm(self):
		# init the test server
		command = 'python3.8 script_test_server.py'
		args = shlex.split(command)
		p = subprocess.Popen(args)
		self.list_subprocess.append(p)

		#init the test client
		command = 'python3.8 script_test_client.py'
		args = shlex.split(command)
		p = subprocess.Popen(args)
		self.list_subprocess.append(p)

		time.sleep(5) # wait for the communication

		self.kill_subprocess()

	###################

	def kill_subprocess(self):
		while len(self.list_subprocess) != 0 :
			p = self.list_subprocess.pop()
			p.terminate()
			p.wait()

if __name__ == '__main__':
	unittest.main()
