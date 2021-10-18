from app.utils.db import *
from flask_sqlalchemy import SQLAlchemy
from app.model.details import Details1
from api import db
import datetime
import pytz

class Details(db.Model):
    def json(self):
        return {'id': self.id, 'User name': self.user_name, 'User_mail': self.user_email,'Status':self.status}
    
    def get_date_time():
        current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        return str(current_time)[:-13]

    def get_all_details():
        return [Details.json(details) for details in Details1.query.all()]

    def update_detail(id,status):
        detail=Details1.query.filter_by(id=id).first()
        if(detail.status == None):
            detail.status=status
            db.session.commit()
            return 1;
        else:
            return 0;
