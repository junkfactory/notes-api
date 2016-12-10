import uuid

schema = {
    "token": {
        "type": "string",
        "minlength": 1,
        "maxlength": 36,
        "default": uuid.uuid4().get_hex()
    },
    "entity_id": {
        "type": "string",
        "minlength": 1,
        "maxlength": 36
    },
    "entity_type": {
        "type": "string",
        "minlength": 1,
        "maxlength": 24
    },
    "entity_note": {
        "type": "string",
        "minlength": 1
    },
    "created_by": {
        "type": "string",
        "minlength": 1,
        "maxlength": 24
    }
}


note = {
    'item_title': 'note',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': schema,
    'resource_methods': ['GET', 'POST']
}
