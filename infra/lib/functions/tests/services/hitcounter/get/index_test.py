import os
from unittest import mock
from .... import BaseTestCase, TABLE_NAME
from services.hitcounter.get import index


class TestHitCounterGet(BaseTestCase):

    @mock.patch.dict(os.environ, {'TABLE_NAME': TABLE_NAME})
    def test_handler(self):
        event = self.load_event('hitcounter-get.json')
        assert 0 == index.handler(event, None)