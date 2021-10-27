import json
from typing import Dict, Any
from .service import get_count


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))

    path = event['pathParameters']['proxy']
    if not path:
        return {
            'statusCode': 400,
            'message': 'no path given',
        }

    count = get_count(path)
    return {
        'path': path,
        'count': count,
    }