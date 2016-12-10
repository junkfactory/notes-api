# Notes API
Remembering what you cannot

### Create a note
Request 
```bash
curl -H 'Content-type: application/json' -X POST 'http://127.0.0.1:5000/notes' -d \
'{
    "token" : "token1",
    "entity_id" : "1",
    "entity_type" : "transaction",
    "entity_note" : "This is a note"
}'
```
Response
```json
{
    "_updated": "Sat, 10 Dec 2016 04:52:14 GMT",
    "entity_id": "1",
    "entity_note": "This is a note",
    "entity_type": "transaction",
    "token": "token-100",
    "_links": {
        "self": {
            "href": "notes/584b89fe9005a933789e4bfc",
            "title": "note"
        },
        "collection": {
            "href": "notes?pretty=",
            "title": "notes"
        },
        "parent": {
            "href": "/",
            "title": "home"
        }
    },
    "_created": "Sat, 10 Dec 2016 04:52:14 GMT",
    "_id": "584b89fe9005a933789e4bfc",
    "_etag": "f826a2f0476f341b54582b8587d5189b7c7b8c1d"
}
```
### Update a note
Request
```bash
curl -H 'Content-type: application/json' -X PUT 'http://127.0.0.1:5000/notes/584b89fe9005a933789e4bfc' -d \
'{
    "entity_note" : "This is a notesssss"
}'
```
# Setup Dev Environment
Create python virtualenv and install eve
```bash
$ mkdir eve
$ cd eve
$ virtualenv venv
$ . venv/bin/activate
New python executable in venv/bin/python

$ pip install git+git://github.com/nicolaiarocci/eve.git
```