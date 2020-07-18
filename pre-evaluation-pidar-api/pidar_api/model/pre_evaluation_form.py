import json
from datetime import date

class PreEvaluationForm(object):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.code = ""
        self.department = ""

def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__
