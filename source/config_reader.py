import os 
import json 


class ConfigReader(object):
	'''
	
	reads the config file (config.json) and stores all entries as properties.
	Alternatively, the user can supply a configuration dictionary.

	'''

	def __init__(self, config_data=None):
		self.read_config_file(config_data=None)



	@property 
	def email(self):
		return self._email 

	@email.setter
	def email(self, value):
		self._email = value  


	@property 
	def playlists(self):
		return self._playlists 

	@playlists.setter
	def playlists(self, value):
		self._playlists = value  


	@property 
	def pause(self):
		return self._pause 

	@pause.setter
	def pause(self, value):
		self._pause = value  


	@property 
	def max_wait(self):
		return self._max_wait 

	@max_wait.setter
	def max_wait(self, value):
		self._max_wait = value  


	@property 
	def email_sender(self):
		return self._email_sender 

	@email_sender.setter
	def email_sender(self, value):
		self._email_sender = value  


	@property 
	def email_body(self):
		return self._email_body 

	@email_body.setter
	def email_body(self, value):
		self._email_body = value  


	@property 
	def email_subject(self):
		return self._email_subject 

	@email_subject.setter
	def email_subject(self, value):
		self._email_subject = value  


	@property 
	def email_recipents(self):
		return self._email_recipents 

	@email_recipents.setter
	def email_recipents(self, value):
		self._email_recipents = value  


	@property 
	def email_server(self):
		return self._email_server 

	@email_server.setter
	def email_server(self, value):
		self._email_server = value 


	@property 
	def email_server_port(self):
		return self._email_server_port 

	@email_server_port.setter
	def email_server_port(self, value):
		self._email_server_port = value 


# *************************************************************
# Start: Private methods
	
	def read_config_file(self, config_data=None):
		'''
		
		Set properties using the config.json file or a user supplie
		configuration dictionary.

		'''

		if config_data is None:
			# open config.json and read it's contents 
			BASE_DIR = os.path.dirname(os.path.abspath(__file__))
			json_file = open(os.path.join(BASE_DIR, 'config.json'), 'r')
			config_data = json.loads(json_file.read())
			json_file.close()


		self.email = config_data['email']
		self.playlists = config_data['playlists']
		self.pause = config_data['pause']
		self.max_wait = config_data['max_wait']
		self.email_sender = config_data['email_sender']
		self.email_body = config_data['email_body']
		self.email_subject = config_data['email_subject']
		self.email_recipents = config_data['email_recipents']
		self.email_server = config_data['email_server']
		self.email_server_port = config_data['email_server_port']









# End: Private methods
# *************************************************************      



