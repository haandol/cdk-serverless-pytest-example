from ... import BaseTestCase
from services.hitcounter.update import adapters


class TestDdbUpdateAdapter(BaseTestCase):
    def beforeEach(self):
        self.load_fixture('hitcounter-update.json')
        self.adapter = adapters.DdbUpdateAdapter(self.table)

    def test_success_with_no_activity(self):
        path = 'no-activity'
        assert 1 == self.adapter.update(path)

    def test_success_with_activity(self):
        path = 'test'
        assert 3 == self.adapter.update(path)