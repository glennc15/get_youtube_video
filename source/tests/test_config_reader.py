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


	def test_email_login_attribute(self):
		config = ConfigReader()
		self.assertEqual(config.email_login, self.config['email_login'])


	def test_email_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email, self.config['email'])


	def test_playlists_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.playlists, self.config['playlists'])


	def test_max_wait_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.max_wait, self.config['max_wait'])


	def test_pause_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.pause, self.config['pause'])


	def test_email_sender_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_sender, self.config['email_sender'])


	def test_email_recipents_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_recipents, self.config['email_recipents'])


	def test_email_server_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_server, self.config['email_server'])


	def test_email_server_port_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_server_port, self.config['email_server_port'])


	def test_email_subject_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_subject, self.config['email_subject'])


	def test_email_body_attribute_with_user_supplies_config_data(self):
		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_body, self.config['email_body'])


	def test_email_login_attribute_with_user_supplies_config_data(self):

		email_login = 'login_email_address@gmail.com'

		self.config['email_login'] = email_login

		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_login, email_login)


	def test_email_login_attribute_missing_with_user_supplies_config_data(self):
		'''
		
		if the 'email_login' attribute is missing in the configuration
		dictionary then 'email_sender' is used for 'email_login'

		'''

		del self.config['email_login']

		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_login, self.config['email_sender'])


	def test_email_login_attribute_is_None(self):
		'''
		
		if the 'email_login' attribute is None in the configuration
		dictionary then 'email_sender' is used for 'email_login'

		'''
		
		self.config['email_login'] = None 

		config = ConfigReader(config_data=self.config)
		self.assertEqual(config.email_login, self.config['email_sender'])








if __name__ == '__main__':
    unittest.main()