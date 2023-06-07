import unittest

from source.email_distributor import EmailDistributor



class EmailDistributorTest(unittest.TestCase):

	def test_send_emails(self):
		email_distributor = EmailDistributor()
		email_distributor.send_emails(
			email_password="epnimreasdtblmzb", 
			video_url='https://www.youtube.com/watch?v=mYF2_FBCvXw&list=PLZ1XR9BfLduNt5QokVd3jBqoc4hKCU48u&index=3&t=4s'
		)



if __name__ == '__main__':
    unittest.main()