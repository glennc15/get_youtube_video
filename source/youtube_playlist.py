import random

from source.playlist_selector import PlaylistSelector
from source.playlist_scraper import PlaylistScraper
from source.email_distributor import EmailDistributor 


class YouTubePlaylist(object):
	'''
	
	Controller class:

	This class randomly selects a YouTube playlist url from the configuration
	file (config.json). Then a Chrome browser is opened with the playlist
	url. A video url is randomly selected from the playlist and emailed to
	every email recipient specified in the config file (config.json)


	'''	
	def __init__(self):

		self.run_controller()



	# *************************************************************
	# Start: Public methods
	
	def run_controller(self):
		'''

		main controller method for the class

		'''
		playlist_url = PlaylistSelector().get_random_playlist()

		playlist_scraper = PlaylistScraper()
		playlist_scraper.get_videos(playlist_url=playlist_url)

		if len(playlist_scraper.videos) > 0:
			video_url = random.choice(playlist_scraper.videos)

			email_distributor = EmailDistributor()
			email_distributor.send_emails(
				email_password='epnimreasdtblmzb',
				video_url=video_url
			)


		else:
			raise ValueError("Cound not find any videos for playlist url: {}".format(playlist_url))





	# End: Public methods
	# *************************************************************   



