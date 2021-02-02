import shutil
import shlex
import subprocess
import requests
import time



class TestsIntegration(unittest.TestCase):

	list_subprocess = []

	def kill_subprocess(self):
		while len(self.list_subprocess) != 0 :
			p = self.list_subprocess.pop()
			p.terminate()

	def tearDown(self):
		self.kill_subprocess()

	def test_launch_server(self):

		command = 'python3 launch_server -c config.file'
		args = shlex.split(command)

		p = subprocess.Popen(args) # lauch command as a subprocess

		list_subprocess.append(p)
		time.sleep(8) # wait for the server to be properly init

		r = requests.get('http://127.0.0.1:12345' + '/rooms',timeout=1)
		self.assertEqual(r.status_code,200)

		req_dict = r.json() # let's get the json payload as a python dict

		self.assertIn('nb_rooms', req_dict) # let's check that we got whatever key we expect in the dict
		self.assertEqual(req_dict['nb_rooms'],3) # let's check that we got whatever value we expect in the associated key

		self.kill_subprocess()
