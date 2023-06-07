from selenium import webdriver 
from selenium.common.exceptions import WebDriverException
import time  

from source.config_reader import ConfigReader 



class PlaylistScraper(ConfigReader):
	'''
	
	scrapes a YouTube playlist page. Builds a list of all video urls found on
	the page.


	'''
	def __init__(self):
		super().__init__()
		
		self.videos = None 


	@property
	def videos(self):
		return self._videos

	@videos.setter
	def videos(self, value):
		self._videos = value


	# *************************************************************
	# Start: Public methods
	
	def get_videos(self, playlist_url):
		'''

		returns a random playlist url.

		'''
		
		pass 


	# End: Public methods
	# *************************************************************   



	# *************************************************************
	# Start: Private methods
	
	def wait_for(self, fn):
		start_time = time.time()
		while True:
			try:
				return fn()

			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)




	# End: Private methods
	# *************************************************************   