import unittest

from source.config_reader import ConfigReader
from source.playlist_selector import PlaylistSelector



class PlaylistSelectorTest(unittest.TestCase):

	def setUp(self):
		# the playlist urls are in a dict object where the keys are categories
		# and the values are list of playlist urls. This converts the
		# dictionary object to a flat list:
		all_playlists = [v for k, v in ConfigReader().playlists.items()]
		self.all_playlists_urls = [url for playlist in all_playlists for url in playlist]


	def test_returns_random_playlist_url(self):
		playlist_selector = PlaylistSelector()
		self.assertIn(playlist_selector.get_randomplaylist(), self.all_playlists_urls)




if __name__ == '__main__':
    unittest.main()