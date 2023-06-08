import random

from source.config_reader import ConfigReader 


class PlaylistSelector(ConfigReader):
	'''
	
	Returns a random playlist url from the config file (config.json)

	'''

	def __init__(self, config_data=None):
		super().__init__(config_data=config_data)



	# *************************************************************
	# Start: Public methods
	
	def get_random_playlist(self):
		'''

		returns a random playlist url.

		'''

		# The playlist in the config file are in a dictionary sorted by
		# category. This converts the dictionary to a flat list:
		all_playlists = [v for k, v in ConfigReader().playlists.items()]
		all_playlists_urls = [url for playlist in all_playlists for url in playlist]

		random_url = random.choice(all_playlists_urls)


		return random_url



	# End: Public methods
	# *************************************************************      
