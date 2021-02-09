# test class for integration

import os, time

command = './dependencies.sh'
os.system(command)

import unittest
from http_client import http_client
import subprocess, shlex

class test_integration(unittest.TestCase):

	list_subprocess = []

	# ---------------------------- #
	# INTEGRATION TEST GET REQUEST #
	# ---------------------------- #

	def test_get_request(self):
		# init the test server
		command = 'python3 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 60000, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('GET', '/', good_header, ''), (0, b''))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:60000)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	# do a GET on the server, endpoint not found
	def test_get_not_found(self):
		# init the test server
		command = 'python3 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 60000, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('GET', '/room', good_header, ''), (-8, 'test : KO'))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:60000)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	# ----------------------------- #
	# INTEGRATION TEST POST REQUEST #
	# ----------------------------- #

	# everything's fine
	def test_post_request(self):
		# init the test server
		command = 'python3 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 60000, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('POST', '/', good_header, 'Hello Server !'), (0, b''))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:60000)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	# do a POST on the server, endpoint not found
	def test_post_not_found(self):
		# init the test server
		command = 'python3 script_test.py'

		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		# test the client class
		good_client_class = http_client("127.0.0.1", 65500, "127.0.0.1", 60000, 1)
		good_header = {"Content-type": "text/plain"}

		self.assertEqual(good_client_class.request('POST', '/room', good_header, 'Hello Server !'), (-8, "test : KO"))

		# kill the test server
		command = 'kill -9 $(lsof -t -i tcp:60000)'
		os.system(command)
		time.sleep(1) # wait for the server to be properly exit

		self.kill_subprocess()

	def kill_subprocess(self):
		while len(self.list_subprocess) != 0 :
			p = self.list_subprocess.pop()
			p.terminate()
			p.wait()

if __name__ == '__main__':
	unittest.main()
