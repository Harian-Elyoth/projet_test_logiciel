import socket, time, os, threading

class socket_comm(object):
	def __new__(self, ip, port):

		# test ip type
		if type(ip) != str:
			return -1

		# test ip format
		ip_bytes = []
		ip_bytes = ip.split(".")

		if len(ip_bytes) == 4:
			for ip_bytes in ip_bytes:
				int_ip_byte = int(ip_byte)

				if int_ip_byte < 0 or int_ip_byte > 255:
					return -2
		else:
			return -2

		# test port type
		if type(port) != int:
			return -3

		# test port format
		if port > 0 and port < 65535:
			if port < 49152:
				return -5
		else:
			return -4

		return super(socket_comm, self).__new__(self)

	def __init__(self, ip, port):
		self.ip   = ip
		self.port = port

		self.socket_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket_send.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		self.receive_msg = ''

		self.send_msg = ''
		self.send_sem = threading.Lock()

		self.stop_threads = False

	def __thread_listen(self):
		clientsocket, address = self.socket_recv.accept()

		try:
			while True:
				if self.stop_threads == True:
					raise ValueError

				message = clientsocket.recv(1028)
				self.receive_msg = message.decode("utf-8")

				if len(self.receive_msg) != 0 :
					print("receive_msg = " + self.receive_msg)

		except ValueError:
			clientsocket.close()

	def __thread_connect(self):
		clientsocket, address = self.socket_send.accept()

		try:
			while True:
				if self.stop_threads == True:
					raise ValueError

				if len(self.send_msg) != 0 :
					self.send_sem.acquire()

					self.socket_send.sendall(bytes(self.send_msg,"utf-8"))
					self.send_msg = ''

					self.send_sem.release()

		except ValueError:
			pass

	def listen(self, backlog_size):
		# test backlog_size type
		if type(backlog_size) != int:
			return -1

		try:
			self.socket_recv.bind((self.ip, self.port))
			self.socket_recv.listen(backlog_size)
		except socket.error:
			return -2

		threading.Thread(target=self.__thread_listen).start()
		return 0

	def connect(self, ip, port):

		# test ip type
		if type(ip) != str:
			return -1

		# test ip format
		ip_bytes = []
		ip_bytes = ip.split(".")

		if len(ip_bytes) == 4:
			for ip_bytes in ip_bytes:
				int_ip_byte = int(ip_byte)

				if int_ip_byte < 0 or int_ip_byte > 255:
					return -2
		else:
			return -2

		# test port type
		if type(port) != int:
			return -3

		# test port format
		if port > 0 and port < 65535:
			if port < 49152:
				return -5
		else:
			return -4

		try:
			self.socket_send.connect((ip, port))
		except ConnectionRefusedError:
			return -6

		threading.Thread(target=self.__thread_connect).start()
		return 0

	def send_message(self, message):
		self.send_sem.acquire()
		self.send_msg = message
		self.send_sem.release()

	def __del__(self):
		pass
