from .... import BaseTestCase
from services.hitcounter.update import index


class TestHitCounterUpdate(BaseTestCase):
    def test_handler(self):
        event = self.load_event('hitcounter-update.json')
        assert 'ok' == index.handler(event, None)