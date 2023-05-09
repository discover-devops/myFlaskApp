from main import create_app, db

#this will just create the DB tables
#run as below:
# (venv) c:\PythonWorkspace\FlaskAppUTest>python buildDb.py

app = create_app('prod.cfg')
with app.app_context():
    db.drop_all()
    db.create_all()