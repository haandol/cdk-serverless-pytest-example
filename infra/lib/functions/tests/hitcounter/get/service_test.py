from ... import BaseTestCase
from services.hitcounter.get import service


class TestService(BaseTestCase):
    def beforeEach(self):
        self.load_fixture('hitcounter-get.json')

    def test_success_with_no_activity(self):
        path = 'no-activity'
        count = service.get_count(path)
        assert 0 == count

    def test_success_with_some_activity(self):
        path = 'test'
        count = service.get_count(path)
        assert 2 == count