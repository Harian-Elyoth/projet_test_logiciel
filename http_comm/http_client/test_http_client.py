# test class for http client

import unittest
from http_client import http_client
from mock import patch
import os
import subprocess
import shlex
import time

class test_http_client(unittest.TestCase):

	list_subprocess = []

	# --------------------- #
	# TEST __NEW__ FUNCTION #
	# --------------------- #

	# everything's fine
	def test_new(self):
		self.assertEqual(type(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)), http_client)

	# ip_server is a string
	def test_ip_server_type(self):
		self.assertEqual(http_client("127.0.0.1", 65500, 192.168, 65501, 1), -1)

	# ip_server is something like 192.168.41.2
	def test_ip_server_format(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "1923.17.435.6524", 65501, 1), -2)

	# port_server is an integer
	def test_port_server_type(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", "65501", 1), -3)

	# port_server is between 0 and 65535
	def test_port_server_format(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", -65501, 1), -4)
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 66000, 1) , -4)

	# port_server is available : 49152 - 65535
	def test_port_server_allow(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 15, 1), -5)

	# timeout is an integer
	def test_timeout_type(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, "1"), -6)

	# timeout is between 10 and 60
	def test_timeout_format(self):
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 0) , -7)
		self.assertEqual(http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 70), -7)

	# ip is a string
	def test_ip_client_type(self):
		self.assertEqual(http_client(192.168, 65500, "127.0.0.1", 65501, 1), -8)

	# ip is something like 192.168.41.2
	def test_ip_client_format(self):
		self.assertEqual(http_client("1923.17.435.6524", 65500, "127.0.0.1", 65501, 1), -9)

	# port is an integer
	def test_port_client_type(self):
		self.assertEqual(http_client("127.0.0.1", "65501", "192.168.47.1", 65500, 1), -10)

	# port is between 0 and 65535
	def test_port_client_format(self):
		self.assertEqual(http_client("127.0.0.1", -65501, "192.168.47.1", 65500, 1), -11)
		self.assertEqual(http_client("127.0.0.1", 66000, "192.168.47.1", 65500, 1) , -11)

	# port is available : 49152 - 65535
	def test_port_client_allow(self):
		self.assertEqual(http_client("127.0.0.1", 15, "192.168.47.1", 65500, 1), -12)

	# --------------------- #
	# TEST REQUEST FUNCTION #
	# --------------------- #

	# everything's fine
	def test_request_get(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		with patch('http_client.http.client.HTTPConnection.request') as mock_request:
			with patch('http_client.http.client.HTTPConnection.getresponse') as mock_getresponse:
				mock_getresponse.return_value.status = 200
				mock_getresponse.return_value.read.return_value = "test : OK"

				self.assertEqual(good_client_class.request('GET', '/', good_header, ''), (0, "test : OK"))

	# everything's fine
	def test_request_post(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		with patch('http_client.http.client.HTTPConnection.request') as mock_request:
			with patch('http_client.http.client.HTTPConnection.getresponse') as mock_getresponse:
				mock_getresponse.return_value.status = 200
				mock_getresponse.return_value.read.return_value = "test : OK"

				self.assertEqual(good_client_class.request('POST', '/', good_header, 'Hello Server !'), (0, "test : OK"))

	# connection failed
	def test_server_unreachable(self):
		bad_client_class = http_client("127.0.0.1", 65500, "192.168.47.0", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		with patch('http_client.http.client.HTTPConnection.request') as mock_request:
			with patch('http_client.http.client.HTTPConnection.getresponse') as mock_getresponse:
				mock_getresponse.return_value.status = 404
				mock_getresponse.return_value.read.return_value = "test : KO"

				self.assertEqual(bad_client_class.request('GET', '/room', good_header, ''), (-8, "test : KO"))

	# method is a string
	def test_method_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		self.assertEqual(good_client_class.request(0, '/', good_header, ''), (-2, ""))

	# method is GET or POST
	def test_method_format(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		self.assertEqual(good_client_class.request('GETE', '/', good_header, ''), (-3, ""))

	# endpoint is a string
	def test_endpoint_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		self.assertEqual(good_client_class.request('GET', 0, good_header, ''), (-4, ""))

	# endpoint is something like /toto/titit
	def test_endpoint_format(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		self.assertEqual(good_client_class.request('GET', 'bad_endpoint', good_header, ''), (-5, ""))

	# body is a string
	def test_body_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 10)
		good_header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		self.assertEqual(good_client_class.request('GET', '/', good_header, 0), (-6, ""))

	# header is a dict
	def test_header_type(self):
		good_client_class = http_client("127.0.0.1", 65500, "192.168.47.1", 65501, 1)

		self.assertEqual(good_client_class.request('GET', '/', 0, ''), (-7, ""))

	# --------------------------------- #
	# TEST FUNCTIONNAL REQUEST FUNCTION #
	# --------------------------------- #

	# everything's fine
	def test_functional_request_get(self):
		# init the test server
		command = 'python3.8 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 65501, 1)
		self.assertEqual(good_client_class.request('GET', '/', {}, ''), (0, b'test : OK'))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:65501)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	# do a GET on the server, endpoint not found
	def test_functionnal_get_not_found(self):
		# init the test server
		command = 'python3.8 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 65501, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('GET', '/room', good_header, ''), (-8, "test : KO"))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:65501)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	# everything's fine
	def test_functional_request_post(self):
		# init the test server
		command = 'python3.8 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 65501, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('POST', '/', good_header, 'Hello Server !'), (0, b'Hello Server !'))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:65501)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	# everything's fine
	def test_functionnal_post_not_found(self):
		# init the test server
		command = 'python3.8 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 65501, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('POST', '/room', good_header, 'Hello Server !'), (-8, "test : KO"))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:65501)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()
	###################

	def kill_subprocess(self):
		while len(self.list_subprocess) != 0 :
			p = self.list_subprocess.pop()
			p.terminate()
			p.wait()


if __name__ == '__main__':
	unittest.main()
