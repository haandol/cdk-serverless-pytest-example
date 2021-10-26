from ... import BaseTestCase
from services.hitcounter.update import service


class TestService(BaseTestCase):
    def beforeEach(self):
        self.load_fixture('hitcounter-update.json')

    def test_success_with_no_activity(self):
        path = 'no-activity'
        count = service.update_count(path)
        assert 1 == count

    def test_success_with_some_activity(self):
        path = 'test'
        count = service.update_count(path)
        assert 3 == count