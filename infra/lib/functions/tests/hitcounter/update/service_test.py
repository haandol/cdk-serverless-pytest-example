from ... import BaseTestCase
from hitcounter.update import services


class TestService(BaseTestCase):
    def beforeEach(self):
        self.load_fixture('hitcounter-update.json')

    def test_success_with_no_activity(self):
        path = 'no-activity'
        count = services.update_count(path)
        assert 1 == count

    def test_success_with_some_activity(self):
        path = 'test'
        count = services.update_count(path)
        assert 3 == count