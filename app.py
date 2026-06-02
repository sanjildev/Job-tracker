from flask import Flask
from models import db,Job
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///jobs.db'

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    return 'Job Tracker is running'
if __name__=='__main__':
    app.run(debug=True)