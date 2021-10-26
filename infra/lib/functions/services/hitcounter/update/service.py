import os
import boto3
if not __package__:
    from adapters import DdbUpdateAdapter
else:
    from .adapters import DdbUpdateAdapter

table = None


def update_count(path: str):
    global table
    if not table:
        dynamodb = boto3.resource('dynamodb')
        TableName = os.environ['TABLE_NAME']
        table = dynamodb.Table(TableName)

    updateAdapter = DdbUpdateAdapter(table=table)
    return updateAdapter.update(path)