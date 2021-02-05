# class for test handler

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# Class for testing http_client
class test_handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'test : KO')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()

        response = BytesIO()
        response.write(body)
        self.wfile.write(response.getvalue())

if __name__ == '__main__':
	httpd = HTTPServer(("127.0.0.1", 65501), test_handler)
	httpd.serve_forever()
