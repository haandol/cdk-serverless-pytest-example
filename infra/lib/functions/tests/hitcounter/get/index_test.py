from ... import BaseTestCase
from services.hitcounter.get import index


class TestE2EGet(BaseTestCase):
    def test_handler(self):
        event = self.load_event('hitcounter-get.json')
        path = event['pathParameters']['proxy']
        assert 'test' == path
        assert index.handler(event, None) == {
            'path': path,
            'count': 0,
        }