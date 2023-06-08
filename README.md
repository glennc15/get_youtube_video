'''


I have 4 youtube playlists. I would like python code that I can paste in
collab. I'd like the code to run each day at 6 am. At 6 am it will randomly
choose one of the playlists, open the playlist and randomly choose a video in
that play list. It will copy the link to that randomly selected video and
send a text (or email to a phone number) with that link. I'd like to have the
option to override and execute the code on demand or allow the schedule to
run each day at 6am. Either / Or option. Is this something you can handle?
please explain your approach.



'''



classes: 

YouTubePlaylist: 
	controller.
	1. Gets a random playlist URL.
	2. Get a video URL from YouTube scraper.
	3. Send video URL via email to email list


PlaylistSelector:
	1. Gets all playlist channels (URLs) from config.json and selection 1 channel at random.


YouTubePlaylistScraper:
	1. Takes a YouTube playlist channel URL.
	2. Scrapes the URL for all available videos. Uses Selenium for scraping.

EmailDistribution:
	1. Takes a video URL
	2. Send an email to the distribution list in config.json

ConfigReader:
	helper method for loading config.json


