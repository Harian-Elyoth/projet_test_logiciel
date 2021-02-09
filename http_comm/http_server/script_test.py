# script for testing http_server

from http_server import http_server

if __name__ == '__main__':
	serv_test = http_server("127.0.0.1", 60000)
	serv_test.run()
