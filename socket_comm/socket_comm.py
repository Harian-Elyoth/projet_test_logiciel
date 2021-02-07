import socket, threading

class socket_comm(object):
	def __new__(self, ip, port):
		return super(socket_comm, self).__new__(self)

	def __init__(self, ip, port):
		pass

	def __thread_listen(self, backlog_size):
		pass

	def __thread_connect(self, ip, port):
		pass

	def listen(self, backlog_size):
		pass

	def connect(self, ip, port):
		pass

	def send_message(self, message):
		pass

	def __del__(self):
		pass
