import os 
import json 


class ConfigReader(object):
	'''
	
	reads the config file (config.json) and stores all entries as properties.

	'''

	def __init__(self):
		self.read_config_file()



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



# *************************************************************
# Start: Private methods
	
	def read_config_file(self):

		# open config.json and read it's contents 
		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		json_file = open(os.path.join(BASE_DIR, 'config.json'), 'r')
		config_json = json.loads(json_file.read())

		self.email = config_json['email']
		self.playlists = config_json['playlists']
		self.pause = config_json['pause']
		self.max_wait = config_json['max_wait']

		json_file.close()



# End: Private methods
# *************************************************************      



