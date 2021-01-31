# class for http client

import http.client
import urllib.request
import socket

class http_client(object):
	
	"""docstring for http_client"""

	# called when creating instance, return an object (can be an integer)
	def __new__(self, ip, port, ip_server, port_server, timeout):

		# TESTS on parameters

		# test ip_server type
		if type(ip_server) != str:
			return -1

		# test ip_server format
		ip_server_bytes = []
		ip_server_bytes = ip_server.split(".")

		if len(ip_server_bytes) == 4:
			for ip_server_byte in ip_server_bytes:
				int_ip_server_byte = int(ip_server_byte)
				
				if int_ip_server_byte < 0 or int_ip_server_byte > 255:
					return -2
		else:
			return -2

		# test port_server type
		if type(port_server) != int:
			return -3

		# test port_server format
		if port_server > 0 and port_server < 65535:
			if port_server < 49152:
				return -5
		else:
			return -4

		# test timeout type
		if type(timeout) != int:
			return -6

		# test timeout format
		if timeout < 10 or timeout > 60:
			return -7

		# test ip type
		if type(ip) != str:
			return -8

		# test ip format
		ip_bytes = []
		ip_bytes = ip.split(".")

		if len(ip_bytes) == 4:
			for ip_byte in ip_bytes:
				int_ip_byte = int(ip_byte)
				
				if int_ip_byte < 0 or int_ip_byte > 255:
					return -9
		else:
			return -9

		# test port type
		if type(port) != int:
			return -10

		# test port format
		if port > 0 and port < 65535:
			if port < 49152:
				return -12
		else:
			return -11

		return super(http_client, self).__new__(self)

	# called for initialize object (after new), return None
	def __init__(self, ip, port, ip_server, port_server, timeout):

		self.ip 			= ip
		self.port 			= port
		self.ip_server 		= ip_server
		self.port_server 	= port_server
		self.timeout		= timeout

		self.http_conn		= http.client.HTTPConnection

	"""establish a connection with the server"""
	def connect(self):
		pass

	""" make http requests (GET, POST)"""
	def request(self, method, endpoint, body, header):
		pass

	# called when there not references anymore
	def __del__(self):
		print('exit')
		# free ports