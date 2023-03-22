from http import HTTPStatus
import unittest

from Helpers.Constants import *
from Helpers.MyLogger import getmylogger
from Helpers.Requests import myRequests

logger = getmylogger(__name__)


class TestAssurityApi(unittest.TestCase):
        @classmethod
        def setUpClass(self):
            logger.debug("Starting set up for the tests")
            logger.debug("Running setUp method")
            self.response = myRequests.getRequest(baseUri)
            if (self.response.status_code != HTTPStatus.OK):
                  logger.error(f'The request to api failed, with error code {self.response.status_code} and body {self.response.content}')
                  self.fail(self,f'The request to api failed, with error code {self.response.status_code} and body {self.response.content}')
            try:
                self.parsed_content = self.response.json()
            except:
                logger.error('Couldn\'t parse response into json')
                self.fail(self,'Couldn\'t parse response into json')

        def test_category_details(self):
        
            self.promo = next((item for item in self.parsed_content['Promotions'] if item['Name'] == PromotionName), None)
            if (self.promo == None):
                logger.error(f'Could not find a promotion with the name {PromotionName}')
                self.fail(f'Could not find a promotion with the name {PromotionName}')
            
            self.assertEqual('Carbon credits', self.parsed_content['Name'])
            self.assertTrue(self.parsed_content['CanRelist'])
            self.assertIn(DescriptionSubString, self.promo['Description'])


if __name__ == '__main__':
    unittest.main()
