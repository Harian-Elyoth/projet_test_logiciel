# test class for http server

import shutil
import shlex
import unittest
import subprocess
import time
import requests

from http_server import handler_http_serv, http_server

class test_http_server(unittest.TestCase):

	list_subprocess = []

	# --------------------- #
	# TEST __NEW__ FUNCTION #
	# --------------------- #

	# everything's fine
	def test_new(self):
		# THREAD OU MOCK

		command = 'python3.9 http_server.py'
		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(2) # wait for the server to be properly init

		self.kill_subprocess()

		# self.assertEqual(type(http_server("127.0.0.1", 65500)), http_server)

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
		self.assertEqual(http_server("127.0.0.1",    15), -5)
		self.assertEqual(http_server("127.0.0.1", 48800), -5)

	# -------------------- #
	# TEST DO_GET FUNCTION #
	# -------------------- #

	# do a GET on the server, everything's fine
	def test_get(self):
		command = 'python3.9 http_server.py'
		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		url 	= "http://127.0.0.1:60000"
		resp 	= requests.get(url)

		self.assertEqual((int)(resp.status_code), 200)

		self.kill_subprocess()

		# pass

	# do a GET on the server, endpoint not found
	def test_get_not_found(self):

		command = 'python3.9 http_server.py'
		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		url 	= "http://127.0.0.1:60000/room"
		resp 	= requests.get(url)

		self.assertEqual(resp.status_code, 404)

		self.kill_subprocess()

		# pass

	# --------------------- #
	# TEST DO_POST FUNCTION #
	# --------------------- #

	# do a POST on the server, everything's fine
	def test_post(self):
		
		command = 'python3.9 http_server.py'
		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init

		url 	= "http://127.0.0.1:60000"
		payload = "test"
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		resp 	= requests.post(url, data=payload, headers=headers)

		self.assertEqual((int)(resp.status_code), 200)

		self.kill_subprocess()
		# pass

	# do a POST on the server, endpoint not found
	def test_post_not_found(self):

		command = 'python3.9 http_server.py'
		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		self.list_subprocess.append(p)
		time.sleep(1) # wait for the server to be properly init
		
		url 	= "http://127.0.0.1:60000/room"
		payload = "test"
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

		resp 	= requests.post(url, data=payload, headers=headers)

		self.assertEqual((int)(resp.status_code), 404)

		self.kill_subprocess()
		# pass

	def kill_subprocess(self):
		while len(self.list_subprocess) != 0 :
			p = self.list_subprocess.pop()
			p.terminate()
			p.wait()

if __name__ == '__main__':

	unittest.main()