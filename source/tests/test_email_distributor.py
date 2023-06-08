import unittest
import os 
import json 

from source.email_distributor import EmailDistributor


class EmailDistributorTest(unittest.TestCase):

	def setUp(self):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		json_file = open(os.path.join(BASE_DIR, 'config.json'), 'r')
		self.config = json.loads(json_file.read())

		json_file.close()


	def test_send_emails(self):
		email_distributor = EmailDistributor()
		email_distributor.send_emails(
			email_password='123',
			video_url='https://www.youtube.com/watch?v=mYF2_FBCvXw&list=PLZ1XR9BfLduNt5QokVd3jBqoc4hKCU48u&index=3&t=4s'
		)



	def test_send_emails_with_user_config_data(self):
		email_distributor = EmailDistributor(config_data=self.config)
		email_distributor.send_emails(
			email_password='123',
			video_url='https://www.youtube.com/watch?v=mYF2_FBCvXw&list=PLZ1XR9BfLduNt5QokVd3jBqoc4hKCU48u&index=3&t=4s'
		)




if __name__ == '__main__':
    unittest.main()