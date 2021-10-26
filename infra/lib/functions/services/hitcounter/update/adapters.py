if not __package__:
    from ports import UpdateTable, UpdateAdapter
else:
    from .ports import UpdateTable, UpdateAdapter


class DdbUpdateAdapter(UpdateAdapter):
    def __init__(self, table: UpdateTable):
        self.table = table

    def update(self, path: str):
        resp = self.table.update_item(
            Key={ 'PK': path },
            UpdateExpression='ADD hitCount :v',
            ExpressionAttributeValues={
                ':v': 1
            },
            ReturnValues='UPDATED_NEW',
        )
        return resp['Attributes']['hitCount']