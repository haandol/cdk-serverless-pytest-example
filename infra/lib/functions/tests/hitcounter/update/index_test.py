from ... import BaseTestCase
import services.hitcounter.update.index as index


class TestE2EUpdate(BaseTestCase):
    def test_handler(self):
        event = self.load_event('hitcounter-update.json')
        path = event['pathParameters']['proxy']
        assert 'test' == path
        assert index.handler(event, None) == {
            'path': path,
            'count': 1
        }