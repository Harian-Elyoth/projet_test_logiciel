'''
Application to demonstrate testing tornado websockets
'''

from tornado import web, websocket

# We don't override `data_received`
# pylint: disable=W0223
class Echo(websocket.WebSocketHandler):

    # Open allows for any number arguments, unlike what pylint thinks.
    # pylint: disable=W0221
    def open(self):
        self.write_message('hello')

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        self.write_message('bye')


APP = web.Application([
    (r"/", Echo),
])

if __name__ == "__main__":
    APP.listen(5000)