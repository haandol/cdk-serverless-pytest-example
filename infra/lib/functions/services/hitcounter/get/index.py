import json
from typing import Dict, Any
from .service import get_count
from .responses import success, error


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))

    path = event['pathParameters']['proxy']
    if not path:
        return error(
            400, body='no path given', error_type='BadRequest'
        )

    count = get_count(path)
    return success(body=json.dumps({
        'path': path,
        'count': count,
    }))