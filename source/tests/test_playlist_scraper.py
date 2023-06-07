import unittest

from source.config_reader import ConfigReader
from source.playlist_scraper import PlaylistScraper



class PlaylistScraperTest(unittest.TestCase):
	'''
	
	There is not a great way to test this as the scraped data is dynamic.
	These tests provide basic "smoke test" in that the class doesent' blow
	up when initialized and can scrape video urls.

	'''	

	def setUp(self):
		# the playlist urls are in a dict object where the keys are categories
		# and the values are list of playlist urls. This converts the
		# dictionary object to a flat list:
		all_playlists = [v for k, v in ConfigReader().playlists.items()]
		self.all_playlists_urls = [url for playlist in all_playlists for url in playlist]



	def test_initialization(self):
		playlist_scraper = PlaylistScraper()
		self.assertIsNone(playlist_scraper.videos)


	def test_get_videos_test1(self):
		playlist_scraper = PlaylistScraper()
		playlist_scraper.get_videos(playlist_url=self.all_playlists_urls[0])
		self.assertTrue(len(playlist_scraper.videos) > 0)


	def test_get_videos_test2(self):
		playlist_scraper = PlaylistScraper()
		playlist_scraper.get_videos(playlist_url=self.all_playlists_urls[-1])
		self.assertTrue(len(playlist_scraper.videos) > 0)





if __name__ == '__main__':
    unittest.main()