import json
from ... import BaseTestCase
from services.hitcounter.update import index


class TestE2EUpdate(BaseTestCase):
    def test_handler(self):
        event = self.load_event('hitcounter-update.json')

        path = event['pathParameters']['proxy']
        self.assertEqual('test', path)

        resp = index.handler(event, None)
        self.assertEqual(resp['statusCode'], 200)

        body = json.loads(resp['body'])
        self.assertEqual(body['path'], path)
        self.assertEqual(body['count'], 1)

    def test_with_empty_path(self):
        event = self.load_event('hitcounter-get.json')
        event['pathParameters']['proxy'] = ''

        resp = index.handler(event, None)
        self.assertEqual(resp['statusCode'], 400)