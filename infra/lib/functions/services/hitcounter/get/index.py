import os
import json
import boto3
from typing import Dict, Any
if not __package__:
    from ports import FetchAdapter
    from adapters import DdbFetchAdapter
else:
    from .ports import FetchAdapter
    from .adapters import DdbFetchAdapter

fetchAdapter: FetchAdapter = None


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))

    global fetchAdapter
    if not fetchAdapter:
        dynamodb = boto3.resource('dynamodb')
        TableName = os.environ['TABLE_NAME']
        table = dynamodb.Table(TableName)
        fetchAdapter = DdbFetchAdapter(table=table)

    path = event['pathParameters']['proxy']
    count = fetchAdapter.fetch(path)
    return {
        'path': path,
        'count': count,
    }