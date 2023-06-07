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


	# def test_email_attribute(self):
	# 	config = ConfigReader()
	# 	self.assertEqual(config.email = json_file['email'])




if __name__ == '__main__':
    unittest.main()