import os
import json
import boto3
from typing import Dict, Any
if not __package__:
    from ports import UpdateAdapter
    from adapters import DdbUpdateAdapter
else:
    from .ports import UpdateAdapter
    from .adapters import DdbUpdateAdapter

updateAdapter: UpdateAdapter = None


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))

    global updateAdapter
    if not updateAdapter:
        dynamodb = boto3.resource('dynamodb')
        TableName = os.environ['TABLE_NAME']
        table = dynamodb.Table(TableName)
        updateAdapter = DdbUpdateAdapter(table=table)
 
    path = event['pathParameters']['proxy']
    count = updateAdapter.update(path)
    return {
        'path': path,
        'count': count,
    }