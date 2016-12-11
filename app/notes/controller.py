from flask import Blueprint, current_app as app, json
from bson.objectid import ObjectId

custom_notes = Blueprint('custom_notes', __name__)

"""
Sample custom webservice
"""


@custom_notes.route('/<note_id>', methods=['GET'])
def index(note_id):
    notes = app.data.driver.db['notes']
    note = notes.find_one({'_id': ObjectId(note_id)})
    return json.dumps(note, cls=app.data.json_encoder_class)

