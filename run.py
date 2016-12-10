from eve import Eve
from app.notes import pre_insert_notes
from flask_script import Manager

app = Eve()
app.on_insert_notes += pre_insert_notes

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
