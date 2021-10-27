import json
from typing import Dict, Any
from .service import get_count
from ..common import response


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))

    path = event['pathParameters']['proxy']
    if not path:
        return response.error(400, body='no path given')

    count = get_count(path)
    return response.success(body=json.dumps({
        'path': path,
        'count': count,
    }))