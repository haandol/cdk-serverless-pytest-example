import os
import json
import boto3
from typing import Dict, Any
from ports import FetchAdapter
from adapters import DdbFetchAdapter

TableName: str = None
fetchAdapter: FetchAdapter = None


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))
    global TableName
    if TableName is None:
        TableName = os.environ['TABLE_NAME']

    global fetchAdapter
    if not fetchAdapter:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(TableName)
        fetchAdapter = DdbFetchAdapter(table=table)

    path = event['pathParameters']['proxy']
    count = fetchAdapter.fetch(path)
    return {
        'path': path,
        'count': count,
    }