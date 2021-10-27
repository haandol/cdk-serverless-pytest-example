import json
from ... import BaseTestCase
from hitcounter.get import index


class TestE2EGet(BaseTestCase):
    def beforeEach(self):
        self.load_fixture('hitcounter-get.json')

    def test_handler(self):
        event = self.load_event('hitcounter-get.json')
        self.assertEqual('test', event['pathParameters']['proxy'])

        resp = index.handler(event, None)
        self.assertEqual(resp['statusCode'], 200)

        body = json.loads(resp['body'])
        self.assertEqual(body['count'], 2)

    def test_with_empty_path(self):
        event = self.load_event('hitcounter-get.json')
        event['pathParameters']['proxy'] = ''

        resp = index.handler(event, None)
        self.assertEqual(resp['statusCode'], 400)