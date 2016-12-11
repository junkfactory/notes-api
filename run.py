from eve import Eve
from app.notes import pre_insert_notes
from app.notes.controller import custom_notes
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Eve()
app.on_insert_notes += pre_insert_notes
Bootstrap(app)
app.register_blueprint(custom_notes, url_prefix='/custom_notes')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
