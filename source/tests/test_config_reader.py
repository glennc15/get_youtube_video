import unittest
import os 
import json

from source.config_reader import ConfigReader



class ConfigReaderTest(unittest.TestCase):
	def setUp(self):

		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		json_file = open(os.path.join(BASE_DIR, 'config.json'), 'r')
		self.config = json.loads(json_file.read())

		json_file.close()


	def test_email_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email, self.config['email'])


	def test_playlists_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.playlists, self.config['playlists'])


	def test_max_wait_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.max_wait, self.config['max_wait'])


	def test_pause_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.pause, self.config['pause'])


	def test_email_sender_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_sender, self.config['email_sender'])


	def test_email_recipents_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_recipents, self.config['email_recipents'])


	def test_email_server_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_server, self.config['email_server'])


	def test_email_server_port_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_server_port, self.config['email_server_port'])


	def test_email_subject_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_subject, self.config['email_subject'])


	def test_email_body_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_body, self.config['email_body'])




	# def test_email_attribute(self):
	# 	config = ConfigReader()
	# 	self.assertEqual(config.email = json_file['email'])




if __name__ == '__main__':
    unittest.main()