from flask.json import jsonify
from app.utils.db import *
from flask_sqlalchemy import SQLAlchemy
from app.model.details import Details1
from api import db
import datetime
import pytz
import mysql.connector
import smtplib, ssl
import schedule
import time
from email.message import EmailMessage

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

    def send_mail(email,id):
        msg = EmailMessage()
        msg['Subject'] = "Check out and fill in the status" 
        msg['From'] = "xabc0604@gmail.com"
        msg['To'] = email
        msg.set_content("Kindly fill the status !!")

        msg.add_alternative("""\
            <html>
                <body>
                    <h1>The button Element</h1>
                    <button type="button" onclick=yfunc()>Accept the request</button>
                    <br><br>
                    <button type="button" onclick="alert("Hello World!")">Reject the request</button>
                </body>
            </html>
        """,subtype='html')

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("xabc0604@gmail.com", "Ethicalhacking@9")
        s.send_message(msg)

        print("Email sent to ", email)
        s.quit()
        return None;
    
    
    def check_database():
        l=[Details.json(details) for details in Details1.query.all()]
        for i in l:
            # print(i)
            print(i['User_mail'],i['Status'])
            if(i['Status']==None):
                Details.send_mail(i['User_mail'],i['id'])   
        return jsonify({"MSG":"Email sent!!"})
                

    # def check_status():
    #     schedule.every(1).minutes.do(check_database)