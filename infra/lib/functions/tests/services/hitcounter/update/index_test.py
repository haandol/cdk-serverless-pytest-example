from .... import BaseTestCase
import services.hitcounter.update.index as index


class TestHitCounterUpdate(BaseTestCase):
    def test_success_update(self):
        path = 'dongkyl'
        for c in range(1, 5):
            assert c == index.update(self.table, path)


class TestE2E(BaseTestCase):
    def test_handler(self):
        event = self.load_event('hitcounter-update.json')
        path = event['pathParameters']['proxy']
        assert {'path': path, 'count': 1} == index.handler(event, None)