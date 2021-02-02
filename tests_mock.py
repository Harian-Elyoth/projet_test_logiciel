#Fichier my_module.py:

def simple_get_req( ip_port, endpoint):
	""" This function send a get request and check if status code is 200 it returns {} if not """
	try:
		r = requests.get('http://' + ip_port + '/' + endpoint,timeout = 1)
		if r.status_code == 200:
			req_json = r.json()
			return req_json # returns json answer
		else :
			logging.error('could not reach %s endpoint %s', ip_port, endpoint)

	except requests.exceptions.RequestException as e:
		logging.error(str(e))

	return {}


# tests associ�s:

import my_module.py

class mock_req():

	def __init__(self, status_code, json):
		self.status_code = status_code
		self.jso = json

	def json(self):
		return self.jso

class Tests_SimpleGetReq(unittest.TestCase):

	def test_simple_get_req_OK(self):
		ip_port = '0.0.0.1:1'
		endpoint = 'endpoint'

		with patch('my_module.requests') as mock_requests:
			mock_requests.get = MagicMock(return_value=mock_req(200,{'whatever_key':'value'}))

			self.assertEqual(simple_get_req(ip_port,endpoint), {'whatever_key':'value'})


	def test_simple_get_req_KO(self):
		ip_port = '0.0.0.1:1'
		endpoint = 'endpoint'

		with patch('my_module.requests') as mock_requests:
			mock_requests.get = MagicMock(return_value=mock_req(500, {'whatever_key':'value'}))

			self.assertEqual(simple_get_req(ip_port,endpoint), {})
