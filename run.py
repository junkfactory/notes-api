from eve import Eve
from app.notes import pre_insert_notes

app = Eve()
app.on_insert_notes += pre_insert_notes

if __name__ == '__main__':
    app.run()
