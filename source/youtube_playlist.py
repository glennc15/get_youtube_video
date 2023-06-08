import random

from source.playlist_selector import PlaylistSelector
from source.playlist_scraper import get_videos
from source.email_distributor import EmailDistributor 


class YouTubePlaylist(object):
	'''
	
	Controller class:

	This class randomly selects a YouTube playlist url from the configuration
	file (config.json). Then a Chrome browser is opened with the playlist
	url. A video url is randomly selected from the playlist and emailed to
	every email recipient specified in the config file (config.json)


	'''	
	def __init__(self, email_password, config_data=None):
		self.run_controller(
			email_password=email_password,
			config_data=config_data
		)



	# *************************************************************
	# Start: Public methods
	
	def run_controller(self, email_password, config_data):
		'''

		main controller method for the class

		'''

		# Selecting a random playlist:
		playlist_url = PlaylistSelector(config_data=config_data).get_random_playlist()
		print("Selected the following playlist:\n{}\n".format(playlist_url))

		# playlist_scraper = PlaylistScraper()
		print("Getting video urls from YouTube (this will take a few seconds...)")
		videos = get_videos(playlist_url=playlist_url)

		# main a random video to each email recipient:
		if len(videos) > 0:
			video_url = random.choice(videos)

			print("Sending the following video URL to each email recipient\n{}\n".format(video_url))
			
			email_distributor = EmailDistributor()
			email_distributor.send_emails(
				email_password=email_password,
				video_url=video_url
			)


		else:
			raise ValueError("Cound not find any videos for playlist url: {}".format(playlist_url))





	# End: Public methods
	# *************************************************************   



