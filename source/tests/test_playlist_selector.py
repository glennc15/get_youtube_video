import unittest
import os 
import json 

from source.config_reader import ConfigReader
from source.playlist_selector import PlaylistSelector



class PlaylistSelectorTest(unittest.TestCase):

	def setUp(self):
		# the playlist urls are in a dict object where the keys are categories
		# and the values are list of playlist urls. This converts the
		# dictionary object to a flat list:
		all_playlists = [v for k, v in ConfigReader().playlists.items()]
		self.all_playlists_urls = [url for playlist in all_playlists for url in playlist]

		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		json_file = open(os.path.join(BASE_DIR, 'config.json'), 'r')
		self.config = json.loads(json_file.read())

		json_file.close()


	def test_returns_random_playlist_url(self):
		playlist_selector = PlaylistSelector()
		self.assertIn(playlist_selector.get_random_playlist(), self.all_playlists_urls)


	def test_returns_random_playlist_url_with_user_config(self):
		playlist_selector = PlaylistSelector(config_data=self.config)
		self.assertIn(playlist_selector.get_random_playlist(), self.all_playlists_urls)




if __name__ == '__main__':
    unittest.main()