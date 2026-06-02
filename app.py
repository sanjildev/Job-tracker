from flask import Flask,render_template,request,redirect,url_for
from datetime import datetime
from models import db,Job
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///jobs.db'

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    return 'Job Tracker is running'

@app.route('/add',methods=["GET","POST"])
def add_job():
    if request.method=="POST":
        company=request.form.get('company')
        role=request.form.get('role')
        status=request.form.get('status')
        date_applied=datetime.strptime(request.form.get('date_applied'),'%Y-%m-%d').date()
        deadline = request.form.get('deadline')
        deadline = datetime.strptime(deadline, '%Y-%m-%d').date() if deadline else None
        notes=request.form.get('notes')
        job_link=request.form.get('job_link')
        job=Job(company=company,role=role,status=status,date_applied=date_applied,deadline=deadline,notes=notes,job_link=job_link)
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')
if __name__=='__main__':
    app.run(debug=True)