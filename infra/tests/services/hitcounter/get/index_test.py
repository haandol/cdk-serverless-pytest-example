from .... import BaseTestCase
from services.hitcounter.get import index, adapters


class TestDdbRepository(BaseTestCase):
    def beforeEach(self):
        self.load_fixture('hitcounter-get.json')

    def test_success_with_no_activity(self):
        path = 'no-activity'
        adapter = adapters.DdbFetchAdapter(self.table)
        assert 0 == adapter.fetch(path)

    def test_success_with_activity(self):
        path = 'test'
        adapter = adapters.DdbFetchAdapter(self.table)
        assert 2 == adapter.fetch(path)


class TestE2E(BaseTestCase):
    def test_handler(self):
        event = self.load_event('hitcounter-get.json')
        path = event['pathParameters']['proxy']
        assert 'test' == path
        assert index.handler(event, None) == {
            'path': path,
            'count': 0,
        }