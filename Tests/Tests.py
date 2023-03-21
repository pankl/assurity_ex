import unittest
import requests
import http
import json
from Helpers.Constants import *
from Helpers.mylogger import getmylogger

logger = getmylogger(__name__)


class TestAssurityApi(unittest.TestCase):
        @classmethod
        def setUpClass(self):
            logger.debug("Starting set up for the tests")
            logger.debug("Running setUp method")
            self.res = requests.get(baseUri)
            if (self.res.status_code != http.HTTPStatus.OK):
                  logger.error(f'The request to api failed, with error code {self.res.status_code} and body {self.res.content}')
                  self.fail(self,f'The request to api failed, with error code {self.res.status_code} and body {self.res.content}')
            try:
                self.parsed_content = json.loads(self.res.content)
            except:
                logger.error('Couldn\'t parse response into json')
                self.fail(self,'Couldn\'t parse response into json')

        def test_Name_correct(self):
            self.assertEqual('Carbon credits', self.parsed_content['Name'])

        def test_CanRelist(self):
            self.assertTrue(self.parsed_content['CanRelist'])
        
        def test_Promotions(self):
            self.promo = next((item for item in self.parsed_content['Promotions'] if item['Name'] == PromotionName), None)
            if (self.promo == None):
                logger.error(f'Could not find a promotion with the name {PromotionName}')
                self.fail(f'Could not find a promotion with the name {PromotionName}')
            self.assertIn(DescriptionSubString, self.promo['Description'])


if __name__ == '__main__':
    unittest.main()
