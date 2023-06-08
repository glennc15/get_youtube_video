import unittest
import os 
import json


from source.youtube_playlist import YouTubePlaylist



class YouTubePlaylistTest(unittest.TestCase):

	def setUp(self):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		json_file = open(os.path.join(BASE_DIR, 'config.json'), 'r')
		self.config = json.loads(json_file.read())

		json_file.close()

	def test_with_config_file(self):
		YouTubePlaylist(email_password='123')


	def test_with_user_config_data(self):
		YouTubePlaylist(
			email_password='123',
			config_data=self.config
		)


if __name__ == '__main__':
    unittest.main()