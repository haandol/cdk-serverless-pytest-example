import json
from typing import Dict, Any


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))
    return 'ok'