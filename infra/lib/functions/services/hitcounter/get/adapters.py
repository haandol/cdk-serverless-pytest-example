if __package__ is None:
    from ports import FetchTable, FetchAdapter
else:
    from .ports import FetchTable, FetchAdapter


class DdbFetchAdapter(FetchAdapter):
    def __init__(self, table: FetchTable):
        self.table = table

    def fetch(self, path: str):
        resp = self.table.get_item(
            Key={ 'PK': path },
        )
        if 'Item' in resp:
            return int(resp['Item']['hitCount'])
        else:
            return 0