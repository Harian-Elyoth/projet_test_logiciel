import socket, time, os, threading

class socket_comm(object):
	def __new__(self):
		return super(socket_comm, self).__new__(self)

	def __init__(self):

		self.sockets_recv  = []
		self.sockets_send = []

		self.send_msgs    = []
		self.send_mutexs  = []

		self.client_address = []
		self.nb_clients   = -1

		self.stop_threads = False

	def __thread_listen(self, socket_recv):

		try:
			clientsocket, address = socket_recv.accept()
			self.client_address.append(address)

			while True:
				if self.stop_threads == True:
					raise ValueError

				message = clientsocket.recv(1028)
				receive_msg = message.decode("utf-8")

				if len(receive_msg) != 0 :
					print(receive_msg)
					self.send_broadcast(receive_msg, address)

		except ValueError:
			clientsocket.close()

	def __thread_connect(self):
		thread_nb_clients = self.nb_clients

		try:
			while True:
				if self.stop_threads == True:
					raise ValueError

				if len(self.send_msgs[thread_nb_clients]) != 0 :
					self.send_mutexs[thread_nb_clients].acquire()

					self.sockets_send[thread_nb_clients].sendall(bytes(self.send_msgs[thread_nb_clients],"utf-8"))
					self.send_msgs[thread_nb_clients] = ''

					self.send_mutexs[thread_nb_clients].release()
		except ValueError:
			pass

	def listen(self, ip, port, backlog_size):
		# test ip type
		if type(ip) != str:
			return -1

		# test ip format
		ip_bytes = []
		ip_bytes = ip.split(".")

		if len(ip_bytes) == 4:
			for ip_byte in ip_bytes:
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

		# test backlog_size type
		if type(backlog_size) != int:
			return -6

		try:
			self.sockets_recv.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
			self.sockets_recv[-1].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

			self.sockets_recv[-1].bind((ip, port))
			self.sockets_recv[-1].listen(backlog_size)
		except socket.error:
			return -5

		threading.Thread(target=self.__thread_listen, args=(self.sockets_recv[-1],)).start()
		return 0

	def connect(self, ip, port):

		# test ip type
		if type(ip) != str:
			return -1

		# test ip format
		ip_bytes = []
		ip_bytes = ip.split(".")

		if len(ip_bytes) == 4:
			for ip_byte in ip_bytes:
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
			self.nb_clients += 1

			self.sockets_send.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
			self.sockets_send[-1].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.sockets_send[-1].connect((ip, port))

			self.send_msgs.append('')
			self.send_mutexs.append(threading.Lock())

		except ConnectionRefusedError:
			return -6

		threading.Thread(target=self.__thread_connect).start()
		return 0

	def send_message(self, message):
		for i in range(len(self.send_msgs)):
			self.send_mutexs[i].acquire()
			self.send_msgs[i] = message
			self.send_mutexs[i].release()

	def send_broadcast(self, message, addr):
		for i in range(len(self.client_address)):
			if addr != self.client_address[i]:
				self.send_msgs[i] = message

	def __del__(self):
		for socket_recv in self.sockets_recv:
			socket_recv.close()
		for socket_send in self.sockets_send:
			socket_send.close()
