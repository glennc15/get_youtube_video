from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time  

from source.config_reader import ConfigReader 



# The PlaylistScraper class does not work in Colab for whatever reason.
# ChromeDriver always crashes without any real reason. However the scraper
# works find when ran in a method.


def get_videos(playlist_url, pause_time=10):

	options = Options()

	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	#overcome limited resource problems
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument("lang=en")
	#open Browser in maximized mode
	options.add_argument("start-maximized")
	#disable infobars
	options.add_argument("disable-infobars")
	#disable extension
	options.add_argument("--disable-extensions")
	options.add_argument("--incognito")
	options.add_argument("--disable-blink-features=AutomationControlled")

	driver = webdriver.Chrome(options=options)

	driver.get(playlist_url)
	time.sleep(pause_time)
	all_anchors = driver.find_elements(By.ID, 'video-title')
	videos = [x.get_property('href') for x in all_anchors if x.get_property('id') == 'video-title']

	print(driver.title)
	driver.quit()

	return videos 







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

		returns a random YouTube video url from a YouTube playlist channel.

		playlist_url: a url for a YouTube playlist channel

		'''
		
		browser = webdriver.Chrome()
		browser.get(playlist_url)

		# pausing to allow the browser data to fully load. The page seems to
		# load a little slower in Chrome/Selenium so adding a manual pause.
		# The pause can be adjusted in the config file 'pause' attribute:
		time.sleep(self.pause)

		# scrape the playlist vidoes. All playlist videos are in anchor tags
		# with an id = 'video-title'
		all_anchors = self.wait_for(fn=lambda: browser.find_elements_by_id('video-title'))
		self.videos = [x.get_property('href') for x in all_anchors if x.get_property('id') == 'video-title']

		browser.close()


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
				if time.time() - start_time > self.max_wait:
					raise e
				time.sleep(0.5)




	# End: Private methods
	# *************************************************************   