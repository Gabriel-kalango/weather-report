from ..utils import db
from datetime import datetime,timezone

class Weather(db.Model):
    '''Model for the creating weather data'''
    __tablename__ ='weather'
    id=db.Column(db.Integer, primary_key=True)
    city=db.Column(db.String(250),unique=True,nullable=False)
    date=db.Column(db.DateTime,default=lambda: datetime.now(timezone.utc))
    temperature=db.Column(db.Float,nullable=False)
    description=db.Column(db.String(250),nullable=False)


    def save(self):
        '''save to database'''
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        "update data in database"
        db.session.commit()


    def __str__(self):
        """return string representation of our weather"""
        return self.city