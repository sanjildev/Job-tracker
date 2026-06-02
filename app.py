from flask import Flask,render_template,request,redirect,url_for
from datetime import date
from models import db,Job
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///jobs.db'

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def home():
    jobs=Job.query.all()
    return render_template('home.html',jobs=jobs)

@app.route('/add',methods=["GET","POST"])
def add_job():
    if request.method=="POST":
        company=request.form.get('company')
        role=request.form.get('role')
        status=request.form.get('status')
        date_applied=date.fromisoformat(request.form.get('date_applied'))
        deadline = request.form.get('deadline')
        deadline = date.fromisoformat(deadline) if deadline else None
        notes=request.form.get('notes')
        job_link=request.form.get('job_link')
        job=Job(company=company,role=role,status=status,date_applied=date_applied,deadline=deadline,notes=notes,job_link=job_link)
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit_job(id):
    job=Job.query.get_or_404(id)
    if request.method=="POST":
        job.company=request.form.get('company')
        job.role=request.form.get('role')
        job.status=request.form.get('status')
        job.date_applied=date.fromisoformat(request.form.get('date_applied'))
        deadline = request.form.get('deadline')
        job.deadline=date.fromisoformat(deadline) if deadline else None
        job.notes=request.form.get('notes')
        job.job_link=request.form.get('job_link')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',job=job)
@app.route('/delete/<int:id>')
def delete_job(id):
    job=Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('home'))
if __name__=='__main__':
    app.run(debug=True)