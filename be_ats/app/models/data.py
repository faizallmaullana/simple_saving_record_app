from app import db
import uuid
from datetime import datetime
import pytz

class Incomes(db.Model):
    __tablename__ = 'Icomes'

    id_income = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    income = db.Column(db.Integer)
    keterangan = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Jakarta')))    
    
    def get_id(self):
        return str(self.id_income)

class Outcomes(db.Model):
    __tablename__ = 'Outcomes'

    id_outcome = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    outcome = db.Column(db.Integer)
    keterangan = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Jakarta')))    
    
    def get_id(self):
        return str(self.id_outcome)
