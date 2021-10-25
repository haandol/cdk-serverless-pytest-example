import os
import json
import boto3
from typing import Dict, Any

TableName = None
Table = None


def update(table, path: str):
    resp = table.update_item(
        Key={ 'PK': path },
        UpdateExpression='ADD hitCount :v',
        ExpressionAttributeValues={
            ':v': 1
        },
        ReturnValues='UPDATED_NEW',
    )
    return resp['Attributes']['hitCount']


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))
    global TableName
    if TableName is None:
        TableName = os.environ['TABLE_NAME']

    global Table
    if Table is None:
        dynamodb = boto3.resource('dynamodb')
        Table = dynamodb.Table(TableName)

    path = event['pathParameters']['proxy']
    count = update(Table, path)
    return {
        'path': path,
        'count': count
    }