from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Job(db.Model):
    __tablename__='jobs'
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(100),nullable=False)
    role=db.Column(db.String(100),nullable=False)
    status=db.Column(db.String(100),nullable=False)
    date_applied=db.Column(db.Date,nullable=False)
    deadline=db.Column(db.Date)
    notes=db.Column(db.String(250))
    job_link=db.Column(db.String(250))
    def __repr__(self):
        return f'<Job {self.company} - {self.role}>'
    