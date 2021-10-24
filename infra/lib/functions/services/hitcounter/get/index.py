import os
import json
from typing import Dict, Any

TABLE = None


def handler(event: Dict[str, Any], context: Any):
    print(json.dumps(event))

    global TABLE
    if not TABLE:
        TABLE = os.environ['TABLE_NAME']

    return 0